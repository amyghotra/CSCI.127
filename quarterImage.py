#quarter image
#this code will output the lower left corner of an image

#import libs
import matplotlib.pyplot as plt
import numpy as np

#ask user for file to be edited
img1 = input("Enter file name: ")

#read the file
img = plt.imread(img1)

#ask user for name of the output file
outImg = input("Output file name: ")

# .shape[0] pertains to the height 
height = img.shape[0]
# .shape[1] pertains to the width
width = img.shape[1]

#the height and width are divided by 2 and floored
#the ":" in height//2: means that the height is now everything after the halfway point of the height
# :width//2 means that everything before the halfway point of the width is shown
img2 = img[height//2:, :width//2]

plt.imsave(outImg , img2)
