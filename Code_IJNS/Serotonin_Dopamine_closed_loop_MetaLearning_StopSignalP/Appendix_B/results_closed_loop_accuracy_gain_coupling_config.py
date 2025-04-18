#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federicarobertazzi
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

matrix_nocoupling= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
matrix_nocoupling.head()

matrix_coupling_upup= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
matrix_coupling_upup.head()

matrix_coupling_downup= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
matrix_coupling_downup.head()

matrix_coupling_downdown= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
matrix_coupling_downdown.head()

matrix_coupling_updown= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
matrix_coupling_updown.head()

matrix_gain_coupling_imported= pd.read_csv('<insert path>', delimiter = ';',decimal=",")
matrix_gain_coupling_imported.head()

#dataset no coupling 
mean_data_nocoupling=np.mean(matrix_nocoupling)
std_data_nocoupling=np.std(matrix_nocoupling)

#mutual upregulation
mean_data_coupling_upup=np.mean(matrix_coupling_upup)
std_data_coupling_upup=np.std(matrix_coupling_upup)
 
x = [0,1,2,3,4,5,6,7,8]

fig, ax1 = plt.subplots()
color = 'black'
ax1.set_xlabel('external input',size=17)
ax1.set_ylabel('no coupling', color = color, size=17)
ax1.plot(x, mean_data_nocoupling, color = color)
ax1.fill_between(x, mean_data_nocoupling- std_data_nocoupling/np.sqrt(7),mean_data_nocoupling+std_data_nocoupling/np.sqrt(7), color = color, alpha=0.2)
ax1.tick_params(axis ='y', labelcolor = color)
plt.xticks(x,['0','1','1.3','1.5','1.7','1.9','2','3','4'])
ax2 = ax1.twinx()
color = 'magenta'
ax2.set_ylabel('coupling up/up', color = color, size=17)
ax2.plot(x, mean_data_coupling_upup, color = color)
ax2.fill_between(x, mean_data_coupling_upup-std_data_coupling_upup/np.sqrt(7), mean_data_coupling_upup+ std_data_coupling_upup/np.sqrt(7), color = color, alpha=0.2)
ax2.tick_params(axis ='y', labelcolor = color)
plt.xlim(0,8)
plt.show()

#serotonin downregulates dopamine and dopamine upregulates serotonin
mean_data_coupling_downup=np.mean(matrix_coupling_downup)
std_data_coupling_downup=np.std(matrix_coupling_downup)

fig, ax1 = plt.subplots()
color = 'black'
ax1.set_xlabel('external input',size=17)
ax1.set_ylabel('no coupling', color = color, size=17)
ax1.plot(x, mean_data_nocoupling, color = color)
ax1.fill_between(x, mean_data_nocoupling- std_data_nocoupling/np.sqrt(7),mean_data_nocoupling+std_data_nocoupling/np.sqrt(7), color = color, alpha=0.2)
ax1.tick_params(axis ='y', labelcolor = color)
plt.xticks(x,['0','1','1.3','1.5','1.7','1.9','2','3','4'])
ax2 = ax1.twinx()
color = 'orange'
ax2.set_ylabel('coupling down/up', color = color, size=17)
ax2.plot(x, mean_data_coupling_downup, color = color)
ax2.fill_between(x, mean_data_coupling_downup-std_data_coupling_downup/np.sqrt(7),mean_data_coupling_downup+std_data_coupling_downup/np.sqrt(7), color = color, alpha=0.2)
ax2.tick_params(axis ='y', labelcolor = color)
plt.xlim(0,8)
plt.show()

#mutual downregulation
mean_data_coupling_downdown=np.mean(matrix_coupling_downdown)
std_data_coupling_downdown=np.std(matrix_coupling_downdown)

fig, ax1 = plt.subplots()
color = 'black'
ax1.set_xlabel('external input',size=17)
ax1.set_ylabel('no coupling', color = color, size=17)
ax1.plot(x, mean_data_nocoupling, color = color)
ax1.fill_between(x, mean_data_nocoupling- std_data_nocoupling/np.sqrt(7),mean_data_nocoupling+std_data_nocoupling/np.sqrt(7), color = color, alpha=0.2)
ax1.tick_params(axis ='y', labelcolor = color)
plt.xticks(x,['0','1','1.3','1.5','1.7','1.9','2','3','4'])
ax2 = ax1.twinx()
color = 'blue'
ax2.set_ylabel('coupling down/down', color = color,size=17)
ax2.plot(x,mean_data_coupling_downdown, color = color)
ax2.fill_between(x, mean_data_coupling_downdown-std_data_coupling_downdown/np.sqrt(7),mean_data_coupling_downdown+std_data_coupling_downdown/np.sqrt(7), color = color, alpha=0.2)
ax2.tick_params(axis ='y', labelcolor = color)
plt.xlim(0,8)
plt.show()

#serotonin upragulates dopamine and dopamine downregulates serotonin 
mean_data_coupling_updown=np.mean(matrix_coupling_updown)
std_data_coupling_updown=np.std(matrix_coupling_updown)

fig, ax1 = plt.subplots()
color = 'black'
ax1.set_xlabel('external input',size=17)
ax1.set_ylabel('no coupling', color = color, size=17)
ax1.plot(x, mean_data_nocoupling, color = color)
ax1.fill_between(x, mean_data_nocoupling- std_data_nocoupling/np.sqrt(7),mean_data_nocoupling+std_data_nocoupling/np.sqrt(7), color = color, alpha=0.2)
ax1.tick_params(axis ='y', labelcolor = color)
plt.xticks(x,['0','1','1.3','1.5','1.7','1.9','2','3','4'])
ax2 = ax1.twinx()
color = 'cyan'
ax2.set_ylabel('coupling up/down', color = color, size=17)
ax2.plot(x, mean_data_coupling_updown, color = color)
ax2.fill_between(x, mean_data_coupling_updown-std_data_coupling_updown/np.sqrt(7),mean_data_coupling_updown+std_data_coupling_updown/np.sqrt(7), color = color, alpha=0.2)
ax2.tick_params(axis ='y', labelcolor = color)
plt.xlim(0,8)
plt.show()

#closed-loop accuracy gain in the four coupling config
matrix_gain_coupling_upup=np.subtract(matrix_coupling_upup, matrix_nocoupling)
matrix_gain_coupling_upup=(np.divide(matrix_gain_coupling_upup,matrix_nocoupling))*100
mean_matrix_gain_coupling_upup=np.mean(matrix_gain_coupling_upup)
std_matrix_gain_coupling_upup=np.std(matrix_gain_coupling_upup)

matrix_gain_coupling_downup=np.subtract(matrix_coupling_downup, matrix_nocoupling)
matrix_gain_coupling_downup=(np.divide(matrix_gain_coupling_downup,matrix_nocoupling))*100
mean_matrix_gain_coupling_downup=np.mean(matrix_gain_coupling_downup)
std_matrix_gain_coupling_downup=np.std(matrix_gain_coupling_downup)

matrix_gain_coupling_downdown=np.subtract(matrix_coupling_downdown, matrix_nocoupling)
matrix_gain_coupling_downdown=(np.divide(matrix_gain_coupling_downdown,matrix_nocoupling))*100
mean_matrix_gain_coupling_downdown=np.mean(matrix_gain_coupling_downdown)
std_matrix_gain_coupling_downdown=np.std(matrix_gain_coupling_downdown)

matrix_gain_coupling_updown=np.subtract(matrix_coupling_updown, matrix_nocoupling)
matrix_gain_coupling_updown=(np.divide(matrix_gain_coupling_updown,matrix_nocoupling))*100
mean_matrix_gain_coupling_updown=np.mean(matrix_gain_coupling_updown)
std_matrix_gain_coupling_updown=np.std(matrix_gain_coupling_updown)

plt.figure()
plt.plot(x, mean_matrix_gain_coupling_upup, label='gain up/up', color='magenta')
plt.fill_between(x, mean_matrix_gain_coupling_upup- std_matrix_gain_coupling_upup/np.sqrt(7),mean_matrix_gain_coupling_upup+std_matrix_gain_coupling_upup/np.sqrt(7), label='gain up/up', color='magenta',alpha=0.2)

plt.plot(x, mean_matrix_gain_coupling_downup, label='gain down/up', color='orange')
plt.fill_between(x, mean_matrix_gain_coupling_downup-std_matrix_gain_coupling_downup/np.sqrt(7), mean_matrix_gain_coupling_downup+std_matrix_gain_coupling_downup/np.sqrt(7),label='gain down/up', color='orange', alpha=0.2)

plt.plot(x, mean_matrix_gain_coupling_downdown, label='gain down/down', color='blue')
plt.fill_between(x,mean_matrix_gain_coupling_downdown- std_matrix_gain_coupling_downdown/np.sqrt(7),mean_matrix_gain_coupling_downdown + std_matrix_gain_coupling_downdown/np.sqrt(7), label='gain down/down', color='blue',alpha=0.2)

plt.plot(x, mean_matrix_gain_coupling_updown, label='gain up/down', color='cyan')
plt.fill_between(x, mean_matrix_gain_coupling_updown- std_matrix_gain_coupling_updown/np.sqrt(7),mean_matrix_gain_coupling_updown+ std_matrix_gain_coupling_updown/np.sqrt(7), label='gain up/down', color='cyan', alpha=0.2)

plt.xticks(x,['0','1','1.3','1.5','1.7','1.9','2','3','4'])
plt.xlabel('external input',size=17)
plt.ylabel('closed-loop accuracy gain curves [%]', size=17)
plt.vlines(x=0, ymin=-15, ymax=60,colors='black', linestyle='dashed')
plt.vlines(x=1, ymin=-15, ymax=60,colors='black', linestyle='dashed')
plt.vlines(x=6, ymin=-15, ymax=60,colors='black', linestyle='dashed')
plt.xlim(-0.5,8)
plt.ylim(-15,55)
plt.legend()
plt.show()

matrix_gain_coupling_upup=np.array(matrix_gain_coupling_upup)
matrix_gain_coupling_downup=np.array(matrix_gain_coupling_downup)
matrix_gain_coupling_downdown=np.array(matrix_gain_coupling_downdown)
matrix_gain_coupling_updown=np.array(matrix_gain_coupling_updown)

mean_dataset_matrix_gain_coupling_upup=[np.mean(matrix_gain_coupling_imported['accuracy_up_up_low']), np.mean(matrix_gain_coupling_imported['accuracy_up_up_medium']), np.mean(matrix_gain_coupling_imported['accuracy_up_up_high'])]
std_dataset_matrix_gain_coupling_upup=[np.std(matrix_gain_coupling_imported['accuracy_up_up_low']), np.std(matrix_gain_coupling_imported['accuracy_up_up_medium']), np.std(matrix_gain_coupling_imported['accuracy_up_up_high'])]
cv_dataset_matrix_gain_coupling_upup=[np.mean(matrix_gain_coupling_imported['accuracy_up_up_low'])/np.std(matrix_gain_coupling_imported['accuracy_up_up_low']), np.mean(matrix_gain_coupling_imported['accuracy_up_up_medium'])/np.std(matrix_gain_coupling_imported['accuracy_up_up_medium']), np.mean(matrix_gain_coupling_imported['accuracy_up_up_high'])/np.std(matrix_gain_coupling_imported['accuracy_up_up_high'])]

mean_dataset_matrix_gain_coupling_downup=[np.mean(matrix_gain_coupling_imported['accuracy_down_up_low']), np.mean(matrix_gain_coupling_imported['accuracy_down_up_medium']), np.mean(matrix_gain_coupling_imported['accuracy_down_up_high'])]
std_dataset_matrix_gain_coupling_downup=[np.std(matrix_gain_coupling_imported['accuracy_down_up_low']), np.std(matrix_gain_coupling_imported['accuracy_down_up_medium']), np.std(matrix_gain_coupling_imported['accuracy_down_up_high'])]
cv_dataset_matrix_gain_coupling_downup=[np.mean(matrix_gain_coupling_imported['accuracy_down_up_low'])/np.std(matrix_gain_coupling_imported['accuracy_down_up_low']), np.mean(matrix_gain_coupling_imported['accuracy_down_up_medium'])/np.std(matrix_gain_coupling_imported['accuracy_down_up_medium']), np.mean(matrix_gain_coupling_imported['accuracy_down_up_high'])//np.std(matrix_gain_coupling_imported['accuracy_down_up_high'])]

mean_dataset_matrix_gain_coupling_downdown=[np.mean(matrix_gain_coupling_imported['accuracy_down_down_low']), np.mean(matrix_gain_coupling_imported['accuracy_down_down_medium']), np.mean(matrix_gain_coupling_imported['accuracy_down_down_high'])]
std_dataset_matrix_gain_coupling_downdown=[np.std(matrix_gain_coupling_imported['accuracy_down_down_low']), np.std(matrix_gain_coupling_imported['accuracy_down_down_medium']), np.std(matrix_gain_coupling_imported['accuracy_down_down_high'])]
cv_dataset_matrix_gain_coupling_downdown=[np.mean(matrix_gain_coupling_imported['accuracy_down_down_low'])/np.std(matrix_gain_coupling_imported['accuracy_down_down_low']), np.mean(matrix_gain_coupling_imported['accuracy_down_down_medium'])/np.std(matrix_gain_coupling_imported['accuracy_down_down_medium']), np.mean(matrix_gain_coupling_imported['accuracy_down_down_high'])/np.std(matrix_gain_coupling_imported['accuracy_down_down_high'])]

mean_dataset_matrix_gain_coupling_updown=[np.mean(matrix_gain_coupling_imported['accuracy_up_down_low']), np.mean(matrix_gain_coupling_imported['accuracy_up_down_medium']), np.mean(matrix_gain_coupling_imported['accuracy_up_down_high'])]
std_dataset_matrix_gain_coupling_updown=[np.std(matrix_gain_coupling_imported['accuracy_up_down_low']), np.std(matrix_gain_coupling_imported['accuracy_up_down_medium']), np.std(matrix_gain_coupling_imported['accuracy_up_down_high'])]
cv_dataset_matrix_gain_coupling_updown=[np.mean(matrix_gain_coupling_imported['accuracy_up_down_low'])/np.std(matrix_gain_coupling_imported['accuracy_up_down_low']), np.mean(matrix_gain_coupling_imported['accuracy_up_down_medium'])/np.std(matrix_gain_coupling_imported['accuracy_up_down_medium']), np.mean(matrix_gain_coupling_imported['accuracy_up_down_high'])/np.std(matrix_gain_coupling_imported['accuracy_up_down_high'])]

N = 3
fig, ax = plt.subplots()
ind = np.arange(N) 
width = 0.18
ax.bar(ind-2*width, mean_dataset_matrix_gain_coupling_upup, width,yerr=std_dataset_matrix_gain_coupling_upup/np.sqrt(7), label='gain up/up',align='center',facecolor='magenta',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind-width , mean_dataset_matrix_gain_coupling_downup, width,yerr= std_dataset_matrix_gain_coupling_downup/np.sqrt(7),label='gain down/up',align='center',facecolor='orange',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind , mean_dataset_matrix_gain_coupling_downdown, width, yerr=std_dataset_matrix_gain_coupling_downdown/np.sqrt(7), label='gain down/down',align='center',facecolor='blue',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind + width, mean_dataset_matrix_gain_coupling_updown, width, yerr=std_dataset_matrix_gain_coupling_updown/np.sqrt(7), label='gain up/down', align='center', edgecolor='black',facecolor='cyan', ecolor='black',alpha=0.8, capsize=10)
ax.set_xlabel('range external input',size=17)
ax.set_ylabel('closed-loop accuracy gain [%]',size=17)
ax.set_xticks(ind + width / 2)
plt.xticks(ind, ['low[0-1]', 'medium[1.3-1.9]','high[2-4]'],size=17)
ax.legend()
ax.autoscale_view()
plt.ylim(-15,55)
plt.show()


