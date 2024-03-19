# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: Feburary 20th, 2024
# This code creates a hexagon with cornflowerblue shaped turtles

import turtle

wn = turtle.Screen()
andre = turtle.Turtle()

andre.color('#6495ED')
andre.shape('turtle')

for i in range(5):
    andre.forward(100)
    andre.stamp()
    andre.left(72)

wn.exitonclick()


