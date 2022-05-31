"""
Author: Amin Fahiminia
Purpose: computes whether a line segment will intersect with a circle. Lines segments are represented by two 2D coordinates.
Circles are represented by a center coordinate and a radius.
Formula for distance of line given by two points retrieved from: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
"""

import math

# Input for line (parameters: x1, y1, x2, y2 )
x1_Input = int(input("Please input the x-coordinate for the first point of the line." ))
y1_Input = int(input("Please input the y-coordinate for the first point of the line." ))

x2_Input = int(input("Please input the x-coordinate for the second point of the line." ))
y2_Input = int(input("Please input the y-coordinate for the second point of the line." ))

#Input for Circle: (parameters: x3,y3, r)
x3_Input = int(input("Please input the x-coordinate for center of the circle." ))
y3_Input = int(input("Please input the y-coordinate for center of the circle." ))
r_Input = int(input("Please input the radius of the circle."))

def IntersectCheck(x1, y1, x2, y2, x3, y3, r):

    # Formula taken from above link
    d = abs((x2 - x1)(y1 - y3) - (x1 - x3)(y2 - y1)) / math.sqrt((x2 - x1)^2 + (y2 - y1)^2)

    if r > d:
        print(2)
    if r == d:
        print(1)
    else:
        print(0)

print(IntersectCheck(x1_Input, y1_Input, x2_Input, y2_Input, x3_Input, y3_Input, r_Input))
        

