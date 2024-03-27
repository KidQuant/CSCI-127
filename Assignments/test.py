def num2string(num):
    numString = ""
    numList = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    number = numList[num]

    numString = numString + number

    print(numString)
    return numString


num2string(9)
