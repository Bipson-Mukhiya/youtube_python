# Problem: Create a function that returns both the area and circumference of a circle given its radius.


# pi r^2 
# 2 pi r

import math
def circle_stats(radius):
    area =  math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area , circumference


Area, Circumference = circle_stats(14)
print(Area)
print(Circumference)