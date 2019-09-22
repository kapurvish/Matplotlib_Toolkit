# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 21:02:44 2018

@author: Vishal Kapur
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as nm

#The color is used to represent the color of the line, here it is red
plt.plot([2,4,5,6],[4,16,25,36],color='red')

"""
#Here, 'X' is the label on X axis and 'X*X' is the label on the Y axis,
#we have specified the font color and size
plt.xlabel('X',fontsize=15,color='green')
plt.ylabel('X*X',fontsize=15,color='green')



#Here only one list is passed, it is assumed that are the Y coordinates.
#X coordinates are set to index of each Y coordinate.
plt.plot([1,5,7,8,9])



#Here we are defining the x and y axis tick parameters.
#Specify the color of the tick, label color of the tick and labesize as well
#In the x tick parameter, we have used the bottom and labelbottom as False, so that nothing
#is displayed for x tick.
x_data = nm.linspace(start=0,stop=20,num=30)
plt.plot(x_data,nm.sin(x_data),label='sine curve')
#plt.tick_params(axis='x',bottom=False,labelbottom=False)
plt.tick_params(axis='y',color='red',labelcolor='blue',labelsize='xx-large')
#Here we get the legend for the figure.It will pick the label assiciated with the plot function
plt.legend()
plt.title('Plot Expereince')

#x axis limit
plt.xlim(1,5)
#y axis limit
plt.ylim(-1,.5)
#We can swap the Xlim, to ge the mirror image of the plot. plt.xlim(5,1)
#Same is with the y axis as well.



x_data = nm.linspace(start=0,stop=20,num=30)
#Here we are specifying two plots, one for sine and other for the cos.
#linestyle=':' for dotted, for linestyle='--' line is dashed, marker= 'd', use the diamond share marker
#linsestyle='None' will leave only the dots..
plt.plot(x_data,nm.sin(x_data),label='sine curve',color = 'green',linestyle=':', marker= 'd',markersize='10')
plt.plot(x_data,nm.cos(x_data),label='cos curve',color = 'm')
plt.legend()


fig=plt.figure()
"""














