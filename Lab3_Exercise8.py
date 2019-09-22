#Program that will compute the area of a circle
#Formula for area of circle is: A = Pi * r ** 2
#Let area of circle be A and r be radius
#Where Pi is 3.142 but we will be importing Pi in Python3

import math
radius = float(input("Enter the radius of the cirlce"))
Area = math.pi * (radius ** 2)
print("Dear user, the radius of your circle is", Area)
