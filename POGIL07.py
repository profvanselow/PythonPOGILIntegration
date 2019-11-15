"""
    Code from POGIL 7.

    __author__ = "Prof. Vanselow"
"""


def demonstrate_decisions_elif():
    """
        Demonstrates elif statements.
    """

    sales = int(input("Enter sales:"))
    if sales >= 100000:
        bonus = 10000
    elif sales >= 75000:
        bonus = 5000
    elif sales >= 50000:
        bonus = 2500
    elif sales >= 25000:
        bonus = 1000
    else:
        bonus = 0
    print("Your bonus is ${:,.2f}".format(bonus))
