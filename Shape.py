#creates a simple shape

#import libraries which will be utilized
import turtle

#name the turtle (to be called on later)
myshape = turtle.Turtle()

#code to be run
for i in range(150):        #code repeats 150 times
    myshape.forward(75)     #turtle will move forward 75 steps each time code runs
    myshape.right(89)       #turtle will turn right at an 89 degree angle every time code runs
