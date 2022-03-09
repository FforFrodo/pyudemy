# Write a Python program that calculates the distance between two 3D points.
# The points are represented by two lists with three elements.
# The first element is the x-coordinate. 
# The second element is the y-coordinate. 
# The third element is the z-coordinate.
# The value of the distance must always be positive.

# pointA    [1,2,3]     [3,4,5]     [-3,4,-5]
# pointB    [1,2,3]     [1,3,5]     [2,0,-4]
# Output        0       2.23607     6.48074

# Option 1 - raw python without modules
# We need 2 lists with the 3 co-ordinates, subtract each (x - x) then Square each result
# Do same for each cor-ordinate and add each together and square root the result
# **2 is power of 2
# ** (1/2) square by 1/2 is square root

# pointA = [3,4,5]
# pointB = [1,3,5]

# distance = ((pointA[0] - pointB[0]) **2 +
#             (pointA[1] - pointB[1]) **2 +
#             (pointA[2] - pointB[2]) **2) **(1/2)

# print(distance)

# Option 2 - Math function
# We still find each distance/difference between x,y,x, square them and add together,
#then square root like before, but here we use math.sqrt() to square root

import math

pointA = [3,4,5]
pointB = [1,3,5]

addition = ((pointA[0] - pointB[0]) **2 +
             (pointA[1] - pointB[1]) **2 +
             (pointA[2] - pointB[2]) **2)

distance = math.sqrt(addition)

print(distance)