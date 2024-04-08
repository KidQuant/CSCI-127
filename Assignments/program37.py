# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: April 8th, 2024
# This program returns a month of the year.yield


def monthString(monthNum):
    """
    Takes as input a number, monthNum, and
    returns the corresponding month name as a string.
    Example: monthString(1) returns "January".
    Assumes that input is a integer ranging from 1 to 12.
    """

    monthString = ""

    months = [
        "January",
        "Feburary",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    monthString = months[monthNum - 1]

    return monthString


def main():
    n = int(input("Enter the number of the month: "))
    mString = monthString(n)
    print("The month is", mString)


if __name__ == "__main__":
    main()
