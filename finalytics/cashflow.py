from typing import Iterable, List, Dict, Tuple
from .time_value import net_present_value


def internal_rate_of_return(
    cashflows: Iterable[float],
    guess_low: float = -0.9999,
    guess_high: float = 1.0,
    tol: float = 1e-6,
    max_iter: int = 1000,
) -> float:
    cfs = list(cashflows)

    npv_low = net_present_value(guess_low, cfs)
    npv_high = net_present_value(guess_high, cfs)

    if npv_low * npv_high > 0:
        raise ValueError(
            "IRR search interval does not bracket a root. "
            "Try different guess_low/guess_high."
        )

    low, high = guess_low, guess_high
    for _ in range(max_iter):
        mid = (low + high) / 2.0
        npv_mid = net_present_value(mid, cfs)

        if abs(npv_mid) < tol:
            return mid
        if npv_low * npv_mid < 0:
            high = mid
            npv_high = npv_mid
        else:
            low = mid
            npv_low = npv_mid

    # If we exit loop, return midpoint as approximation
    return (low + high) / 2.0


def modified_irr(
    cashflows: Iterable[float], finance_rate: float, reinvest_rate: float
) -> float:

    cfs = list(cashflows)
    n = len(cfs)
    if n < 2:
        raise ValueError("Need at least 2 cash flows for MIRR.")

    pv_neg = 0.0

    fv_pos = 0.0

    for t, cf in enumerate(cfs):
        if cf < 0:
            pv_neg += cf / ((1 + finance_rate) ** t)
        elif cf > 0:
            fv_pos += cf * ((1 + reinvest_rate) ** (n - 1 - t))

    if pv_neg >= 0:
        raise ValueError("No negative cash flows found; MIRR undefined.")

    mirr = (fv_pos / -pv_neg) ** (1 / (n - 1)) - 1
    return mirr


def cumulative_cashflow(cashflows: Iterable[float]) -> List[float]:

    cum = []
    total = 0.0
    for cf in cashflows:
        total += cf
        cum.append(total)
    return cum


def payback_period(cashflows: Iterable[float]) -> float:

    cfs = list(cashflows)
    cum = 0.0
    for t in range(len(cfs)):
        cum += cfs[t]
        if cum >= 0:

            prev_cum = cum - cfs[t]
            if cfs[t] == 0:
                return float(t)
            frac = (0 - prev_cum) / cfs[t]
            return (t - 1) + frac if t > 0 else frac

    return float("inf")


def discounted_payback(cashflows: Iterable[float], rate: float) -> float:

    cfs = list(cashflows)
    cum = 0.0
    for t in range(len(cfs)):
        discounted_cf = cfs[t] / ((1 + rate) ** t)
        cum += discounted_cf
        if cum >= 0:
            prev_cum = cum - discounted_cf
            if discounted_cf == 0:
                return float(t)
            frac = (0 - prev_cum) / discounted_cf
            return (t - 1) + frac if t > 0 else frac
    return float("inf")
