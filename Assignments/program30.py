# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: March 20th, 2024

import matplotlib.pyplot as plt
import pandas as pd

inputFile = input("Enter name of input file: ")
outputFile = input("Enter name of output file: ")

homeless = pd.read_csv(inputFile)

homeless["Fraction Children"] = (
    homeless["Total Children in Shelter"] / homeless["Total Individuals in Shelter"]
)
homeless.plot(x="Date of Census", y="Fraction Children")

fig = plt.gcf()
fig.savefig(outputFile)
