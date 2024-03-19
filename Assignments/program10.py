# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: Feburary 16th, 2024
# This program creates another weird shape

import turtle

wn = turtle.Screen()            # instantiates the Sreen method to variable wn
weirdS = turtle.Turtle()        

for i in range(5, 305, 5):      # loops through a list of integers from 5 to 300 incrementing by 5
    weirdS.forward(i)           # move forward by i units
    weirdS.left(91)             # turn left 91 degrees

wn.exitonclick()               # exit on click 
