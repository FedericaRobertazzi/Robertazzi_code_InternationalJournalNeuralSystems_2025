#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federicarobertazzi
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data_test_open_loop = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_test_open_loop.head()

data_test_closed_loop = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_test_closed_loop.head()

vec_mean_SSRT=[np.mean(data_test_open_loop['SSRT']), np.mean(data_test_closed_loop['SSRT'])]
vec_std_SSRT=[np.std(data_test_open_loop['SSRT']),np.std(data_test_closed_loop['SSRT']) ]

vec_mean_right_inhibition=[np.mean(data_test_open_loop['right_inhibition']),np.mean(data_test_closed_loop['right_inhibition'])]
vec_std_right_inhibition=[np.std(data_test_open_loop['right_inhibition']),np.std(data_test_closed_loop['right_inhibition'])]

vec_mean_accuracy=[np.mean(data_test_open_loop['accuracy']),np.mean(data_test_closed_loop['accuracy'])]
vec_std_accuracy=[np.std(data_test_open_loop['accuracy']),np.std(data_test_closed_loop['accuracy'])]

N = 2
fig, ax = plt.subplots()
ind = np.arange(N)
width = 0.20
ax.bar((0,0.3), vec_mean_SSRT,width, yerr=vec_std_SSRT, align='center', edgecolor='black',color=['white', 'white'],hatch=['///', '///'], ecolor='black', alpha=0.8, capsize=10)
ax.set_ylabel('SSRT [samples]',size=17)
ax.set_xticks(((0,0.3)))
ax.set_xticklabels(('Open-loop', 'Closed-loop'),size=17)
ax.autoscale_view()
plt.ylim(0,50)
bars=ax.patches
for bar, hatch in zip(bars, (" ", "\\")):
        bar.set_hatch(hatch)
plt.show()

fig, ax = plt.subplots()
width = 0.2 
ax.bar((0,0.3), vec_mean_right_inhibition, width, yerr=vec_std_right_inhibition,align='center', edgecolor='black',color=['white', 'white'], ecolor='black', alpha=0.8, capsize=10)
ax.set_ylabel('Right Inhibition [%]',size=17)
ax.set_xticks(((0,0.3)))
ax.set_xticklabels(('Open-loop', 'Closed-loop'),size=17)
ax.autoscale_view()
plt.ylim(0,100)
bars=ax.patches
for bar, hatch in zip(bars, (" ", "\\")):
        bar.set_hatch(hatch)
ax.legend(loc='upper center')
plt.show()

fig, ax = plt.subplots()
width = 0.20
ax.bar((0,0.3), vec_mean_accuracy, width, yerr=vec_std_accuracy, align='center', edgecolor='black', ecolor='black', alpha=0.8, capsize=10, color=('white','white'))
ax.set_ylabel('Accuracy [%]',size=17)
ax.set_xticks(((0,0.3)))
ax.set_xticklabels(('Open-loop', 'Closed-loop'),size=17)
ax.autoscale_view()
plt.ylim(0,100)
bars=ax.patches
for bar, hatch in zip(bars, (" ", "\\")):
        bar.set_hatch(hatch)
plt.show()


































