# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: March 7th, 2024
# The program uses strings to control the direction of a turtle

import turtle

commands = input("Please enter a command string: ")

wn = turtle.Screen()
andre = turtle.Turtle()


for ch in commands:
    if ch == "F":
        andre.forward(50)
    elif ch == "L":
        andre.left(90)
    elif ch == "R":
        andre.right(90)
    elif ch == "^":
        andre.penup()
    elif ch == "v":
        andre.pendown()
    elif ch == "B":
        andre.backward(50)
    elif ch == "S":
        andre.stamp()
    elif ch == "l":
        andre.left(45)
    elif ch == "r":
        andre.right(45)
    elif ch == "p":
        andre.color("purple")
    else:
        print("Error: do not know the command", ch)


print("See graphics window for your image")
wn.exitonclick()
