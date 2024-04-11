# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: April 11th, 2024
# Fixing the errors of the program


def convert(s):
    """
    Takes a hex string as input. Returns decimal equivalent.
    """

    total = 0

    for c in s:
        total = total * 16
        ascii = ord("c")
        if (ord("0") <= ascii) and (ascii <= ord("9")):
            total = total + ascii - ord("0")
        elif (ord("A") <= ascii) and (ascii <= ord("F")):
            total = total + ascii - ord("A") + 10
        elif (ord("a") <= ascii) and (ascii <= ord("f")):
            total = total + ascii - ord("a") + 10
        else:
            return -1

    return total


def main():
    hexString = input("Enter a number in hex: ")
    print("The number in decimal is", convert(hexString))


if __name__ == "__main__":
    main()
