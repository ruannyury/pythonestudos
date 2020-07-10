import turtle
import math
import random

fred = turtle.Turtle()
fred.up()

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)

numdarts = 10
for i in range(numdarts):
    randx = random.random()
    randy = random.random()

    x = -1000
    y = 1000

wn.exitonclick()