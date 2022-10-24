# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 13:27:39 2021
Adding here new information here
@author: USDF659971
"""

import pandas as pd #https://pandas.pydata.org/docs/user_guide/index.html#user-guide\n",
from pandas import *
import numpy as np #https://numpy.org/doc/stable/user/whatisnumpy.html\n",
import matplotlib #https://matplotlib.org/stable/users/index.html\n",
import matplotlib.pyplot as plt #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html\n",
import random
import string
import csv
randn = np.random.randn


raw_df =  pd.read_excel(r"C:\Users\usdf659971\UDEMY\Complete-Python-3-Bootcamp-master\Challenges\RK-20_Main Cable Compaction measurement log.xlsx")

raw_df.rename(columns = {'Unnamed: 0': 'PP'}, inplace = True)
raw_df= raw_df.drop([0])
pp_hold = raw_df['PP']
raw_df= raw_df.iloc[0:,1:]/(np.pi)
raw_df.insert(0, 'PP', pp_hold)

wrap_thickness = 0.135
nom_dia = 0.196
additional_thickness = (wrap_thickness +nom_dia)*2

stats_r = pd.DataFrame()
#stats_r.set_index(raw_df['PP'],inplace=True)
stats_r['minimum']      =raw_df.iloc[0:,1:].min(axis=1)
stats_r.set_index(raw_df['PP'],inplace=True) #na error begins here and continues for stats_r data frame
stats_r['maximum']      =(raw_df.iloc[0:,1:].max(axis=1))
stats_r['delta']        =stats_r['maximum']-stats_r['minimum']
stats_r['average']      =raw_df.iloc[0:,1:].mean(axis=1)
stats_r['legup']      =stats_r['maximum']-stats_r['average']
stats_r['legdown']    =stats_r['minimum']-stats_r['average']

stats_c = pd.DataFrame()

stats_c['minimum']      =raw_df.iloc[0:,1:].min() 
stats_c['maximum']      =raw_df.iloc[0:,1:].max()
stats_c['delta']        =stats_c['maximum']-stats_c['minimum']
stats_c['average']      =raw_df.iloc[0:,1:].mean()
stats_c['legup']      =stats_c['maximum']-stats_c['average']
stats_c['legdown']    =stats_c['minimum']-stats_c['average']

max_dia = additional_thickness+max(max(stats_c['maximum']),max(stats_r['maximum']))
min_dia = additional_thickness+min(min(stats_c['minimum']),min(stats_r['minimum']))
delta_dia = max_dia-min_dia


fig, (ax1, ax2) = plt.subplots(1,2, sharey=True)
lst= [1,2,3,4,5,6,7,8,9] 
ax1.errorbar(lst , stats_r['average'], stats_r['delta']/2, color='C2')
ax1.scatter(raw_df.iloc[0:,1:], lst, color='C3')
lst2 = [0, 5, 10, 15, 20, 25, 30]
ax2.errorbar(lst2 , stats_c['average'], stats_c['delta']/2, color='C1')


#vert_beams_df = pd.DataFrame(all_values)\n",
#"vert_beams_df.to_excel(\"C:\\\\Users\\\\usdf659971\\\\Documents\\\\Rochdale Element Schedule.xlsx\", sheet_name =\"Vert Beams\", index=False)\n",

#below is the color table sample code from https://stackoverflow.com/questions/11623056/matplotlib-using-a-colormap-to-color-table-cell-background

#idx = Index(np.arange(1,11))
#df = DataFrame(randn(10, 5), index=idx, columns=['A', 'B', 'C', 'D', 'E'])
#vals = np.around(df.values,2)
#norm = plt.Normalize(vals.min()-1, vals.max()+1)
#colours = plt.cm.hot(normal(vals))

#fig = plt.figure(figsize=(15,8))
#ax = fig.add_subplot(111, frameon=True, xticks=[], yticks=[])

#the_table=plt.table(cellText=vals, rowLabels=df.index, colLabels=df.columns, 
#                    colWidths = [0.03]*vals.shape[1], loc='center', 
#                    cellColours=colours)
#plt.show()

