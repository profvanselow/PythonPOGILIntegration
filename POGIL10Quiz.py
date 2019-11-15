"""
    Quiz from POGIL 10.
"""


for student in range(3):
    name = input()
    total = 0
    for quiz in range(3):
        score = int(input())
        total += score
    average = float(total / 3)
    print("Name:", name)
    print("Average: {0:.2f}".format(average))
