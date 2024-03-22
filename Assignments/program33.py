# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: March 21th, 2024
# This program reorgranizes the names in a list()

nameList = input("Please enter your list of names: ")
splitList = nameList.split("; ")
print("")

print("You entered:")
print("")

for i in splitList:
    name = i.split(", ")
    print("{} {}".format(name[1], name[0]))

print("")
print("Thank you for using name organizer!")
