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

#Here, 'X' is the label on X axis and 'X*X' is the label on the Y axis, we have specified the font color and size
#Output plot present in plot_img.md as Figure_0
plt.xlabel('X',fontsize=15,color='green')
plt.ylabel('X*X',fontsize=15,color='green')


#Here only one list is passed, it is assumed that are the Y coordinates.
#X coordinates are set to index of each Y coordinate.
#Output plot present in plot_img.md as Figure_1
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
#Output plot present in plot_img.md as Figure_2
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
#Output plot present in plot_img.md as Figure_3


  

x = nm.linspace(start=0,stop=20,num=30)
fig=plt.figure()
#ax = fig.add_axes([0,0,1,1])
#Here the the first value '0.15', tell the very left of the figure to start
#Here the the seconnd value '0.6', tell it is postioned one of the above.,It is 0.6 unit as a whole
# Here the the third value '1', tell the enire widht of the figure 
# Here the the fourth value '4', tell the enire height of the figure 
ax1 = fig.add_axes([0.15,0.6,0.6,0.4])
ax2 = fig.add_axes([0.15,0.1,0.8,0.4])

ax1.plot(x,nm.sin(x))
ax1.set_xlabel('x',fontsize=15,color='r')
ax1.set_ylabel('sin(x)',fontsize=15,color='r')

ax2.plot(x,nm.cos(x))
ax2.set_xlabel('x',fontsize=15,color='r')
ax2.set_ylabel('cos(x)',fontsize=15,color='r')
plt.show()
#Output plot present in plot_img.md as Figure_4


x = nm.linspace(start=0,stop=20,num=30)
fig=plt.figure()
#Here ax1 sets the larger axis, span to the width and the height of the figure.
ax1 = fig.add_axes([0.1,0.1,1,1])
#ax1.plot(x,nm.sin(x))

#Here ax2 forms the smaller axis, which inset on the larger axis.
ax2 = fig.add_axes([0.5,0.5,0.4,0.4])
ax2.plot(x,nm.cos(x))
plt.show()
#Output plot present in plot_img.md as Figure_5

x = nm.linspace(start=0,stop=20,num=30)
#Here figsize=(15,7) is the height and width of the figure in inches
fig=plt.figure(figsize=(15,7))
#subplot functionality, it will set up a 2X2 grid to the overall figure.
#It will plot at the first postion in the grid. top left of the figure.
ax1 = fig.add_subplot(2,2,1)
ax1.plot(x,nm.sin(x))

ax2 = fig.add_subplot(2,2,4)
ax2.plot(x,nm.cos(x))

plt.show()
#Output plot present in plot_img.md as Figure_6



x = nm.linspace(start=0,stop=20,num=30)
#Here we pass two tuples, first indicates the matrix representation of the gird, here we have 2X3.
#Second tuple is the row and column value for this particular subplot.If we want a particular graph to to span more than
#one row or column we can use the rowspan and colspan attribute.
ax1=plt.subplot2grid((2,3),(0,0))
ax1.plot(x,nm.sin(x))
ax1.set_label('sine curve')

ax2=plt.subplot2grid((2,3),(0,1))
ax2.plot(x,nm.cos(x))
ax2.set_label('cos curve')

ax3=plt.subplot2grid((2,3),(0,2),rowspan=2)
ax3.plot(x,nm.exp2(x))
ax3.set_label('Exp Curve')


ax4=plt.subplot2grid((2,3),(1,0),colspan=2)
ax4.plot(x,nm.tan(x))
ax4.set_label('tan curve')

plt.show()



