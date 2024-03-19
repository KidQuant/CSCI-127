# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: Feburary 29th, 2024
# This program creates 50 strips of both purple and yellow colors.

import matplotlib.pyplot as plt
import numpy as np

output = input("Enter outfile file: ")
num = int(input("Enter the size: "))

img = np.zeros((num, num, 3))

for i in range(0, num):
    if i % 2 == 0:
        color = np.array([255, 0, 255])
    else:
        color = np.array([255, 255, 0])

    for x in range(0, num):
        img[i, x, :] = color

plt.imsave(output, img.astype('uint8'))
