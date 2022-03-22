# -*- coding: utf-8 -*-
"""
This is a program to make an excel and pdf to inventory the column connections of a steel structure.
The excel sheet lists each leg corresponding to 4 clip angle connections as a row item.
This information is useful to define the number of bolts on each clip angle leg.   
The resulting Excel file is difficult to use in the field 
So this file also saves a figure which displays a simple graphic for each clip angle connection
The figure is divided into three subplots which correspond to three section cuts 
The figure is saved as a pdf to be used in the field.
The printed figure saves the inspector time sketching and reduces transcription errors.

The inspector sent the markup to a CADD operator who defined each connection in Revit.
This format allowed multiple engineers to describe complex connections without sketching.
I found the process to be a far more efficient use of CADD resources, with assistant engineers providing neat data-rich markups quickly.

Improvements needed include:
    -Streamline defining the figure and marker size
    -Use the node_labels DataFrame instead of the connections DataFrame to define the text annotations
        the annotations seem to plot one higher than they should
        ideally, the node_labels DataFrame would be replaced by a filtered connections DataFrame
    -redefine all of the steps as functions
    -add user input prompts
    -directly print the pdf
"""

#import some libraries
import pandas as pd #https://pandas.pydata.org/docs/user_guide/index.html#user-guide
import matplotlib.pyplot as plt #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
import string
import numpy as np

#make base lists of sufficient length to define all of your parameters
#where nums and letters correspond to the number of gridlines in the x and y directions
gridlines_x = 110
gridlines_y = 11
nums= list(range(1,gridlines_x+1)) #the range function is not inclusive of the last number given so 1 is added to gridlines_x 
#nums = nums[::-1] #uncomment this line to reverse the order of the gridlines in the x direction
letters= list(string.ascii_uppercase)[0:gridlines_y]
#letters = letters[::-1] #uncomment this line to reverse the order of the gridlines in the y direction
corner= ['NE', 'SE', 'SW', 'NW']
direction = ['N', 'S', 'E', 'W']
#make a list of all possible grid nodes
letter_lst=[]
num_lst=[]
corner_lst=[]
direction_lst=[]
by_lst = []
for j in letters:
    for i in nums:
        for k in corner:
            for l in direction:
                if l in k:
                    letter_lst.append(str(j))
                    num_lst.append(str(i))
                    corner_lst.append(str(k))
                    direction_lst.append(str(l))
                    by_lst.append(str(j) + str(i) + str(k)+ str(l))
                    #for each item inside each list, append a string consisting
                    #of the concatenated str of each item

#make a df of all the possible grid nodes
#the lists made in the previous for loop are each zipped together then converted to a list which is read as the data to fill the DataFrame 
#Each list is considered as a column which are all named as part of the .DataFrame() method column argument
connections = pd.DataFrame(list(zip(letter_lst, num_lst, corner_lst, direction_lst, by_lst)), columns=['letter', 'num', 'corner', 'direction', 'bylst'])

#write the DataFrame to excel
with pd.ExcelWriter(r"\\ennyccifs01\disciplines\STR\Structures\Structures Library\Scripts\WIP\Python\Connection Schedule.xlsx") as writer:
    connections.to_excel(writer,sheet_name='Connections')
#read the excel to make sure there were no errors
pd.read_excel(r"\\ennyccifs01\disciplines\STR\Structures\Structures Library\Scripts\WIP\Python\Connection Schedule.xlsx")

#now, two data frames describe every node in an array of columns
#the rest of the code will define a figure of three subplots to display graphics used here to describe the possible clip angle connections from three prospectives
fig, ax = plt.subplots(1, 3, sharex=True, sharey=False)
plt.subplots_adjust(wspace=0.05, hspace=0)
for a in ax:
    a.set_aspect(17/11)
fig.set_size_inches(33, 17)

#Next, we plot a bit of text at each of our nodes. The text will be the name of that node
#Here the .DataFrame() method takes in a list using two for loops acting on our two lists of gridline 
node_labels = pd.DataFrame([(i, j) for i in letters for j in nums], columns=['letter', 'num'])
#The following section uses the .apply() method from pandas.
#A function is applied to every row or column of a DataFrame.
#Inside the .apply() method there is a lambda function
#Lambda functions are similar to a for loop in which the row variable is passed into the .text() method 
#The .text method is reading the row variable, defined here as a particular row of the DataFrame
connections[['letter','num','letter']].apply(   lambda row: ax[0].text(*row, ha='left', va = 'center', fontsize = 8),axis=1)
connections[['letter','num','num']].apply(      lambda row: ax[0].text(*row, ha='right', va = 'center', fontsize = 8),axis=1)
#connections[['letter','num','letter']].apply(   lambda row: ax[1].text(*row, ha='left', va = 'center', fontsize = 8),axis=1)
#connections[['letter','num','num']].apply(      lambda row: ax[1].text(*row, ha='right', va = 'center', fontsize = 8),axis=1)
#connections[['letter','num','letter']].apply(   lambda row: ax[2].text(*row, ha='left', va = 'center', fontsize = 8),axis=1)
#connections[['letter','num','num']].apply(      lambda row: ax[2].text(*row, ha='right', va = 'center', fontsize = 8),axis=1)

#I don't know why using the node_labels DataFrame is skipping a row, so the connections DataFrame is used instead.
#The labels are commented out because they loop through every row of the DataFrame which introduces a few seconds of latency  
#node_labels[['letter','num','num']].apply(     lambda row: ax[0].text(*row, ha = 'right', va = 'center', fontsize = 8),axis=1)
#node_labels[['letter','num','num']].apply(      lambda row: ax[0].text(*row, ha='right', va = 'center', fontsize = 8),axis=1)
#node_labels[['letter','num','letter']].apply(   lambda row: ax[1].text(*row, ha='left', va = 'center', fontsize = 8),axis=1)
#node_labels[['letter','num','num']].apply(      lambda row: ax[1].text(*row, ha='right', va = 'center', fontsize = 8),axis=1)
#node_labels[['letter','num','letter']].apply(   lambda row: ax[2].text(*row, ha='left', va = 'center', fontsize = 8),axis=1)
#node_labels[['letter','num','num']].apply(      lambda row: ax[2].text(*row, ha='right', va = 'center', fontsize = 8),axis=1)

#Below is an option to reverse the label for the x axis for grid lines that are numbered West to East
#Renaming the .xticks is incompatible with the .text() labels applied at each node
#Instead, the commented out lines to redefine nums and letters should be used 
#plt.xticks(range(len(letters)), letters[::-1]) #this method could be used to name the after any list

#Now, there are three labeled plots and we want to add graphics to each
#Scatter plots have the option to make markers from data points presented as a list of x and y coordinates 
#Clip angles look like...angles which are simple to draw from three numbers listed in the correct order
#Here, it is defined using lst_1 and lst_2 those define the extents of an angle shape

a = 2
b = 2
c = b*3
lst_1 = [a,c,c,b,b,a,a]
lst_2 = lst_1[::-1]
#lst_1 and lst_2 define the x and y coordinates which can be multiplied by -1 to flip and have a space added to repeat and move the angle shaped marker
#The following lists are each making a list of points which can be interpreted as a 2D shape by zipping together lst_1 and lst_2
#The result is unique markers for each node in the scatter plot
space = 6
lst_A = [list(x) for x in zip([(1*(x+space))    for x in lst_1], [(1*(x+0))         for x in lst_2])]
lst_B = [list(x) for x in zip([(-1*(x+space))   for x in lst_1], [(1*(x+0))         for x in lst_2])]
lst_C = [list(x) for x in zip([(1*(x+space))    for x in lst_1], [(-1*(x+0))        for x in lst_2])]
lst_D = [list(x) for x in zip([(-1*(x+space))   for x in lst_1], [(-1*(x+0))        for x in lst_2])]
lst_E = [list(x) for x in zip([(1*(x+0))        for x in lst_1], [(1*(x+space))     for x in lst_2])]
lst_F = [list(x) for x in zip([(-1*(x+0))       for x in lst_1], [(1*(x+space))     for x in lst_2])]
lst_G = [list(x) for x in zip([(1*(x+0))        for x in lst_1], [(-1*(x+space))    for x in lst_2])]
lst_H = [list(x) for x in zip([(-1*(x+0))       for x in lst_1], [(-1*(x+space))    for x in lst_2])]
lst_I = [list(x) for x in zip([(1*(x+space))    for x in lst_1], [(1*(x+space))     for x in lst_2])]
lst_J = [list(x) for x in zip([(-1*(x+space))   for x in lst_1], [(1*(x+space))     for x in lst_2])]
lst_K = [list(x) for x in zip([(1*(x+space))    for x in lst_1], [(-1*(x+space))    for x in lst_2])]
lst_L = [list(x) for x in zip([(-1*(x+space))   for x in lst_1], [(-1*(x+space))    for x in lst_2])]
lst_M = [list(x) for x in zip([(1*(x+0))        for x in lst_1], [(1*(x+0))         for x in lst_2])]
lst_N = [list(x) for x in zip([(-1*(x+0))       for x in lst_1], [(1*(x+0))         for x in lst_2])]
lst_O = [list(x) for x in zip([(1*(x+0))        for x in lst_1], [(-1*(x+0))        for x in lst_2])]
lst_P = [list(x) for x in zip([(-1*(x+0))       for x in lst_1], [(-1*(x+0))        for x in lst_2])]

#Set the size and layer scatter plots of each list on to their respective axis or ax[]
#The .scatter() method reads the column called letter and num in the connections DataFrame to plot markers on each subplot 
size = 1500

ax[0].scatter(connections['letter'],connections['num'], s=size, marker=lst_A, c='0') #c='0' defines the marker to be colored black
ax[0].scatter(connections['letter'],connections['num'], s=size, marker=lst_B, c='0')
ax[0].scatter(connections['letter'],connections['num'], s=size, marker=lst_C, c='0')
ax[0].scatter(connections['letter'],connections['num'], s=size, marker=lst_D, c='0')
ax[0].scatter(connections['letter'],connections['num'], s=size, marker=lst_E, c='0')
ax[0].scatter(connections['letter'],connections['num'], s=size, marker=lst_F, c='0')
ax[0].scatter(connections['letter'],connections['num'], s=size, marker=lst_G, c='0')
ax[0].scatter(connections['letter'],connections['num'], s=size, marker=lst_H, c='0')
ax[0].set_title("Plan view") #each subplot is named using the .set_title() method
#similar methods are available in the matplotlib library to define chart features

ax[1].scatter(connections['letter'],connections['num'], s=size, marker=lst_I, c='0')
ax[1].scatter(connections['letter'],connections['num'], s=size, marker=lst_J, c='0')
ax[1].scatter(connections['letter'],connections['num'], s=size, marker=lst_K, c='0')
ax[1].scatter(connections['letter'],connections['num'], s=size, marker=lst_L, c='0')
ax[1].set_title("North South Elevations")

ax[2].scatter(connections['letter'],connections['num'], s=size, marker=lst_M, c='0')
ax[2].scatter(connections['letter'],connections['num'], s=size, marker=lst_N, c='0')
ax[2].scatter(connections['letter'],connections['num'], s=size, marker=lst_O, c='0')
ax[2].scatter(connections['letter'],connections['num'], s=size, marker=lst_P, c='0')
ax[2].set_title("East West Elevations")

#finally the figure is saved in the same folder as this .py file
plt.savefig(r"\\ennyccifs01\disciplines\STR\Structures\Structures Library\Scripts\WIP\Python\Clip angle connection figures.pdf", dpi=600, transparent=True) #figure can be saved as .png as well
plt.show() #the figure will be shown in the console depending on the editor used

