from typing import List, Dict

# Calculates the periodic installment amount required to fully repay a loan
def loan_payment(principal: float, annual_rate: float, years: float, payments_per_year: int = 12) -> float:
    p_rate = annual_rate / payments_per_year
    total_periods = int(years * payments_per_year)
    if p_rate == 0:
        return principal / total_periods
    return principal * p_rate / (1 - (1 + p_rate) ** -total_periods)


# Generates a complete breakdown of payments, interest, and equity over the life of the loan
def amortization_schedule(principal: float, annual_rate: float, years: float, payments_per_year: int = 12) -> List[Dict]:
    plan = []
    installment = loan_payment(principal, annual_rate, years, payments_per_year)
    p_rate = annual_rate / payments_per_year
    total_periods = int(years * payments_per_year)
    curr_bal = principal

    for step in range(1, total_periods + 1):
        interest_amt = curr_bal * p_rate
        principal_amt = installment - interest_amt
        
        # Handle final rounding differences
        if principal_amt > curr_bal:
            principal_amt = curr_bal
            installment = interest_amt + principal_amt
            
        curr_bal -= principal_amt
        plan.append({
            "period": step,
            "payment": installment,
            "interest": interest_amt,
            "principal": principal_amt,
            "balance": curr_bal
        })
        if curr_bal <= 1e-8:
            break

    return plan


# Calculates the remaining debt after a specific number of payments have been made using a direct formula
def remaining_balance(principal: float, annual_rate: float, years: float, payments_made: int, payments_per_year: int = 12) -> float:
    p_rate = annual_rate / payments_per_year
    total_periods = int(years * payments_per_year)
    
    if payments_made <= 0:
        return principal
    if payments_made >= total_periods:
        return 0.0

    # Optimization: Direct calculation instead of iterating through schedule
    numerator = (1 + p_rate) ** total_periods - (1 + p_rate) ** payments_made
    denominator = (1 + p_rate) ** total_periods - 1
    return principal * (numerator / denominator)


# Determines how much of a single payment goes toward interest versus principal
def interest_principal_split(payment: float, annual_rate: float, balance: float, payments_per_year: int = 12) -> Dict[str, float]:
    p_rate = annual_rate / payments_per_year
    int_part = balance * p_rate
    prin_part = payment - int_part
    return {"interest": int_part, "principal": prin_part}