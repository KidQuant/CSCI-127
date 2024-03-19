# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: Feburary 9th, 2024
# This program makes a weird shape, per instructions of the pseudo code

import turtle  # Imports the turtle module

wn = turtle.Screen()  # assigns the 'Screen' method to variable

weirdS = turtle.Turtle()  # assigns the 'Turtle' method to variable 'weirdS'
weirdS.color("blue")  # using the 'color' to change the color of the lines

for i in range(36):  # loops through numbers from 0 to 36
    weirdS.forward(100)  # 'weirdS' moves forward by 100 units
    weirdS.left(145)  # 'weirdS' turns left 145 degrees
    weirdS.forward(10)  # 'weirdS' moves forward 10 units
    weirdS.right(90)  # 'WeirdS' turns right 90 degrees
    weirdS.forward(10)
    weirdS.left(135)  # weirdS turns left 135 degrees
    weirdS.forward(100)

wn.exitonclick()  # exits the screen on click

