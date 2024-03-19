# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: March 7th, 2024
# The program counts the fraction of words in a list ends in a constanant

nounList = input("Enter nouns: ")

splitList = nounList.split(" ")

print("Number of words: ", len(splitList))

count = 0

for i in splitList:
    if i[-1] == "s":
        count += 1

print("Fraction of your list that is plural is {}".format(count / len(splitList)))
