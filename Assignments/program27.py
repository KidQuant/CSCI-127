# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: March 7th, 2024
# This program prints the average and maximum populatio in a borough

import pandas as pd

pop = pd.read_csv("nycHistPop.csv", skiprows=5)

borough = input("Enter borough: ")

average = pop[borough].mean()
max = pop[borough].max()

print("Average population: ", average)
print("Maximum population: ", max)
