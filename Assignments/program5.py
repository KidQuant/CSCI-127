# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: Feburary 9th, 2024
# This program makes a star


import turtle               # imports the turtle module
wn = turtle.Screen()        # assigns the screen method class to variable 'wn'

starS = turtle.Turtle()     # assigns the turtle class to the variable 'starS'
starS.color('blue')         # uses the color method to changge the color of the line

for i in range(5):          # loops through the numbers 0 to 4
    starS.forward(200)      # moves the turtle 100 units forward
    starS.right(144)        # turns the turtle 144 degrees

wn.exitonclick()            # exits the program on click of the window
