# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: Feburary 20th, 2024
# This program makes something that looks like a blue ballon.

import turtle

turtle.colormode(255)
andre = turtle.Turtle()
andre.shape('turtle')
andre.backward(100)

for i in range(0, 255, 10):
    andre.forward(10)
    andre.pensize(i)
    andre.color(0,0,i)
