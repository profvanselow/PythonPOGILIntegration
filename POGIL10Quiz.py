"""
    Quiz from POGIL 10.

    __author__ = "Prof. Vanselow"
"""


def get_quiz_average():
    """
        Demonstrates nested loops.
    """

    print("This is a demonstration of a nested loop.")
    for student in range(3):
        name = input()
        total = 0
        for quiz in range(3):
            score = int(input())
            total += score
        average = float(total / 3)
        print("Name:", name)
        print("Average: {0:.2f}".format(average))
