#snow count

#import libraries which will be used
import numpy as py
import matplotlib.pyplot as plt

#reads the image
ca = plt.imread(input())          

#will keep track of the number of white pixels
countSnow = 0                     

#almost white pixels are also counted
t = 0.75                        

#code will repeat for every pixel, reagrdless of color
for i in range(ca.shape[0]):
  for j in range(ca.shape[1]):
    #checks to see if colors are > 0.75:
    if (ca[i,j,0] >t) and (ca[i,j,1]>t) and (ca[i,j,2] >t):
      countSnow = countSnow + 1

print("Snow count is", countSnow)
