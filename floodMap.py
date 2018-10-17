#flood map
#this program assumes that you have file 'elevationsNYC.txt' on your computer

#import libraries which will be used 
import numpy as np
import matplotlib.pyplot as plt

#reads the information on the file, and puts it onto an array, "elevations"
elevations = np.loadtxt("elevationsNYC.txt")

#this loads the array into plt
plt.imshow(elevations)

#determines the color of the pixel based on the elevation
if elevations[row,col] > 6:
    #colors the pixel gray
    elevations[row,col,0] = 0.5
    elevations[row,col,1] = 0.5
    elevations[row,col,2] = 0.5
elif elevations[row, col] <= 20:
    #colors the pixel gray
    elevations[row,col,0] = 0.5
    elevations[row,col,1] = 0.5
    elevations[row,col,2] = 0.5
else:
    #colors the piexel green
    elevations[row,col,1] = 1.0

#shows the plot
plt.show()
