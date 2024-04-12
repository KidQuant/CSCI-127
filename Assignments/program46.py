# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: April 12th, 2024
# This program randomly turns an arrow and moves it forward 10 units

import random
import turtle

andre = turtle.Turtle()

for i in range(100):
    andre.forward(10)
    a = random.randrange(0, 360, 1)
    andre.right(a)
