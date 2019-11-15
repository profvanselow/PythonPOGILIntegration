"""
    Price Calculator.
"""


def price_calculator():
    """
        Demonstrates comparison operators.
    """
    price1 = float(input("Enter the price of the first item: "))
    price2 = float(input("Enter the price of the second item: "))
    payment = float(input("Enter the payment amount: "))
    difference = payment - price1 - price2
    if difference >= 0:
        print("Thank you, your change is ${:,.2f}".format(difference))
    else:
        print("You still owe ${:,.2f}".format(-difference))
