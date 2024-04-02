# Intro Programming Lab: A propgram with a herd of turtles

import turtle


def welcomeMessage():
    print()
    print("Welcome to our herd of turtles demonstration!")
    print()
    return


def getInput():
    n = eval(input("Please enter number of turtles: "))
    return n


def setUpScreen():
    w = turtle.Screen()
    w.bgcolor()
    return w


def setUpTurtles(n):
    tList = []
    for i in range(n):
        t = turtle.Turtle()
        t.shape("turtle")
        tList.append(t)

    for i in range(n):
        tList[i].color(0, 0, i / (2 * n) + 0.5)
        tList[i].right(i * 360 / n)

    return tList


def moveForward(tList):
    for t in tList:
        t.forward(30)


def stamp(tList):
    for t in tList:
        t.stamp()


def main():
    welcomeMessage()
    numTurtles = getInput()
    w = setUpScreen()
    turtleList = setUpTurtles(numTurtles)
    for i in range(10):
        moveForward(turtleList)
        stamp(turtleList)


if __name__ == "__main__":
    main()
