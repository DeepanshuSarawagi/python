# Day 8 - Exercise 1 - PaintAreaCalculator
# We are going to determine the no. of cans of paint needed to paint the wall of certain height and width

import math
height = int(input("Enter the height of the wall: "))
width = int(input("Enter the width of the wall: "))
coverage = 5


def paint_calc(height, width, coverage):
    no_of_cans = math.ceil((height * width) / coverage)
    print("You will need {} cans to paint the wall of {} meters in height and {} meters in width"
          .format(no_of_cans, height, width))

paint_calc(height=height, width=width, coverage=coverage)
