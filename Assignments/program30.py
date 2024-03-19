import pandas as pd
import matplotlib.pyplot as plt

inputFile = input("Enter name of input file: ")
outputFile = input("Enter name of output file: ")

homeless = pd.read_csv(inputFile)
homeless['Fraction'] = homeless['Total Children in Shelter'] / homeless['Total Individuals in Shelter']
homeless.plot(x = "Date of Census", y = "Fraction")

plt.savefig(outputFile)