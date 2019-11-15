"""
    Code from POGIL 12.
"""


import math


def calculate_area(radius):
    """
    Calculates the area.
    :param radius: The radius.
    """
    area = math.pi * radius ** 2
    print(format(area, ".2f"))


def calculate_diameter(radius):
    """
    Calculates the diameter.
    :param radius:  The radius.
    """
    diameter = radius + radius
    print(format(diameter, ".2f"))
