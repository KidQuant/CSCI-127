# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: April 8th, 2024
# Writes a nested Triangle

import turtle


def setUp(t, dist, col):
    """
    Takes three parameters, a turtle, t, the distance, dist,
    to move the turtle and a color, col, to set the turtle's color.
    """
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)


def triangle(t, length):
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
        triangle(t, length / 2)


def nestedTriangle(t, length):
    if length > 10:
        for j in range(3):
            t.forward(length)
            t.left(120)
            triangle(t, length / 2)


def main():
    n = int(input("Enter length: "))

    tom = turtle.Turtle()
    setUp(tom, -100, "darkgreen")
    triangle(tom, n)

    tess = turtle.Turtle()
    setUp(tess, 100, "steelblue")
    nestedTriangle(tess, n)


if __name__ == "__main__":
    main()
