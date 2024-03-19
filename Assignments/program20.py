# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: March 7th, 2024
# This program counts the number of snow in an image

import matplotlib.pyplot as plt

img = input("Enter the name of image: ")
ca = plt.imread(img)
countShow = 0
t = 0.75

for i in range(ca.shape[0]):
    for j in range(ca.shape[1]):
        if (ca[i, j, 0] > t) and (ca[i, j, 1] > t) and (ca[i, j, 2] > t):
            countShow = countShow + 1

print("Snow count is ", countShow)
