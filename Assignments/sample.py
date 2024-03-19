# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: March 9th, 2024
# Takes elevation data of NYC and display using the default color map

# Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt

# Read in the data to an array, called elevations:
elevations = np.loadtxt("elevationsNYC.txt")

# Take the shape (dimensions) of the elevations
# and add another dimensions to hold the 3 color channels:

mapShape = elevations.shape + (3,)

# Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row, col] <= 0:
            # Below sea level
            floodMap[row, col] = 1.0

        elif elevations[row, col] <= 6:
            # Below the storm surge of Hurricane Sandy (flooding likely)
            floodMap[row, col, 0] = 1.0
        else:
            # Above the 6 foot storm surge and didn't flood
            floodMap[row, col, 1] = 1.0

# Load the flood map image into matplotlib.pyplot
plt.imshow(floodMap)

# Display the plot
plt.show()

# Save the image:
plt.imsave("floodMap.png", floodMap)
