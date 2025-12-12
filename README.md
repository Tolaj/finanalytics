# 📘 finanalytics — Financial Calculations Package

A complete Python package for performing essential financial mathematics, including:

- Time Value of Money  
- Cash Flow Analysis  
- Loan & Amortization Calculations  
- Depreciation Methods  
- Bond Valuation & Interest Rate Sensitivity  
- Financial Visualizations  

This package is built entirely using numerical methods, algebra, and financial formulas — no machine learning.  
Ideal for academic projects, finance learning, and professional analysis.

![License](https://img.shields.io/badge/license-MIT-blue.svg)  
![Python](https://img.shields.io/badge/python-3.9+-blue)  
![Status](https://img.shields.io/badge/status-active-success)

---

## 📄 Documentation

See full documentation and guidelines:

- **Contribution Guidelines** → [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)
- __Commit Rules__ → [docs/COMMIT_RULES.md](docs/COMMIT_RULES.md)
- __Code of Conduct__ → [docs/CODE_OF_CONDUCT.md](docs/CODE_OF_CONDUCT.md)
- __Bug Report Template__ → [.github/ISSUE_TEMPLATE/bug_report.md](.github/ISSUE_TEMPLATE/bug_report.md)
- __Feature Request Template__ → [.github/ISSUE_TEMPLATE/feature_request.md](.github/ISSUE_TEMPLATE/feature_request.md)
- __Pull Request Template__ → [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md)

---


## 🚀 Features Overview

### ✔ 1. Time Value of Money (TVM)
- Present Value (PV)  
- Future Value (FV)  
- Discount Factor  
- Effective Annual Rate (EAR)  
- Continuous compounding  
- Net Present Value (NPV)

---

### ✔ 2. Cash Flow Analysis
- Internal Rate of Return (IRR)  
- Modified IRR (MIRR)  
- Payback Period  
- Discounted Payback Period  
- Cumulative Cashflow  
- Cashflow Diagrams  

---

### ✔ 3. Loan Calculations
- Mortgage/loan payment (EMI)  
- Amortization schedule  
- Interest vs principal split  
- Remaining balance  

---

### ✔ 4. Asset Depreciation
- Straight-line depreciation  
- Declining balance  
- Double declining balance (DDB)  
- Sum-of-years-digits (SYD)  
- Book value tracking  

---

### ✔ 5. Bond Valuation
- Bond price  
- Yield to Maturity (YTM)  
- Duration  
- Modified Duration  
- Convexity  

---

### ✔ 6. Visualization Tools
- Cashflow bar plots  
- Loan amortization graphs  
- Depreciation curves  
- NPV profile charts  
- PV/FV growth curves  

(Uses matplotlib)

---

## 📁 Project Structure

```
finanalytics/
│── README.md
│── setup.py
│── requirements.txt
│── examples/
│   └── demo_examples.py
└── modules/
    ├── __init__.py
    ├── time_value.py
    ├── cashflow.py
    ├── loans.py
    ├── depreciation.py
    ├── bonds.py
    └── visualization.py
```

---

## 🔧 Installation

### Install dependencies
```
pip install -r requirements.txt
```

### Install package locally
```
pip install .
```

### Import in Python
```python
import fincalc
from fincalc import time_value, cashflow, loans, depreciation, bonds, visualization
```

---

# 🎯 Usage Examples

Below are usage samples for each module.  
Full examples available in `examples/demo_examples.py`.

---

## 1️⃣ Time Value of Money

```python
from fincalc import time_value

fv = time_value.future_value(1000, rate=0.08, years=5)
pv = time_value.present_value(2000, rate=0.05, years=3)
npv = time_value.net_present_value(0.08, [-1000, 300, 300, 300, 400])

print("Future Value:", fv)
print("Present Value:", pv)
print("NPV:", npv)
```

---


## 2️⃣ Cash Flow Analysis

```python
from fincalc import cashflow

cfs = [-1000, 300, 300, 300, 400]

irr = cashflow.internal_rate_of_return(cfs)
mirr = cashflow.modified_irr(cfs, finance_rate=0.08, reinvest_rate=0.06)
payback = cashflow.payback_period(cfs)
discounted_pb = cashflow.discounted_payback(cfs, rate=0.08)

print("IRR:", irr)
print("MIRR:", mirr)
print("Payback:", payback)
print("Discounted Payback:", discounted_pb)
```

### Visualize cashflows
```python
from fincalc import visualization as viz
viz.plot_cashflows(cfs)
```

---

## 3️⃣ Loan Payment & Amortization

```python
from fincalc import loans

payment = loans.loan_payment(200000, annual_rate=0.05, years=30)
schedule = loans.amortization_schedule(200000, 0.05, 30)

print("Monthly Payment:", payment)
print("First Entry:", schedule[0])
```

### Plot amortization
```python
from fincalc import visualization as viz
viz.plot_amortization(schedule)
```

---

## 4️⃣ Asset Depreciation

```python
from fincalc import depreciation

deps = depreciation.straight_line(10000, salvage=1000, life=5)
ddb = depreciation.double_declining_balance(10000, life=5)

print("Straight-line Depreciation:", deps)
print("Double Declining Balance:", ddb)
```

### Plot depreciation
```python
from fincalc import visualization as viz
viz.plot_depreciation(deps)
```

---

## 5️⃣ Bond Valuation

```python
from fincalc import bonds

price = bonds.bond_price(1000, coupon_rate=0.05, yield_rate=0.06, years=10)
ytm = bonds.yield_to_maturity(price, 1000, 0.05, 10)
duration = bonds.duration(1000, 0.05, 0.06, 10)
convexity = bonds.convexity(1000, 0.05, 0.06, 10)

print("Bond Price:", price)
print("YTM:", ytm)
print("Duration:", duration)
print("Convexity:", convexity)
```

---

# 📈 Visualization Examples

### NPV Profile
```python
import numpy as np
from fincalc import time_value, visualization as viz

rates = np.linspace(0.01, 0.2, 20)
cfs = [-1000, 300, 300, 300, 400]
npvs = [time_value.net_present_value(r, cfs) for r in rates]

viz.plot_npv_profile(rates, npvs)
```

---






# 🧪 Testing

Recommended tests:

- PV/FV formula accuracy  
- IRR convergence correctness  
- Payback logic  
- Amortization schedule correctness  
- Depreciation totals  
- Bond price vs yield monotonicity  

Unit tests can be added under a `tests/` folder.

---

# 📦 Build & Distribution

Build distribution:
```
python setup.py sdist bdist_wheel
```

Install locally:
```
pip install dist/fincalc-0.1.0-py3-none-any.whl
```

---

## 🛠 Technologies Used

- Python 3.8+  
- NumPy  
- Matplotlib  

---

# ⭐ Why This Project Is Valuable

This toolkit replicates real-world financial analyst workflows for:

- Investment return evaluation (IRR/NPV)  
- Business project analysis  
- Loan & mortgage planning  
- Asset valuation & accounting  
- Bond pricing & interest rate sensitivity  

Mathematically rigorous yet easy to use — ideal for academic submission or personal finance automation.

---

# 📄 License

MIT License

---


# 🎉 Author

**Swapnil Jadhav and Akash Kulkarni**
