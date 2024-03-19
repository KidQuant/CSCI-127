# Name: Andre sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: February 2, 2024
# This program draws an octagon using the turtle module

import turtle               # imports the turtle package
wn = turtle.Screen()        # creates a new screen to draw the octagon and assigns to variable 'wn'

andreS = turtle.Turtle()    # creates an instance of the Turtle class and assigns it to the variable 'andreS'
andreS.color("blue")        # uses the color method to change the color of the line blue
andreS.shape("turtle")      # uses the shape method to change the change of the turtle

for i in range(8):          # loops through a list of numbers from 0 to 8, not including 8
    andreS.forward(60)      # makes andre draw an octagon
    andreS.stamp()
    andreS.left (360/8)     # turns andre 45 degrees

wn.exitonclick()            # exits the program on click
