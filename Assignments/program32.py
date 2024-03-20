# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: March 18th, 2024
# This program zooms in on an section of the image

import matplotlib.pyplot as plt

inputFile = input("Enter image file name: ")
outputFile = input("Enter output file: ")

img = plt.imread(inputFile)


height = img.shape[0]
width = img.shape[1]

img2 = img[height // 2 :, : width // 2]

plt.imsave(outputFile, img2)
