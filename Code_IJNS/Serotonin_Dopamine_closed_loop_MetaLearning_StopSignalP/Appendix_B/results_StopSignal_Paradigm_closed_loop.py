#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@author: federicarobertazzi
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data_training_closed_loop = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_training_closed_loop.head()

data_test_closed_loop = pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_test_closed_loop.head()

#network parameters and inhibition performance metrics
#mean
vec_mean_mean_reaction_time_Go_1=[np.mean(data_training_closed_loop['mean_reaction_time_Go_1']),np.mean(data_test_closed_loop['mean_reaction_time_Go_1'])]
vec_mean_mean_reaction_time_StopSignal_total_1=[np.mean(data_training_closed_loop['mean_reaction_time_Hold_total_1']),np.mean(data_test_closed_loop['mean_reaction_time_Hold_total_1'])]
vec_mean_mean_reaction_time_StopSignal_1=[np.mean(data_training_closed_loop['mean_reaction_time_Hold_1']),np.mean(data_test_closed_loop['mean_reaction_time_Hold_1'])]
vec_mean_mean_reaction_time_StopSignal_correct_1=[np.mean(data_training_closed_loop['mean_reaction_time_Hold_correct_1']),np.mean(data_test_closed_loop['mean_reaction_time_Hold_correct_1'])]

vec_mean_mean_max_PMC_Go=[np.mean(data_training_closed_loop['mean_max_PMC_Go']),np.mean(data_test_closed_loop['mean_max_PMC_Go'])]
vec_mean_mean_max_PMC_StopSignal_total=[np.mean(data_training_closed_loop['mean_max_PMC_Hold_total']),np.mean(data_test_closed_loop['mean_max_PMC_Hold_total'])]
vec_mean_mean_max_PMC_StopSignal=[np.mean(data_training_closed_loop['mean_max_PMC_Hold']),np.mean(data_test_closed_loop['mean_max_PMC_Hold'])]
vec_mean_mean_max_PMC_StopSignal_correct=[np.mean(data_training_closed_loop['mean_max_PMC_Hold_correct']),np.mean(data_test_closed_loop['mean_max_PMC_Hold_correct'])]

vec_mean_mean_Pmax_Go=[np.mean(data_training_closed_loop['mean_Pmax_Go']),np.mean(data_test_closed_loop['mean_Pmax_Go'])]
vec_mean_mean_Pmax_StopSignal_total=[np.mean(data_training_closed_loop['mean_Pmax_Hold_total']),np.mean(data_test_closed_loop['mean_Pmax_Hold_total'])]
vec_mean_mean_Pmax_StopSignal=[np.mean(data_training_closed_loop['mean_Pmax_Hold']),np.mean(data_test_closed_loop['mean_Pmax_Hold'])]
vec_mean_mean_Pmax_StopSignal_correct=[np.mean(data_training_closed_loop['mean_Pmax_Hold_correct']),np.mean(data_test_closed_loop['mean_Pmax_Hold_correct'])]

vec_mean_SSRT=[0,np.mean(data_test_closed_loop['SSRT'])]

vec_mean_right_inhibition=[np.mean(data_training_closed_loop['right_inhibition']),np.mean(data_test_closed_loop['right_inhibition'])]
vec_mean_accuracy=[np.mean(data_training_closed_loop['accuracy']),np.mean(data_test_closed_loop['accuracy'])]

#standard dev
vec_std_mean_reaction_time_Go_1=[np.std(data_training_closed_loop['mean_reaction_time_Go_1']),np.std(data_test_closed_loop['mean_reaction_time_Go_1'])]
vec_std_mean_reaction_time_StopSignal_total_1=[np.std(data_training_closed_loop['mean_reaction_time_Hold_total_1']),np.std(data_test_closed_loop['mean_reaction_time_Hold_total_1'])]
vec_std_mean_reaction_time_StopSignal_1=[np.std(data_training_closed_loop['mean_reaction_time_Hold_1']),np.std(data_test_closed_loop['mean_reaction_time_Hold_1'])]
vec_std_mean_reaction_time_StopSignal_correct_1=[np.std(data_training_closed_loop['mean_reaction_time_Hold_correct_1']),np.std(data_test_closed_loop['mean_reaction_time_Hold_correct_1'])]

vec_std_mean_max_PMC_Go=[np.std(data_training_closed_loop['mean_max_PMC_Go']),np.std(data_test_closed_loop['mean_max_PMC_Go'])]
vec_std_mean_max_PMC_StopSignal_total=[np.std(data_training_closed_loop['mean_max_PMC_Hold_total']),np.std(data_test_closed_loop['mean_max_PMC_Hold_total'])]
vec_std_mean_max_PMC_StopSignal=[np.std(data_training_closed_loop['mean_max_PMC_Hold']),np.std(data_test_closed_loop['mean_max_PMC_Hold'])]
vec_std_mean_max_PMC_StopSignal_correct=[np.std(data_training_closed_loop['mean_max_PMC_Hold_correct']),np.std(data_test_closed_loop['mean_max_PMC_Hold_correct'])]

vec_std_mean_Pmax_Go=[np.std(data_training_closed_loop['mean_Pmax_Go']),np.std(data_test_closed_loop['mean_Pmax_Go'])]
vec_std_mean_Pmax_StopSignal_total=[np.std(data_training_closed_loop['mean_Pmax_Hold_total']),np.std(data_test_closed_loop['mean_Pmax_Hold_total'])]
vec_std_mean_Pmax_StopSignal=[np.std(data_training_closed_loop['mean_Pmax_Hold']),np.std(data_test_closed_loop['mean_Pmax_Hold'])]
vec_std_mean_Pmax_StopSignal_correct=[np.std(data_training_closed_loop['mean_Pmax_Hold_correct']),np.std(data_test_closed_loop['mean_Pmax_Hold_correct'])]

vec_std_SSRT=[0,np.std(data_test_closed_loop['SSRT'])]

vec_std_right_inhibition=[np.std(data_training_closed_loop['right_inhibition']),np.std(data_test_closed_loop['right_inhibition'])]
vec_std_accuracy=[np.std(data_training_closed_loop['accuracy']),np.std(data_test_closed_loop['accuracy'])]

N = 2
fig, ax = plt.subplots()
ind = np.arange(N) 
width = 0.26
ax.bar(ind-width , vec_mean_mean_reaction_time_Go_1, width,yerr=vec_std_mean_reaction_time_Go_1,
       label='Stop Signal Go Trials',align='center',facecolor='#295981',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind , vec_mean_mean_reaction_time_StopSignal_1, width,yerr=vec_std_mean_reaction_time_StopSignal_1,
       label='Stop Signal failur Trials',align='center',facecolor='#3d84bf',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind + width, vec_mean_mean_reaction_time_StopSignal_correct_1, width,yerr=vec_std_mean_reaction_time_StopSignal_correct_1,
      label='Stop Signal correct Trials',align='center',facecolor='#8dbdda',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.set_ylabel('RT [samples]',size=17)
plt.xticks(ind, ['Training', 'Test'],size=17)
ax.legend()
ax.autoscale_view()
plt.ylim(0,100)
plt.show()

fig, ax = plt.subplots()
ind = np.arange(N)
width = 0.26
ax.bar(ind - width, vec_mean_mean_max_PMC_Go, width, yerr=vec_std_mean_max_PMC_Go, label='Go Trials', align='center', edgecolor='black',facecolor='#295981', ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind, vec_mean_mean_max_PMC_StopSignal, width,yerr=vec_std_mean_max_PMC_StopSignal,
       label='Stop Signal failure Trials',align='center',facecolor='#3d84bf',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind +width, vec_mean_mean_max_PMC_StopSignal_correct, width,yerr= vec_std_mean_max_PMC_StopSignal_correct,
       label='Stop Signal correct Trials  ',align='center',facecolor='#8dbdda',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.set_ylabel('PMC peak [a.u.]',size=17)
ax.set_xticks(ind + width / 2)
plt.xticks(ind, ['Training', 'Test'],size=17)
ax.legend()
ax.autoscale_view()
plt.ylim(0,1)
plt.show()

fig, ax = plt.subplots()
ind = np.arange(N)
width = 0.26
ax.bar(ind - width, vec_mean_mean_Pmax_Go, width, yerr=vec_std_mean_Pmax_Go, label='Go Trials', align='center', edgecolor='black',facecolor='#295981', ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind , vec_mean_mean_Pmax_StopSignal, width,yerr=vec_std_mean_Pmax_StopSignal,
       label='Stop Signal failure Trials',align='center',facecolor='#3d84bf',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.bar(ind +width , vec_mean_mean_Pmax_StopSignal_correct, width,yerr= vec_std_mean_Pmax_StopSignal_correct,
       label='Stop Signal correct Trials',align='center',facecolor='#8dbdda',edgecolor='black',ecolor='black',alpha=0.8, capsize=10)
ax.set_ylabel('P${max}$ ',size=17)
ax.set_xticks(ind + width / 2)
plt.xticks(ind, ['Training', 'Test'],size=17)
ax.legend()
ax.autoscale_view()
plt.ylim(0,1)
plt.show()

fig, ax = plt.subplots()
ind = np.arange(N)
width = 0.20
ax.bar((0,0.3), vec_mean_SSRT,width, yerr=vec_std_SSRT, align='center', edgecolor='black',facecolor='white', ecolor='black', alpha=0.8, capsize=10,fill=False, hatch='\\')
ax.set_ylabel('SSRT [samples]',size=17)
ax.set_xticks(((0,0.3)))
ax.set_xticklabels(('Training', 'Test'),size=17)
ax.autoscale_view()
plt.ylim(0,50)
plt.show()

fig, ax = plt.subplots()
width = 0.2 
ax.bar((0,0.3), vec_mean_right_inhibition, width, yerr=vec_std_right_inhibition,align='center', edgecolor='black', ecolor='black', alpha=0.8, capsize=10,fill=False, hatch='\\')
ax.set_ylabel('Right Inhibition [%]',size=17)
ax.set_xticks(((0,0.3)))
ax.set_xticklabels(('Training', 'Test'),size=17)
ax.autoscale_view()
plt.ylim(0,100)
plt.show()

fig, ax = plt.subplots()
width = 0.20
ax.bar((0,0.3), vec_mean_accuracy, width, yerr=vec_std_accuracy,align='center', edgecolor='black',ecolor='black', alpha=0.8, capsize=10, fill=False, hatch='\\')
ax.set_ylabel('Accuracy [%]',size=17)
ax.set_xticks(((0,0.3)))
ax.set_xticklabels(('Training', 'Test'),size=17)
ax.autoscale_view()
plt.ylim(0,100)
plt.show()















