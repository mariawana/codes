import math
from turtle import *

def circlea(k):
    return 15*math.sin(k)**3

def circle(k):
    return 15*math.cos(k)-5*\
    math.cos(4*k)-2*\
    math.cos(4*k)-\
    math.cos(4*k)

speed(10000)
bgcolor("black")

for i in range(10000):
    goto(circlea(i)*15,circle(i)*15)
    for j in range(5):
        color("beige")
    goto(0,0)
done()