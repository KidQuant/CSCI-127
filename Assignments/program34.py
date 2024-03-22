# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: March 21th, 2024
# This program tells you the time of the day

time = int(input("Enter hour (in 24 hour time): "))

hour = time % 24

if hour < 12:
    print("Good Morning")
elif (hour < 17) and (hour > 12):
    print("Good Afternoon")
else:
    print("Good evening")
