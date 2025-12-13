import math
from typing import Iterable, List

# Calculates the future value of a lump sum investment with periodic compounding
def future_value(present_val: float, annual_rate: float, years: float, comp_freq: int = 1) -> float:
    periodic_rate = annual_rate / comp_freq
    total_periods = comp_freq * years
    return present_val * (1 + periodic_rate) ** total_periods


# Calculates the present value required to reach a specific future amount
def present_value(future_val: float, annual_rate: float, years: float, comp_freq: int = 1) -> float:
    periodic_rate = annual_rate / comp_freq
    total_periods = comp_freq * years
    return future_val / ((1 + periodic_rate) ** total_periods)


# Computes the simple annual discount factor
def discount_factor(annual_rate: float, years: float) -> float:
    return 1.0 / ((1.0 + annual_rate) ** years)


# Converts a nominal interest rate to an effective annual rate based on compounding frequency
def effective_annual_rate(nominal_rate: float, comp_freq: int) -> float:
    return (1 + nominal_rate / comp_freq) ** comp_freq - 1


# Calculates future value using continuous compounding
def continuous_future_value(present_val: float, annual_rate: float, years: float) -> float:
    return present_val * math.exp(annual_rate * years)


# Calculates present value using continuous discounting
def continuous_present_value(future_val: float, annual_rate: float, years: float) -> float:
    return future_val * math.exp(-annual_rate * years)


# Computes the Net Present Value (NPV) for a series of cash flows
def net_present_value(discount_rate: float, cashflows: Iterable[float]) -> float:
    return sum(cf / ((1 + discount_rate) ** t) for t, cf in enumerate(cashflows))