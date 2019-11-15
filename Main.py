"""
    An integration of everything I have learned about programming in Python

    __author__ = "Prof. Vanselow"
"""

import POGIL04
from POGIL05 import comparison_operators
from POGIL06 import demonstrate_decisions
from POGIL07 import demonstrate_decisions_elif


def main():
    """
        The starting point of the program. Displays a menu of all options.
    """
    print("Welcome to my Integration Project!")
    continue_program = True
    while continue_program:
        print("Enter the choice for what you would like to see")
        print("1. Output formatting")
        print("2. Comparison operators")
        print("3. Decision statements")
        print("4. Decision statements elif")
        print("5. Quit")

        user_choice = int(input())

        if user_choice == 1:
            POGIL04.do_output_format_demo()
        elif user_choice == 2:
            comparison_operators()
        elif user_choice == 3:
            demonstrate_decisions()
        elif user_choice == 4:
            demonstrate_decisions_elif()
        elif user_choice == 5:
            continue_program = False
        else:
            print("Invalid selection. Try again.")


main()
