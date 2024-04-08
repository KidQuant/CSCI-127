# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: April 8th, 2024
# List the top 3 contributing factors for collision

import pandas as pd

csvFile = input("Enter CSV file name: ")

df = pd.read_csv(csvFile)

print("Top three contributing factors for collisions:")
print(df["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])
