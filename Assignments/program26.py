# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: March 7th, 2024
# This program plots the population fraction based on user input


import pandas as pd
import matplotlib.pyplot as plt

borough = input("Enter borough name: ")
output = input("Enter output file name: ")

pop = pd.read_csv("nycHistPop.csv", skiprows=5)

pop["Fraction"] = pop[borough] / pop["Total"]

pop.plot(x="Year", y="Fraction")

fig = plt.gcf()
fig.savefig(output)
