"""
    Code from somewhere.
"""


def demonstrate_while():
    """
        Demonstrates while statements.
    """

    total_quizzes = 5
    quiz_num = 1
    total = 0
    while quiz_num <= total_quizzes:
        total += float(input("Enter your quiz score for quiz number " + str(quiz_num) + ": "))
        quiz_num += 1
    average = total / total_quizzes
    print("Quiz average:", average)
