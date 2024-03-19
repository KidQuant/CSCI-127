# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: Feburary 20th, 2024
# This program changes the color of the turtle from any Hex Code

import turtle

hex_code = input('Enter a hex string: ')

wn = turtle.Screen()
andre = turtle.Turtle()

andre.color(hex_code)
andre.shape('turtle')

wn.exitonclick()






