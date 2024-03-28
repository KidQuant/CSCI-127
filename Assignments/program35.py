# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: March 28th, 2024
# This program counts which cars got the most parking tickets

import pandas as pd

csvFile = input("Enter file name: ")
attribute = input("Enter attribute: ")

df = pd.read_csv(csvFile)

print("The 10 worst offenders are:")
print(df[attribute].value_counts()[:10])
