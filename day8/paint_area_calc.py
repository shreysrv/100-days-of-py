import math


def cans_needed(height, width):
    wall_area = height * width
    return math.ceil(wall_area / 5)


height = int(input("enter Height of the wall"))
weight = int(input("enter weight of the wall"))
print(f"Total Cans needed:{cans_needed(height, weight)}")
