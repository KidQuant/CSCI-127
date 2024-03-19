#Name: Andre Sealy
#Email: andre.sealy72@myhunter.cuny.edu
#Date: Feburary 28th, 2024
# This program takes 5 integers and uses those integers for turtle commands

import turtle

turtleCommands = 0

commands = []

while turtleCommands < 5:
    
    commands.append(int(input("Enter a number: ")))

    turtleCommands += 1

wn = turtle.Screen()
andreS = turtle.Turtle()

for i in commands:
    andreS.left(i)
    andreS.forward(100)

wn.exitonclick()
