"""
    Code from POGIL 10.

    __author__ = "Prof. Vanselow"
"""


def demonstrate_while():
    """
        Demonstrates while statements.
    """

    name = input("What is your name: ")
    columns = 5
    for x in range(columns):
        for y in range(3):
            print(name + " ", end=" ")
            print("* ", end=" ")
        print()

    height = int(input("Enter height: "))
    for row in range(1, height + 1):
        for column in range(row):
            print(row, end=" ")
        print()
