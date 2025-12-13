from finalytics import (
    time_value,
    cashflow,
    loans,
    depreciation,
    bonds,
    visualization,
)

# Demonstrates basic time value of money calculations like Future Value and Present Value
def demo_time_value():
    print("=== Time Value of Money Demo ===")
    # Updated 'rate' -> 'annual_rate' to match the optimized time_value.py
    future_amt = time_value.future_value(1000, annual_rate=0.08, years=5)
    present_amt = time_value.present_value(2000, annual_rate=0.05, years=3)
    print("FV of 1000 at 8% for 5 years:", future_amt)
    print("PV of 2000 at 5% in 3 years:", present_amt)


# Illustrates cash flow metrics including IRR, MIRR, and Payback periods
def demo_cashflow():
    print("\n=== Cash Flow Demo ===")
    project_streams = [-1000, 300, 300, 300, 400]
    int_rate_return = cashflow.internal_rate_of_return(project_streams)
    mod_irr = cashflow.modified_irr(project_streams, finance_rate=0.08, reinvest_rate=0.06)
    payback_time = cashflow.payback_period(project_streams)
    disc_payback = cashflow.discounted_payback(project_streams, rate=0.08)
    
    print("Cashflows:", project_streams)
    print("IRR:", int_rate_return)
    print("MIRR:", mod_irr)
    print("Payback period:", payback_time)
    print("Discounted payback:", disc_payback)
    visualization.plot_cashflows(project_streams, chart_title="Project Cash Flows")


# Shows loan payment calculations and generates an amortization schedule
def demo_loans():
    print("\n=== Loan Demo ===")
    monthly_installment = loans.loan_payment(principal=200000, annual_rate=0.05, years=30)
    print("Monthly payment on 200k at 5% for 30 years:", monthly_installment)
    
    payoff_plan = loans.amortization_schedule(200000, 0.05, 30)
    print("First 3 periods of schedule:")
    for record in payoff_plan[:3]:
        print(record)
    visualization.plot_amortization(payoff_plan, chart_title="Mortgage Amortization")


# Displays depreciation calculations using straight-line method
def demo_depreciation():
    print("\n=== Depreciation Demo ===")
    annual_loss = depreciation.straight_line(cost=10000, salvage=1000, life=5)
    print("Straight-line depreciation:", annual_loss)
    visualization.plot_depreciation(annual_loss, chart_title="Straight-Line Depreciation")


# Calculates bond pricing, yield to maturity, duration, and convexity metrics
def demo_bonds():
    print("\n=== Bonds Demo ===")
    curr_val = bonds.bond_price(
        face_value=1000, coupon_rate=0.05, yield_rate=0.06, years=10
    )
    yield_mat = bonds.yield_to_maturity(curr_val, face_value=1000, coupon_rate=0.05, years=10)
    mac_dur = bonds.duration(1000, 0.05, 0.06, 10)
    mod_dur = bonds.modified_duration(1000, 0.05, 0.06, 10)
    cvx_val = bonds.convexity(1000, 0.05, 0.06, 10)
    
    print("Bond price (5% coupon, 6% yield):", curr_val)
    print("Implied YTM from price:", yield_mat)
    print("Duration:", mac_dur)
    print("Modified Duration:", mod_dur)
    print("Convexity:", cvx_val)


if __name__ == "__main__":
    demo_time_value()
    demo_cashflow()
    demo_loans()
    demo_depreciation()
    demo_bonds()