# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: March 18th, 2024
# This program zooms in on an section of the image

import matplotlib.pyplot as plt
import numpy as np

inF = input("Enter file name: ")

img = plt.imread(inF)

height = img.shape[0]
width = img.shape[1]

img2 = img[height // 4 :, width // 4]

plt.imsave(img2)
