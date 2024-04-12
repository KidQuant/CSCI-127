# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: April 12th, 2024
# This program begs for a nonempty string


def main():
    test = input("Enter a non-empty string: ")
    if len(test) == 0:
        print("That was empty. Try again.")
        main()
    else:
        print("You entered: {}".format(test))


if __name__ == "__main__":
    main()
