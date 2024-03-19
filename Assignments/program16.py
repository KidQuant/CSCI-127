#Name: Andre Sealy
#Email: andre.sealy72@myhunter.cuny.edu
#Date: Feburary 28th, 2024
#The program makes a pyramid from a string.

message = input("Enter string: ")

for i in range(len(message)):
    print(message[:i])

for j in range(len(message)):
    print(message[j:])

print("Thank you for using my program!")
