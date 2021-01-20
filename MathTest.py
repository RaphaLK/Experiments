from random import uniform
from math import pi, sqrt

#Using 2 random numbers from the range of 0-1 calculate/estimate pi

def pi_estimate(n):
    x = uniform(0,1)
    y = uniform(0,1)
    distance = x**2 + y**2
    total_square = 0
    total_circle = 0
    #Formula of square area = 4r
    #Formula of circle = PI r^2
    #The ratio of the total square area/total circle area will be pi
    for i in range (n):
        if distance <= 1:
            total_circle += 1 
        total_square += 1
    pie = total_square/total_circle
    print(pie)

pi_estimate(10000)
