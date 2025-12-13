from typing import List


def straight_line(cost: float, salvage: float, life: int) -> List[float]:

    if life <= 0:
        raise ValueError("Life must be positive.")
    dep = (cost - salvage) / life
    return [dep for _ in range(life)]


def declining_balance(cost: float, life: int, rate: float) -> List[float]:

    if life <= 0:
        raise ValueError("Life must be positive.")
    if rate <= 0 or rate >= 1:
        raise ValueError("Rate should be between 0 and 1.")
    deps = []
    book_value = cost
    for _ in range(life):
        dep = rate * book_value
        deps.append(dep)
        book_value -= dep
    return deps


def double_declining_balance(cost: float, life: int) -> List[float]:

    if life <= 0:
        raise ValueError("Life must be positive.")
    rate = 2.0 / life
    deps = []
    book_value = cost
    for _ in range(life):
        dep = rate * book_value
        if dep > book_value:
            dep = book_value
        deps.append(dep)
        book_value -= dep
    return deps


def sum_of_years_digits(cost: float, salvage: float, life: int) -> List[float]:

    if life <= 0:
        raise ValueError("Life must be positive.")
    base = cost - salvage
    syd_sum = life * (life + 1) / 2
    deps = []
    for year in range(1, life + 1):
        remaining_life = life - year + 1
        dep = (remaining_life / syd_sum) * base
        deps.append(dep)
    return deps


def book_value(cost: float, depreciation_taken: float) -> float:

    return cost - depreciation_taken
