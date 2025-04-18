#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federica robertazzi
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

D1=[0.1, 0.3, 0.5, 0.7, 0.9]

D2=[0.1, 0.3, 0.5, 0.7, 0.9]

#dataset for reference/etaD1,low/etaD2,high efficacy condition for concentration-response heatmaps
#SEROTONIN S1 = 0.1 and S2 = 0.1
data_S1_01_S2_01_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_01_S2_01_train.head()

data_S1_01_S2_01_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_01_S2_01_test.head()
#SEROTONIN S1 = 0.1 and S2 = 0.3
data_S1_01_S2_03_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_01_S2_03_train.head()

data_S1_01_S2_03_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_01_S2_03_test.head()
#SEROTONIN S1 = 0.1 and S2 = 0.5
data_S1_01_S2_05_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_01_S2_05_train.head()

data_S1_01_S2_05_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_01_S2_05_test.head()
#SEROTONIN S1 = 0.1 and S2 = 0.7
data_S1_01_S2_07_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_01_S2_07_train.head()

data_S1_01_S2_07_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_01_S2_07_test.head()
#SEROTONIN S1 = 0.1 and S2 = 0.9
data_S1_01_S2_09_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_01_S2_09_train.head()

data_S1_01_S2_09_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_01_S2_09_test.head()
#SEROTONIN S1 = 0.3 and S2 = 0.1
data_S1_03_S2_01_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_03_S2_01_train.head()

data_S1_03_S2_01_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_03_S2_01_test.head()
#SEROTONIN S1 = 0.3 and S2 = 0.3
data_S1_03_S2_03_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_03_S2_03_train.head()

data_S1_03_S2_03_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_03_S2_03_test.head()
#SEROTONIN S1 = 0.3 and S2 = 0.5
data_S1_03_S2_05_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_03_S2_05_train.head()

data_S1_03_S2_05_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_03_S2_05_test.head()
#SEROTONIN S1 = 0.3 and S2 = 0.7
data_S1_03_S2_07_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_03_S2_07_train.head()

data_S1_03_S2_07_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_03_S2_07_test.head()
#SEROTONIN S1 = 0.3 and S2 = 0.9
data_S1_03_S2_09_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_03_S2_09_train.head()

data_S1_03_S2_09_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_03_S2_09_test.head()
#SEROTONIN S1 = 0.5 and S2 = 0.1
data_S1_05_S2_01_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_05_S2_01_train.head()

data_S1_05_S2_01_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_05_S2_01_test.head()
#SEROTONIN S1 = 0.5 and S2 = 0.3
data_S1_05_S2_03_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_05_S2_03_train.head()

data_S1_05_S2_03_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_05_S2_03_test.head()
#SEROTONIN S1 = 0.5 and S2 = 0.5
data_S1_05_S2_05_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_05_S2_05_train.head()

data_S1_05_S2_05_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_05_S2_05_test.head()
#SEROTONIN S1 = 0.5 and S2 = 0.7
data_S1_05_S2_07_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_05_S2_07_train.head()

data_S1_05_S2_07_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_05_S2_07_test.head()
#SEROTONIN S1 = 0.5 and S2 = 0.9
data_S1_05_S2_09_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_05_S2_09_train.head()

data_S1_05_S2_09_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_05_S2_09_test.head()
#SEROTONIN S1 = 0.7 and S2 = 0.1
data_S1_07_S2_01_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_07_S2_01_train.head()

data_S1_07_S2_01_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_07_S2_01_test.head()
#SEROTONIN S1 = 0.7 and S2 = 0.3
data_S1_07_S2_03_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_07_S2_03_train.head()

data_S1_07_S2_03_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_07_S2_03_test.head()
#SEROTONIN S1 = 0.7 and S2 = 0.5
data_S1_07_S2_05_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_07_S2_05_train.head()

data_S1_07_S2_05_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_07_S2_05_test.head()
#SEROTONIN S1 = 0.7 and S2 = 0.7
data_S1_07_S2_07_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_07_S2_07_train.head()

data_S1_07_S2_07_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_07_S2_07_test.head()
#SEROTONIN S1 = 0.7 and S2 = 0.9
data_S1_07_S2_09_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_07_S2_09_train.head()

data_S1_07_S2_09_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_07_S2_09_test.head()
#SEROTONIN S1 = 0.9 and S2 = 0.1
data_S1_09_S2_01_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_09_S2_01_train.head()

data_S1_09_S2_01_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_09_S2_01_test.head()
#SEROTONIN S1 = 0.9 and S2 = 0.3
data_S1_09_S2_03_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_09_S2_03_train.head()

data_S1_09_S2_03_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_09_S2_03_test.head()
#SEROTONIN S1 = 0.9 and S2 = 0.5
data_S1_09_S2_05_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_09_S2_05_train.head()

data_S1_09_S2_05_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_09_S2_05_test.head()
#SEROTONIN S1 = 0.9 and S2 = 0.7
data_S1_09_S2_07_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_09_S2_07_train.head()

data_S1_09_S2_07_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_09_S2_07_test.head()
#SEROTONIN S1 = 0.9 and S2 = 0.9
data_S1_09_S2_09_train= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_09_S2_09_train.head()

data_S1_09_S2_09_test= pd.read_csv('<insert path>',delimiter = ';',decimal=",")
data_S1_09_S2_09_test.head()

#SEROTONIN S1 = 0.1 and S2 = 0.1
#training
vec_mean_mean_reaction_time_Go_S1_01_S2_01_train=np.mean(data_S1_01_S2_01_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_01_S2_01_train=np.mean(data_S1_01_S2_01_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_01_train=np.mean(data_S1_01_S2_01_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_01_S2_01_train=np.mean(data_S1_01_S2_01_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_01_S2_01_train=np.mean(data_S1_01_S2_01_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_01_S2_01_train=np.mean(data_S1_01_S2_01_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_01_train=np.mean(data_S1_01_S2_01_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_01_S2_01_train=np.mean(data_S1_01_S2_01_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_01_S2_01_train=np.mean(data_S1_01_S2_01_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_01_S2_01_train=np.mean(data_S1_01_S2_01_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_01_S2_01_train=np.mean(data_S1_01_S2_01_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_01_S2_01_train=np.mean(data_S1_01_S2_01_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_01_S2_01_train=np.mean(data_S1_01_S2_01_train['right_inhibition'])
vec_mean_accuracy_S1_01_S2_01_train=np.mean(data_S1_01_S2_01_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_01_S2_01_train=np.std(data_S1_01_S2_01_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_01_S2_01_train=np.std(data_S1_01_S2_01_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_01_S2_01_train=np.std(data_S1_01_S2_01_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_01_S2_01_train=np.std(data_S1_01_S2_01_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_01_S2_01_train=np.std(data_S1_01_S2_01_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_01_S2_01_train=np.std(data_S1_01_S2_01_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_01_S2_01_train=np.std(data_S1_01_S2_01_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_01_S2_01_train=np.std(data_S1_01_S2_01_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_01_S2_01_train=np.std(data_S1_01_S2_01_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_01_S2_01_train=np.std(data_S1_01_S2_01_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_01_S2_01_train=np.std(data_S1_01_S2_01_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_01_S2_01_train=np.std(data_S1_01_S2_01_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_01_S2_01_train=np.std(data_S1_01_S2_01_train['right_inhibition'])
vec_std_accuracy_S1_01_S2_01_train=np.std(data_S1_01_S2_01_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_01_S2_01_test=np.mean(data_S1_01_S2_01_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_01_S2_01_test=np.mean(data_S1_01_S2_01_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_01_test=np.mean(data_S1_01_S2_01_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_01_S2_01_test=np.mean(data_S1_01_S2_01_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_01_S2_01_test=np.mean(data_S1_01_S2_01_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_01_S2_01_test=np.mean(data_S1_01_S2_01_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_01_test=np.mean(data_S1_01_S2_01_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_01_S2_01_test=np.mean(data_S1_01_S2_01_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_01_S2_01_test=np.mean(data_S1_01_S2_01_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_01_S2_01_test=np.mean(data_S1_01_S2_01_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_01_S2_01_test=np.mean(data_S1_01_S2_01_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_01_S2_01_test=np.mean(data_S1_01_S2_01_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_01_S2_01_test=np.mean(data_S1_01_S2_01_test['SSRT'])
vec_mean_right_inhibition_S1_01_S2_01_test=np.mean(data_S1_01_S2_01_test['right_inhibition'])
vec_mean_accuracy_S1_01_S2_01_test=np.mean(data_S1_01_S2_01_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_01_S2_01_test=np.std(data_S1_01_S2_01_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_01_S2_01_test=np.std(data_S1_01_S2_01_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_01_S2_01_test=np.std(data_S1_01_S2_01_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_01_S2_01_test=np.std(data_S1_01_S2_01_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_01_S2_01_test=np.std(data_S1_01_S2_01_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_01_S2_01_test=np.std(data_S1_01_S2_01_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_01_S2_01_test=np.std(data_S1_01_S2_01_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_01_S2_01_test=np.std(data_S1_01_S2_01_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_01_S2_01_test=np.std(data_S1_01_S2_01_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_01_S2_01_test=np.std(data_S1_01_S2_01_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_01_S2_01_test=np.std(data_S1_01_S2_01_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_01_S2_01_test=np.std(data_S1_01_S2_01_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_01_S2_01_test=np.std(data_S1_01_S2_01_test['SSRT'])
vec_std_right_inhibition_S1_01_S2_01_test=np.std(data_S1_01_S2_01_test['right_inhibition'])
vec_std_accuracy_S1_01_S2_01_test=np.std(data_S1_01_S2_01_test['accuracy'])

#geometric mean max PMC & Pmax
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_01_train*vec_mean_mean_Pmax_Go_S1_01_S2_01_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_01_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_01_train*vec_mean_mean_Pmax_Hold_S1_01_S2_01_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_01_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_01_train*vec_mean_mean_Pmax_Hold_correct_S1_01_S2_01_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_01_train*vec_mean_mean_Pmax_Hold_total_S1_01_S2_01_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_01_test*vec_mean_mean_Pmax_Go_S1_01_S2_01_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_01_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_01_test*vec_mean_mean_Pmax_Hold_S1_01_S2_01_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_01_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_01_test*vec_mean_mean_Pmax_Hold_correct_S1_01_S2_01_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_01_test*vec_mean_mean_Pmax_Hold_total_S1_01_S2_01_test)

#geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_01_train*vec_mean_mean_reaction_time_Go_S1_01_S2_01_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_01_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_01_train*vec_mean_mean_reaction_time_Hold_S1_01_S2_01_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_01_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_01_train*vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_01_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_01_train*vec_mean_mean_reaction_time_Hold_total_S1_01_S2_01_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_01_test*vec_mean_mean_reaction_time_Go_S1_01_S2_01_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_01_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_01_test*vec_mean_mean_reaction_time_Hold_S1_01_S2_01_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_01_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_01_test*vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_01_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_01_test*vec_mean_mean_reaction_time_Hold_total_S1_01_S2_01_test)

#SEROTONIN S1 = 0.1 and S2 = 0.3
#training
vec_mean_mean_reaction_time_Go_S1_01_S2_03_train=np.mean(data_S1_01_S2_03_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_01_S2_03_train=np.mean(data_S1_01_S2_03_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_03_train=np.mean(data_S1_01_S2_03_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_01_S2_03_train=np.mean(data_S1_01_S2_03_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_01_S2_03_train=np.mean(data_S1_01_S2_03_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_01_S2_03_train=np.mean(data_S1_01_S2_03_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_03_train=np.mean(data_S1_01_S2_03_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_01_S2_03_train=np.mean(data_S1_01_S2_03_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_01_S2_03_train=np.mean(data_S1_01_S2_03_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_01_S2_03_train=np.mean(data_S1_01_S2_03_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_01_S2_03_train=np.mean(data_S1_01_S2_03_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_01_S2_03_train=np.mean(data_S1_01_S2_03_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_01_S2_03_train=np.mean(data_S1_01_S2_03_train['right_inhibition'])
vec_mean_accuracy_S1_01_S2_03_train=np.mean(data_S1_01_S2_03_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_01_S2_03_train=np.std(data_S1_01_S2_03_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_01_S2_03_train=np.std(data_S1_01_S2_03_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_01_S2_03_train=np.std(data_S1_01_S2_03_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_01_S2_03_train=np.std(data_S1_01_S2_03_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_01_S2_03_train=np.std(data_S1_01_S2_03_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_01_S2_03_train=np.std(data_S1_01_S2_03_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_01_S2_03_train=np.std(data_S1_01_S2_03_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_01_S2_03_train=np.std(data_S1_01_S2_03_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_01_S2_03_train=np.std(data_S1_01_S2_03_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_01_S2_03_train=np.std(data_S1_01_S2_03_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_01_S2_03_train=np.std(data_S1_01_S2_03_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_01_S2_03_train=np.std(data_S1_01_S2_03_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_01_S2_03_train=np.std(data_S1_01_S2_03_train['right_inhibition'])
vec_std_accuracy_S1_01_S2_03_train=np.std(data_S1_01_S2_03_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_01_S2_03_test=np.mean(data_S1_01_S2_03_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_01_S2_03_test=np.mean(data_S1_01_S2_03_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_03_test=np.mean(data_S1_01_S2_03_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_01_S2_03_test=np.mean(data_S1_01_S2_03_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_01_S2_03_test=np.mean(data_S1_01_S2_03_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_01_S2_03_test=np.mean(data_S1_01_S2_03_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_03_test=np.mean(data_S1_01_S2_03_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_01_S2_03_test=np.mean(data_S1_01_S2_03_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_01_S2_03_test=np.mean(data_S1_01_S2_03_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_01_S2_03_test=np.mean(data_S1_01_S2_03_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_01_S2_03_test=np.mean(data_S1_01_S2_03_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_01_S2_03_test=np.mean(data_S1_01_S2_03_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_01_S2_03_test=np.mean(data_S1_01_S2_03_test['SSRT'])
vec_mean_right_inhibition_S1_01_S2_03_test=np.mean(data_S1_01_S2_03_test['right_inhibition'])
vec_mean_accuracy_S1_01_S2_03_test=np.mean(data_S1_01_S2_03_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_01_S2_03_test=np.std(data_S1_01_S2_03_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_01_S2_03_test=np.std(data_S1_01_S2_03_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_01_S2_03_test=np.std(data_S1_01_S2_03_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_01_S2_03_test=np.std(data_S1_01_S2_03_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_01_S2_03_test=np.std(data_S1_01_S2_03_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_01_S2_03_test=np.std(data_S1_01_S2_03_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_01_S2_03_test=np.std(data_S1_01_S2_03_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_01_S2_03_test=np.std(data_S1_01_S2_03_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_01_S2_03_test=np.std(data_S1_01_S2_03_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_01_S2_03_test=np.std(data_S1_01_S2_03_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_01_S2_03_test=np.std(data_S1_01_S2_03_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_01_S2_03_test=np.std(data_S1_01_S2_03_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_01_S2_03_test=np.std(data_S1_01_S2_03_test['SSRT'])
vec_std_right_inhibition_S1_01_S2_03_test=np.std(data_S1_01_S2_03_test['right_inhibition'])
vec_std_accuracy_S1_01_S2_03_test=np.std(data_S1_01_S2_03_test['accuracy'])

#geometric mean max PMC & Pmax
#training 
vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_03_train*vec_mean_mean_Pmax_Go_S1_01_S2_03_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_01_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_03_train*vec_mean_mean_Pmax_Hold_S1_01_S2_03_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_01_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_03_train*vec_mean_mean_Pmax_Hold_correct_S1_01_S2_03_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_03_train*vec_mean_mean_Pmax_Hold_total_S1_01_S2_03_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_03_test*vec_mean_mean_Pmax_Go_S1_01_S2_03_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_01_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_03_test*vec_mean_mean_Pmax_Hold_S1_01_S2_03_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_01_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_03_test*vec_mean_mean_Pmax_Hold_correct_S1_01_S2_03_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_03_test*vec_mean_mean_Pmax_Hold_total_S1_01_S2_03_test)

#geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_03_train*vec_mean_mean_reaction_time_Go_S1_01_S2_03_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_01_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_03_train*vec_mean_mean_reaction_time_Hold_S1_01_S2_03_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_01_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_03_train*vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_03_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_03_train*vec_mean_mean_reaction_time_Hold_total_S1_01_S2_03_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_03_test*vec_mean_mean_reaction_time_Go_S1_01_S2_03_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_01_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_03_test*vec_mean_mean_reaction_time_Hold_S1_01_S2_03_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_01_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_03_test*vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_03_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_03_test*vec_mean_mean_reaction_time_Hold_total_S1_01_S2_03_test)

#SEROTONIN S1 = 0.1 and S2 = 0.5
#training
vec_mean_mean_reaction_time_Go_S1_01_S2_05_train=np.mean(data_S1_01_S2_05_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_01_S2_05_train=np.mean(data_S1_01_S2_05_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_05_train=np.mean(data_S1_01_S2_05_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_01_S2_05_train=np.mean(data_S1_01_S2_05_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_01_S2_05_train=np.mean(data_S1_01_S2_05_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_01_S2_05_train=np.mean(data_S1_01_S2_05_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_05_train=np.mean(data_S1_01_S2_05_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_01_S2_05_train=np.mean(data_S1_01_S2_05_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_01_S2_05_train=np.mean(data_S1_01_S2_05_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_01_S2_05_train=np.mean(data_S1_01_S2_05_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_01_S2_05_train=np.mean(data_S1_01_S2_05_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_01_S2_05_train=np.mean(data_S1_01_S2_05_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_01_S2_05_train=np.mean(data_S1_01_S2_05_train['right_inhibition'])
vec_mean_accuracy_S1_01_S2_05_train=np.mean(data_S1_01_S2_05_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_01_S2_05_train=np.std(data_S1_01_S2_05_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_01_S2_05_train=np.std(data_S1_01_S2_05_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_01_S2_05_train=np.std(data_S1_01_S2_05_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_01_S2_05_train=np.std(data_S1_01_S2_05_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_01_S2_05_train=np.std(data_S1_01_S2_05_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_01_S2_05_train=np.std(data_S1_01_S2_05_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_01_S2_05_train=np.std(data_S1_01_S2_05_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_01_S2_05_train=np.std(data_S1_01_S2_05_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_01_S2_05_train=np.std(data_S1_01_S2_05_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_01_S2_05_train=np.std(data_S1_01_S2_05_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_01_S2_05_train=np.std(data_S1_01_S2_05_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_01_S2_05_train=np.std(data_S1_01_S2_05_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_01_S2_05_train=np.std(data_S1_01_S2_05_train['right_inhibition'])
vec_std_accuracy_S1_01_S2_05_train=np.std(data_S1_01_S2_05_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_01_S2_05_test=np.mean(data_S1_01_S2_05_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_01_S2_05_test=np.mean(data_S1_01_S2_05_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_05_test=np.mean(data_S1_01_S2_05_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_01_S2_05_test=np.mean(data_S1_01_S2_05_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_01_S2_05_test=np.mean(data_S1_01_S2_05_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_01_S2_05_test=np.mean(data_S1_01_S2_05_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_05_test=np.mean(data_S1_01_S2_05_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_01_S2_05_test=np.mean(data_S1_01_S2_05_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_01_S2_05_test=np.mean(data_S1_01_S2_05_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_01_S2_05_test=np.mean(data_S1_01_S2_05_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_01_S2_05_test=np.mean(data_S1_01_S2_05_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_01_S2_05_test=np.mean(data_S1_01_S2_05_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_01_S2_05_test=np.mean(data_S1_01_S2_05_test['SSRT'])
vec_mean_right_inhibition_S1_01_S2_05_test=np.mean(data_S1_01_S2_05_test['right_inhibition'])
vec_mean_accuracy_S1_01_S2_05_test=np.mean(data_S1_01_S2_05_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_01_S2_05_test=np.std(data_S1_01_S2_05_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_01_S2_05_test=np.std(data_S1_01_S2_05_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_01_S2_05_test=np.std(data_S1_01_S2_05_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_01_S2_05_test=np.std(data_S1_01_S2_05_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_01_S2_05_test=np.std(data_S1_01_S2_05_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_01_S2_05_test=np.std(data_S1_01_S2_05_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_01_S2_05_test=np.std(data_S1_01_S2_05_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_01_S2_05_test=np.std(data_S1_01_S2_05_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_01_S2_05_test=np.std(data_S1_01_S2_05_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_01_S2_05_test=np.std(data_S1_01_S2_05_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_01_S2_05_test=np.std(data_S1_01_S2_05_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_01_S2_05_test=np.std(data_S1_01_S2_05_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_01_S2_05_test=np.std(data_S1_01_S2_05_test['SSRT'])
vec_std_right_inhibition_S1_01_S2_05_test=np.std(data_S1_01_S2_05_test['right_inhibition'])
vec_std_accuracy_S1_01_S2_05_test=np.std(data_S1_01_S2_05_test['accuracy'])

#geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_05_train*vec_mean_mean_Pmax_Go_S1_01_S2_05_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_01_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_05_train*vec_mean_mean_Pmax_Hold_S1_01_S2_05_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_01_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_05_train*vec_mean_mean_Pmax_Hold_correct_S1_01_S2_05_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_05_train*vec_mean_mean_Pmax_Hold_total_S1_01_S2_05_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_05_test*vec_mean_mean_Pmax_Go_S1_01_S2_05_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_01_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_05_test*vec_mean_mean_Pmax_Hold_S1_01_S2_05_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_01_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_05_test*vec_mean_mean_Pmax_Hold_correct_S1_01_S2_05_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_05_test*vec_mean_mean_Pmax_Hold_total_S1_01_S2_05_test)

#geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_05_train*vec_mean_mean_reaction_time_Go_S1_01_S2_05_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_01_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_05_train*vec_mean_mean_reaction_time_Hold_S1_01_S2_05_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_01_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_05_train*vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_05_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_05_train*vec_mean_mean_reaction_time_Hold_total_S1_01_S2_05_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_05_test*vec_mean_mean_reaction_time_Go_S1_01_S2_05_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_01_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_05_test*vec_mean_mean_reaction_time_Hold_S1_01_S2_05_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_01_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_05_test*vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_05_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_05_test*vec_mean_mean_reaction_time_Hold_total_S1_01_S2_05_test)

#SEROTONIN S1 = 0.1 and S2 = 0.7
#training
vec_mean_mean_reaction_time_Go_S1_01_S2_07_train=np.mean(data_S1_01_S2_07_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_01_S2_07_train=np.mean(data_S1_01_S2_07_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_07_train=np.mean(data_S1_01_S2_07_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_01_S2_07_train=np.mean(data_S1_01_S2_07_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_01_S2_07_train=np.mean(data_S1_01_S2_07_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_01_S2_07_train=np.mean(data_S1_01_S2_07_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_07_train=np.mean(data_S1_01_S2_07_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_01_S2_07_train=np.mean(data_S1_01_S2_07_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_01_S2_07_train=np.mean(data_S1_01_S2_07_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_01_S2_07_train=np.mean(data_S1_01_S2_07_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_01_S2_07_train=np.mean(data_S1_01_S2_07_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_01_S2_07_train=np.mean(data_S1_01_S2_07_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_01_S2_07_train=np.mean(data_S1_01_S2_07_train['right_inhibition'])
vec_mean_accuracy_S1_01_S2_07_train=np.mean(data_S1_01_S2_07_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_01_S2_07_train=np.std(data_S1_01_S2_07_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_01_S2_07_train=np.std(data_S1_01_S2_07_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_01_S2_07_train=np.std(data_S1_01_S2_07_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_01_S2_07_train=np.std(data_S1_01_S2_07_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_01_S2_07_train=np.std(data_S1_01_S2_07_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_01_S2_07_train=np.std(data_S1_01_S2_07_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_01_S2_07_train=np.std(data_S1_01_S2_07_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_01_S2_07_train=np.std(data_S1_01_S2_07_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_01_S2_07_train=np.std(data_S1_01_S2_07_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_01_S2_07_train=np.std(data_S1_01_S2_07_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_01_S2_07_train=np.std(data_S1_01_S2_07_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_01_S2_07_train=np.std(data_S1_01_S2_07_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_01_S2_07_train=np.std(data_S1_01_S2_07_train['right_inhibition'])
vec_std_accuracy_S1_01_S2_07_train=np.std(data_S1_01_S2_07_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_01_S2_07_test=np.mean(data_S1_01_S2_07_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_01_S2_07_test=np.mean(data_S1_01_S2_07_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_07_test=np.mean(data_S1_01_S2_07_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_01_S2_07_test=np.mean(data_S1_01_S2_07_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_01_S2_07_test=np.mean(data_S1_01_S2_07_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_01_S2_07_test=np.mean(data_S1_01_S2_07_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_07_test=np.mean(data_S1_01_S2_07_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_01_S2_07_test=np.mean(data_S1_01_S2_07_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_01_S2_07_test=np.mean(data_S1_01_S2_07_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_01_S2_07_test=np.mean(data_S1_01_S2_07_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_01_S2_07_test=np.mean(data_S1_01_S2_07_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_01_S2_07_test=np.mean(data_S1_01_S2_07_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_01_S2_07_test=np.mean(data_S1_01_S2_07_test['SSRT'])
vec_mean_right_inhibition_S1_01_S2_07_test=np.mean(data_S1_01_S2_07_test['right_inhibition'])
vec_mean_accuracy_S1_01_S2_07_test=np.mean(data_S1_01_S2_07_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_01_S2_07_test=np.std(data_S1_01_S2_07_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_01_S2_07_test=np.std(data_S1_01_S2_07_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_01_S2_07_test=np.std(data_S1_01_S2_07_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_01_S2_07_test=np.std(data_S1_01_S2_07_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_01_S2_07_test=np.std(data_S1_01_S2_07_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_01_S2_07_test=np.std(data_S1_01_S2_07_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_01_S2_07_test=np.std(data_S1_01_S2_07_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_01_S2_07_test=np.std(data_S1_01_S2_07_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_01_S2_07_test=np.std(data_S1_01_S2_07_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_01_S2_07_test=np.std(data_S1_01_S2_07_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_01_S2_07_test=np.std(data_S1_01_S2_07_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_01_S2_07_test=np.std(data_S1_01_S2_07_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_01_S2_07_test=np.std(data_S1_01_S2_07_test['SSRT'])
vec_std_right_inhibition_S1_01_S2_07_test=np.std(data_S1_01_S2_07_test['right_inhibition'])
vec_std_accuracy_S1_01_S2_07_test=np.std(data_S1_01_S2_07_test['accuracy'])

#geometric mean max PMC & Pmax
#training 
vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_07_train*vec_mean_mean_Pmax_Go_S1_01_S2_07_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_01_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_07_train*vec_mean_mean_Pmax_Hold_S1_01_S2_07_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_01_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_07_train*vec_mean_mean_Pmax_Hold_correct_S1_01_S2_07_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_07_train*vec_mean_mean_Pmax_Hold_total_S1_01_S2_07_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_07_test*vec_mean_mean_Pmax_Go_S1_01_S2_07_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_01_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_07_test*vec_mean_mean_Pmax_Hold_S1_01_S2_07_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_01_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_07_test*vec_mean_mean_Pmax_Hold_correct_S1_01_S2_07_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_07_test*vec_mean_mean_Pmax_Hold_total_S1_01_S2_07_test)

#geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_07_train*vec_mean_mean_reaction_time_Go_S1_01_S2_07_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_01_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_07_train*vec_mean_mean_reaction_time_Hold_S1_01_S2_07_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_01_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_07_train*vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_07_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_07_train*vec_mean_mean_reaction_time_Hold_total_S1_01_S2_07_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_07_test*vec_mean_mean_reaction_time_Go_S1_01_S2_07_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_01_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_07_test*vec_mean_mean_reaction_time_Hold_S1_01_S2_07_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_01_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_07_test*vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_07_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_07_test*vec_mean_mean_reaction_time_Hold_total_S1_01_S2_07_test)

#SEROTONIN S1 = 0.1 and S2 = 0.9
#training
vec_mean_mean_reaction_time_Go_S1_01_S2_09_train=np.mean(data_S1_01_S2_09_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_01_S2_09_train=np.mean(data_S1_01_S2_09_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_09_train=np.mean(data_S1_01_S2_09_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_01_S2_09_train=np.mean(data_S1_01_S2_09_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_01_S2_09_train=np.mean(data_S1_01_S2_09_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_01_S2_09_train=np.mean(data_S1_01_S2_09_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_09_train=np.mean(data_S1_01_S2_09_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_01_S2_09_train=np.mean(data_S1_01_S2_09_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_01_S2_09_train=np.mean(data_S1_01_S2_09_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_01_S2_09_train=np.mean(data_S1_01_S2_09_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_01_S2_09_train=np.mean(data_S1_01_S2_09_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_01_S2_09_train=np.mean(data_S1_01_S2_09_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_01_S2_09_train=np.mean(data_S1_01_S2_09_train['right_inhibition'])
vec_mean_accuracy_S1_01_S2_09_train=np.mean(data_S1_01_S2_09_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_01_S2_09_train=np.std(data_S1_01_S2_09_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_01_S2_09_train=np.std(data_S1_01_S2_09_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_01_S2_09_train=np.std(data_S1_01_S2_09_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_01_S2_09_train=np.std(data_S1_01_S2_09_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_01_S2_09_train=np.std(data_S1_01_S2_09_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_01_S2_09_train=np.std(data_S1_01_S2_09_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_01_S2_09_train=np.std(data_S1_01_S2_09_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_01_S2_09_train=np.std(data_S1_01_S2_09_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_01_S2_09_train=np.std(data_S1_01_S2_09_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_01_S2_09_train=np.std(data_S1_01_S2_09_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_01_S2_09_train=np.std(data_S1_01_S2_09_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_01_S2_09_train=np.std(data_S1_01_S2_09_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_01_S2_09_train=np.std(data_S1_01_S2_09_train['right_inhibition'])
vec_std_accuracy_S1_01_S2_09_train=np.std(data_S1_01_S2_09_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_01_S2_09_test=np.mean(data_S1_01_S2_09_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_01_S2_09_test=np.mean(data_S1_01_S2_09_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_09_test=np.mean(data_S1_01_S2_09_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_01_S2_09_test=np.mean(data_S1_01_S2_09_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_01_S2_09_test=np.mean(data_S1_01_S2_09_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_01_S2_09_test=np.mean(data_S1_01_S2_09_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_09_test=np.mean(data_S1_01_S2_09_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_01_S2_09_test=np.mean(data_S1_01_S2_09_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_01_S2_09_test=np.mean(data_S1_01_S2_09_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_01_S2_09_test=np.mean(data_S1_01_S2_09_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_01_S2_09_test=np.mean(data_S1_01_S2_09_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_01_S2_09_test=np.mean(data_S1_01_S2_09_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_01_S2_09_test=np.mean(data_S1_01_S2_09_test['SSRT'])
vec_mean_right_inhibition_S1_01_S2_09_test=np.mean(data_S1_01_S2_09_test['right_inhibition'])
vec_mean_accuracy_S1_01_S2_09_test=np.mean(data_S1_01_S2_09_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_01_S2_09_test=np.std(data_S1_01_S2_09_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_01_S2_09_test=np.std(data_S1_01_S2_09_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_01_S2_09_test=np.std(data_S1_01_S2_09_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_01_S2_09_test=np.std(data_S1_01_S2_09_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_01_S2_09_test=np.std(data_S1_01_S2_09_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_01_S2_09_test=np.std(data_S1_01_S2_09_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_01_S2_09_test=np.std(data_S1_01_S2_09_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_01_S2_09_test=np.std(data_S1_01_S2_09_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_01_S2_09_test=np.std(data_S1_01_S2_09_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_01_S2_09_test=np.std(data_S1_01_S2_09_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_01_S2_09_test=np.std(data_S1_01_S2_09_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_01_S2_09_test=np.std(data_S1_01_S2_09_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_01_S2_09_test=np.std(data_S1_01_S2_09_test['SSRT'])
vec_std_right_inhibition_S1_01_S2_09_test=np.std(data_S1_01_S2_09_test['right_inhibition'])
vec_std_accuracy_S1_01_S2_09_test=np.std(data_S1_01_S2_09_test['accuracy'])

#geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_09_train*vec_mean_mean_Pmax_Go_S1_01_S2_09_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_01_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_09_train*vec_mean_mean_Pmax_Hold_S1_01_S2_09_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_01_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_09_train*vec_mean_mean_Pmax_Hold_correct_S1_01_S2_09_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_09_train*vec_mean_mean_Pmax_Hold_total_S1_01_S2_09_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_09_test*vec_mean_mean_Pmax_Go_S1_01_S2_09_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_01_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_09_test*vec_mean_mean_Pmax_Hold_S1_01_S2_09_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_01_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_09_test*vec_mean_mean_Pmax_Hold_correct_S1_01_S2_09_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_09_test*vec_mean_mean_Pmax_Hold_total_S1_01_S2_09_test)

#geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_09_train*vec_mean_mean_reaction_time_Go_S1_01_S2_09_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_01_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_09_train*vec_mean_mean_reaction_time_Hold_S1_01_S2_09_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_01_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_09_train*vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_09_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_09_train*vec_mean_mean_reaction_time_Hold_total_S1_01_S2_09_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_01_S2_09_test*vec_mean_mean_reaction_time_Go_S1_01_S2_09_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_01_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_01_S2_09_test*vec_mean_mean_reaction_time_Hold_S1_01_S2_09_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_01_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_09_test*vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_09_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_01_S2_09_test*vec_mean_mean_reaction_time_Hold_total_S1_01_S2_09_test)

#SEROTONIN S1 = 0.3 and S2 = 0.1
#training
vec_mean_mean_reaction_time_Go_S1_03_S2_01_train=np.mean(data_S1_03_S2_01_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_03_S2_01_train=np.mean(data_S1_03_S2_01_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_01_train=np.mean(data_S1_03_S2_01_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_03_S2_01_train=np.mean(data_S1_03_S2_01_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_03_S2_01_train=np.mean(data_S1_03_S2_01_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_03_S2_01_train=np.mean(data_S1_03_S2_01_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_01_train=np.mean(data_S1_03_S2_01_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_03_S2_01_train=np.mean(data_S1_03_S2_01_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_03_S2_01_train=np.mean(data_S1_03_S2_01_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_03_S2_01_train=np.mean(data_S1_03_S2_01_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_03_S2_01_train=np.mean(data_S1_03_S2_01_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_03_S2_01_train=np.mean(data_S1_03_S2_01_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_03_S2_01_train=np.mean(data_S1_03_S2_01_train['right_inhibition'])
vec_mean_accuracy_S1_03_S2_01_train=np.mean(data_S1_03_S2_01_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_03_S2_01_train=np.std(data_S1_03_S2_01_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_03_S2_01_train=np.std(data_S1_03_S2_01_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_03_S2_01_train=np.std(data_S1_03_S2_01_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_03_S2_01_train=np.std(data_S1_03_S2_01_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_03_S2_01_train=np.std(data_S1_03_S2_01_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_03_S2_01_train=np.std(data_S1_03_S2_01_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_03_S2_01_train=np.std(data_S1_03_S2_01_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_03_S2_01_train=np.std(data_S1_03_S2_01_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_03_S2_01_train=np.std(data_S1_03_S2_01_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_03_S2_01_train=np.std(data_S1_03_S2_01_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_03_S2_01_train=np.std(data_S1_03_S2_01_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_03_S2_01_train=np.std(data_S1_03_S2_01_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_03_S2_01_train=np.std(data_S1_03_S2_01_train['right_inhibition'])
vec_std_accuracy_S1_03_S2_01_train=np.std(data_S1_03_S2_01_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_03_S2_01_test=np.mean(data_S1_03_S2_01_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_03_S2_01_test=np.mean(data_S1_03_S2_01_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_01_test=np.mean(data_S1_03_S2_01_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_03_S2_01_test=np.mean(data_S1_03_S2_01_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_03_S2_01_test=np.mean(data_S1_03_S2_01_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_03_S2_01_test=np.mean(data_S1_03_S2_01_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_01_test=np.mean(data_S1_03_S2_01_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_03_S2_01_test=np.mean(data_S1_03_S2_01_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_03_S2_01_test=np.mean(data_S1_03_S2_01_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_03_S2_01_test=np.mean(data_S1_03_S2_01_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_03_S2_01_test=np.mean(data_S1_03_S2_01_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_03_S2_01_test=np.mean(data_S1_03_S2_01_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_03_S2_01_test=np.mean(data_S1_03_S2_01_test['SSRT'])
vec_mean_right_inhibition_S1_03_S2_01_test=np.mean(data_S1_03_S2_01_test['right_inhibition'])
vec_mean_accuracy_S1_03_S2_01_test=np.mean(data_S1_03_S2_01_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_03_S2_01_test=np.std(data_S1_03_S2_01_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_03_S2_01_test=np.std(data_S1_03_S2_01_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_03_S2_01_test=np.std(data_S1_03_S2_01_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_03_S2_01_test=np.std(data_S1_03_S2_01_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_03_S2_01_test=np.std(data_S1_03_S2_01_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_03_S2_01_test=np.std(data_S1_03_S2_01_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_03_S2_01_test=np.std(data_S1_03_S2_01_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_03_S2_01_test=np.std(data_S1_03_S2_01_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_03_S2_01_test=np.std(data_S1_03_S2_01_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_03_S2_01_test=np.std(data_S1_03_S2_01_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_03_S2_01_test=np.std(data_S1_03_S2_01_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_03_S2_01_test=np.std(data_S1_03_S2_01_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_03_S2_01_test=np.std(data_S1_03_S2_01_test['SSRT'])
vec_std_right_inhibition_S1_03_S2_01_test=np.std(data_S1_03_S2_01_test['right_inhibition'])
vec_std_accuracy_S1_03_S2_01_test=np.std(data_S1_03_S2_01_test['accuracy'])

#geometric mean max PMC & Pmax 
#training 
vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_01_train*vec_mean_mean_Pmax_Go_S1_03_S2_01_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_03_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_01_train*vec_mean_mean_Pmax_Hold_S1_03_S2_01_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_03_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_01_train*vec_mean_mean_Pmax_Hold_correct_S1_03_S2_01_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_01_train*vec_mean_mean_Pmax_Hold_total_S1_03_S2_01_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_01_test*vec_mean_mean_Pmax_Go_S1_03_S2_01_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_03_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_01_test*vec_mean_mean_Pmax_Hold_S1_03_S2_01_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_03_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_01_test*vec_mean_mean_Pmax_Hold_correct_S1_03_S2_01_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_01_test*vec_mean_mean_Pmax_Hold_total_S1_03_S2_01_test)

#geometric mean max PMC & RT
#training 
vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_01_train*vec_mean_mean_reaction_time_Go_S1_03_S2_01_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_03_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_01_train*vec_mean_mean_reaction_time_Hold_S1_03_S2_01_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_03_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_01_train*vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_01_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_01_train*vec_mean_mean_reaction_time_Hold_total_S1_03_S2_01_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_01_test*vec_mean_mean_reaction_time_Go_S1_03_S2_01_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_03_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_01_test*vec_mean_mean_reaction_time_Hold_S1_03_S2_01_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_03_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_01_test*vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_01_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_01_test*vec_mean_mean_reaction_time_Hold_total_S1_03_S2_01_test)

#SEROTONIN S1 = 0.3 and S2 = 0.3
#training
vec_mean_mean_reaction_time_Go_S1_03_S2_03_train=np.mean(data_S1_03_S2_03_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_03_S2_03_train=np.mean(data_S1_03_S2_03_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_03_train=np.mean(data_S1_03_S2_03_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_03_S2_03_train=np.mean(data_S1_03_S2_03_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_03_S2_03_train=np.mean(data_S1_03_S2_03_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_03_S2_03_train=np.mean(data_S1_03_S2_03_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_03_train=np.mean(data_S1_03_S2_03_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_03_S2_03_train=np.mean(data_S1_03_S2_03_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_03_S2_03_train=np.mean(data_S1_03_S2_03_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_03_S2_03_train=np.mean(data_S1_03_S2_03_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_03_S2_03_train=np.mean(data_S1_03_S2_03_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_03_S2_03_train=np.mean(data_S1_03_S2_03_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_03_S2_03_train=np.mean(data_S1_03_S2_03_train['right_inhibition'])
vec_mean_accuracy_S1_03_S2_03_train=np.mean(data_S1_03_S2_03_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_03_S2_03_train=np.std(data_S1_03_S2_03_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_03_S2_03_train=np.std(data_S1_03_S2_03_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_03_S2_03_train=np.std(data_S1_03_S2_03_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_03_S2_03_train=np.std(data_S1_03_S2_03_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_03_S2_03_train=np.std(data_S1_03_S2_03_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_03_S2_03_train=np.std(data_S1_03_S2_03_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_03_S2_03_train=np.std(data_S1_03_S2_03_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_03_S2_03_train=np.std(data_S1_03_S2_03_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_03_S2_03_train=np.std(data_S1_03_S2_03_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_03_S2_03_train=np.std(data_S1_03_S2_03_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_03_S2_03_train=np.std(data_S1_03_S2_03_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_03_S2_03_train=np.std(data_S1_03_S2_03_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_03_S2_03_train=np.std(data_S1_03_S2_03_train['right_inhibition'])
vec_std_accuracy_S1_03_S2_03_train=np.std(data_S1_03_S2_03_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_03_S2_03_test=np.mean(data_S1_03_S2_03_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_03_S2_03_test=np.mean(data_S1_03_S2_03_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_03_test=np.mean(data_S1_03_S2_03_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_03_S2_03_test=np.mean(data_S1_03_S2_03_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_03_S2_03_test=np.mean(data_S1_03_S2_03_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_03_S2_03_test=np.mean(data_S1_03_S2_03_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_03_test=np.mean(data_S1_03_S2_03_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_03_S2_03_test=np.mean(data_S1_03_S2_03_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_03_S2_03_test=np.mean(data_S1_03_S2_03_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_03_S2_03_test=np.mean(data_S1_03_S2_03_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_03_S2_03_test=np.mean(data_S1_03_S2_03_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_03_S2_03_test=np.mean(data_S1_03_S2_03_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_03_S2_03_test=np.mean(data_S1_03_S2_03_test['SSRT'])
vec_mean_right_inhibition_S1_03_S2_03_test=np.mean(data_S1_03_S2_03_test['right_inhibition'])
vec_mean_accuracy_S1_03_S2_03_test=np.mean(data_S1_03_S2_03_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_03_S2_03_test=np.std(data_S1_03_S2_03_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_03_S2_03_test=np.std(data_S1_03_S2_03_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_03_S2_03_test=np.std(data_S1_03_S2_03_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_03_S2_03_test=np.std(data_S1_03_S2_03_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_03_S2_03_test=np.std(data_S1_03_S2_03_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_03_S2_03_test=np.std(data_S1_03_S2_03_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_03_S2_03_test=np.std(data_S1_03_S2_03_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_03_S2_03_test=np.std(data_S1_03_S2_03_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_03_S2_03_test=np.std(data_S1_03_S2_03_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_03_S2_03_test=np.std(data_S1_03_S2_03_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_03_S2_03_test=np.std(data_S1_03_S2_03_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_03_S2_03_test=np.std(data_S1_03_S2_03_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_03_S2_03_test=np.std(data_S1_03_S2_03_test['SSRT'])
vec_std_right_inhibition_S1_03_S2_03_test=np.std(data_S1_03_S2_03_test['right_inhibition'])
vec_std_accuracy_S1_03_S2_03_test=np.std(data_S1_03_S2_03_test['accuracy'])

#geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_03_train*vec_mean_mean_Pmax_Go_S1_03_S2_03_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_03_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_03_train*vec_mean_mean_Pmax_Hold_S1_03_S2_03_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_03_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_03_train*vec_mean_mean_Pmax_Hold_correct_S1_03_S2_03_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_03_train*vec_mean_mean_Pmax_Hold_total_S1_03_S2_03_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_03_test*vec_mean_mean_Pmax_Go_S1_03_S2_03_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_03_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_03_test*vec_mean_mean_Pmax_Hold_S1_03_S2_03_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_03_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_03_test*vec_mean_mean_Pmax_Hold_correct_S1_03_S2_03_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_03_test*vec_mean_mean_Pmax_Hold_total_S1_03_S2_03_test)

#geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_03_train*vec_mean_mean_reaction_time_Go_S1_03_S2_03_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_03_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_03_train*vec_mean_mean_reaction_time_Hold_S1_03_S2_03_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_03_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_03_train*vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_03_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_03_train*vec_mean_mean_reaction_time_Hold_total_S1_03_S2_03_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_03_test*vec_mean_mean_reaction_time_Go_S1_03_S2_03_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_03_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_03_test*vec_mean_mean_reaction_time_Hold_S1_03_S2_03_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_03_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_03_test*vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_03_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_03_test*vec_mean_mean_reaction_time_Hold_total_S1_03_S2_03_test)

#SEROTONIN S1 = 0.3 and S2 = 0.5
#training
vec_mean_mean_reaction_time_Go_S1_03_S2_05_train=np.mean(data_S1_03_S2_05_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_03_S2_05_train=np.mean(data_S1_03_S2_05_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_05_train=np.mean(data_S1_03_S2_05_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_03_S2_05_train=np.mean(data_S1_03_S2_05_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_03_S2_05_train=np.mean(data_S1_03_S2_05_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_03_S2_05_train=np.mean(data_S1_03_S2_05_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_05_train=np.mean(data_S1_03_S2_05_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_03_S2_05_train=np.mean(data_S1_03_S2_05_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_03_S2_05_train=np.mean(data_S1_03_S2_05_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_03_S2_05_train=np.mean(data_S1_03_S2_05_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_03_S2_05_train=np.mean(data_S1_03_S2_05_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_03_S2_05_train=np.mean(data_S1_03_S2_05_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_03_S2_05_train=np.mean(data_S1_03_S2_05_train['right_inhibition'])
vec_mean_accuracy_S1_03_S2_05_train=np.mean(data_S1_03_S2_05_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_03_S2_05_train=np.std(data_S1_03_S2_05_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_03_S2_05_train=np.std(data_S1_03_S2_05_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_03_S2_05_train=np.std(data_S1_03_S2_05_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_03_S2_05_train=np.std(data_S1_03_S2_05_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_03_S2_05_train=np.std(data_S1_03_S2_05_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_03_S2_05_train=np.std(data_S1_03_S2_05_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_03_S2_05_train=np.std(data_S1_03_S2_05_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_03_S2_05_train=np.std(data_S1_03_S2_05_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_03_S2_05_train=np.std(data_S1_03_S2_05_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_03_S2_05_train=np.std(data_S1_03_S2_05_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_03_S2_05_train=np.std(data_S1_03_S2_05_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_03_S2_05_train=np.std(data_S1_03_S2_05_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_03_S2_05_train=np.std(data_S1_03_S2_05_train['right_inhibition'])
vec_std_accuracy_S1_03_S2_05_train=np.std(data_S1_03_S2_05_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_03_S2_05_test=np.mean(data_S1_03_S2_05_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_03_S2_05_test=np.mean(data_S1_03_S2_05_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_05_test=np.mean(data_S1_03_S2_05_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_03_S2_05_test=np.mean(data_S1_03_S2_05_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_03_S2_05_test=np.mean(data_S1_03_S2_05_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_03_S2_05_test=np.mean(data_S1_03_S2_05_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_05_test=np.mean(data_S1_03_S2_05_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_03_S2_05_test=np.mean(data_S1_03_S2_05_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_03_S2_05_test=np.mean(data_S1_03_S2_05_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_03_S2_05_test=np.mean(data_S1_03_S2_05_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_03_S2_05_test=np.mean(data_S1_03_S2_05_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_03_S2_05_test=np.mean(data_S1_03_S2_05_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_03_S2_05_test=np.mean(data_S1_03_S2_05_test['SSRT'])
vec_mean_right_inhibition_S1_03_S2_05_test=np.mean(data_S1_03_S2_05_test['right_inhibition'])
vec_mean_accuracy_S1_03_S2_05_test=np.mean(data_S1_03_S2_05_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_03_S2_05_test=np.std(data_S1_03_S2_05_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_03_S2_05_test=np.std(data_S1_03_S2_05_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_03_S2_05_test=np.std(data_S1_03_S2_05_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_03_S2_05_test=np.std(data_S1_03_S2_05_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_03_S2_05_test=np.std(data_S1_03_S2_05_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_03_S2_05_test=np.std(data_S1_03_S2_05_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_03_S2_05_test=np.std(data_S1_03_S2_05_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_03_S2_05_test=np.std(data_S1_03_S2_05_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_03_S2_05_test=np.std(data_S1_03_S2_05_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_03_S2_05_test=np.std(data_S1_03_S2_05_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_03_S2_05_test=np.std(data_S1_03_S2_05_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_03_S2_05_test=np.std(data_S1_03_S2_05_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_03_S2_05_test=np.std(data_S1_03_S2_05_test['SSRT'])
vec_std_right_inhibition_S1_03_S2_05_test=np.std(data_S1_03_S2_05_test['right_inhibition'])
vec_std_accuracy_S1_03_S2_05_test=np.std(data_S1_03_S2_05_test['accuracy'])

#geometric mean max PMC & Pmax
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_05_train*vec_mean_mean_Pmax_Go_S1_03_S2_05_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_03_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_05_train*vec_mean_mean_Pmax_Hold_S1_03_S2_05_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_03_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_05_train*vec_mean_mean_Pmax_Hold_correct_S1_03_S2_05_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_05_train*vec_mean_mean_Pmax_Hold_total_S1_03_S2_05_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_05_test*vec_mean_mean_Pmax_Go_S1_03_S2_05_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_03_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_05_test*vec_mean_mean_Pmax_Hold_S1_03_S2_05_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_03_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_05_test*vec_mean_mean_Pmax_Hold_correct_S1_03_S2_05_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_05_test*vec_mean_mean_Pmax_Hold_total_S1_03_S2_05_test)

#geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_05_train*vec_mean_mean_reaction_time_Go_S1_03_S2_05_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_03_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_05_train*vec_mean_mean_reaction_time_Hold_S1_03_S2_05_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_03_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_05_train*vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_05_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_05_train*vec_mean_mean_reaction_time_Hold_total_S1_03_S2_05_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_05_test*vec_mean_mean_reaction_time_Go_S1_03_S2_05_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_03_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_05_test*vec_mean_mean_reaction_time_Hold_S1_03_S2_05_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_03_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_05_test*vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_05_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_05_test*vec_mean_mean_reaction_time_Hold_total_S1_03_S2_05_test)

#SEROTONIN S1 = 0.3 and S2 = 0.7
#training
vec_mean_mean_reaction_time_Go_S1_03_S2_07_train=np.mean(data_S1_03_S2_07_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_03_S2_07_train=np.mean(data_S1_03_S2_07_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_07_train=np.mean(data_S1_03_S2_07_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_03_S2_07_train=np.mean(data_S1_03_S2_07_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_03_S2_07_train=np.mean(data_S1_03_S2_07_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_03_S2_07_train=np.mean(data_S1_03_S2_07_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_07_train=np.mean(data_S1_03_S2_07_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_03_S2_07_train=np.mean(data_S1_03_S2_07_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_03_S2_07_train=np.mean(data_S1_03_S2_07_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_03_S2_07_train=np.mean(data_S1_03_S2_07_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_03_S2_07_train=np.mean(data_S1_03_S2_07_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_03_S2_07_train=np.mean(data_S1_03_S2_07_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_03_S2_07_train=np.mean(data_S1_03_S2_07_train['right_inhibition'])
vec_mean_accuracy_S1_03_S2_07_train=np.mean(data_S1_03_S2_07_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_03_S2_07_train=np.std(data_S1_03_S2_07_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_03_S2_07_train=np.std(data_S1_03_S2_07_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_03_S2_07_train=np.std(data_S1_03_S2_07_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_03_S2_07_train=np.std(data_S1_03_S2_07_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_03_S2_07_train=np.std(data_S1_03_S2_07_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_03_S2_07_train=np.std(data_S1_03_S2_07_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_03_S2_07_train=np.std(data_S1_03_S2_07_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_03_S2_07_train=np.std(data_S1_03_S2_07_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_03_S2_07_train=np.std(data_S1_03_S2_07_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_03_S2_07_train=np.std(data_S1_03_S2_07_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_03_S2_07_train=np.std(data_S1_03_S2_07_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_03_S2_07_train=np.std(data_S1_03_S2_07_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_03_S2_07_train=np.std(data_S1_03_S2_07_train['right_inhibition'])
vec_std_accuracy_S1_03_S2_07_train=np.std(data_S1_03_S2_07_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_03_S2_07_test=np.mean(data_S1_03_S2_07_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_03_S2_07_test=np.mean(data_S1_03_S2_07_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_07_test=np.mean(data_S1_03_S2_07_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_03_S2_07_test=np.mean(data_S1_03_S2_07_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_03_S2_07_test=np.mean(data_S1_03_S2_07_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_03_S2_07_test=np.mean(data_S1_03_S2_07_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_07_test=np.mean(data_S1_03_S2_07_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_03_S2_07_test=np.mean(data_S1_03_S2_07_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_03_S2_07_test=np.mean(data_S1_03_S2_07_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_03_S2_07_test=np.mean(data_S1_03_S2_07_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_03_S2_07_test=np.mean(data_S1_03_S2_07_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_03_S2_07_test=np.mean(data_S1_03_S2_07_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_03_S2_07_test=np.mean(data_S1_03_S2_07_test['SSRT'])
vec_mean_right_inhibition_S1_03_S2_07_test=np.mean(data_S1_03_S2_07_test['right_inhibition'])
vec_mean_accuracy_S1_03_S2_07_test=np.mean(data_S1_03_S2_07_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_03_S2_07_test=np.std(data_S1_03_S2_07_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_03_S2_07_test=np.std(data_S1_03_S2_07_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_03_S2_07_test=np.std(data_S1_03_S2_07_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_03_S2_07_test=np.std(data_S1_03_S2_07_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_03_S2_07_test=np.std(data_S1_03_S2_07_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_03_S2_07_test=np.std(data_S1_03_S2_07_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_03_S2_07_test=np.std(data_S1_03_S2_07_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_03_S2_07_test=np.std(data_S1_03_S2_07_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_03_S2_07_test=np.std(data_S1_03_S2_07_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_03_S2_07_test=np.std(data_S1_03_S2_07_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_03_S2_07_test=np.std(data_S1_03_S2_07_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_03_S2_07_test=np.std(data_S1_03_S2_07_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_03_S2_07_test=np.std(data_S1_03_S2_07_test['SSRT'])
vec_std_right_inhibition_S1_03_S2_07_test=np.std(data_S1_03_S2_07_test['right_inhibition'])
vec_std_accuracy_S1_03_S2_07_test=np.std(data_S1_03_S2_07_test['accuracy'])

#geometric mean max PMC & Pmax 
#training  
vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_07_train*vec_mean_mean_Pmax_Go_S1_03_S2_07_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_03_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_07_train*vec_mean_mean_Pmax_Hold_S1_03_S2_07_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_03_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_07_train*vec_mean_mean_Pmax_Hold_correct_S1_03_S2_07_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_07_train*vec_mean_mean_Pmax_Hold_total_S1_03_S2_07_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_07_test*vec_mean_mean_Pmax_Go_S1_03_S2_07_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_03_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_07_test*vec_mean_mean_Pmax_Hold_S1_03_S2_07_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_03_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_07_test*vec_mean_mean_Pmax_Hold_correct_S1_03_S2_07_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_07_test*vec_mean_mean_Pmax_Hold_total_S1_03_S2_07_test)

#geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_07_train*vec_mean_mean_reaction_time_Go_S1_03_S2_07_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_03_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_07_train*vec_mean_mean_reaction_time_Hold_S1_03_S2_07_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_03_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_07_train*vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_07_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_07_train*vec_mean_mean_reaction_time_Hold_total_S1_03_S2_07_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_07_test*vec_mean_mean_reaction_time_Go_S1_03_S2_07_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_03_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_07_test*vec_mean_mean_reaction_time_Hold_S1_03_S2_07_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_03_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_07_test*vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_07_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_07_test*vec_mean_mean_reaction_time_Hold_total_S1_03_S2_07_test)

#SEROTONIN S1 = 0.3 and S2 = 0.9
#training
vec_mean_mean_reaction_time_Go_S1_03_S2_09_train=np.mean(data_S1_03_S2_09_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_03_S2_09_train=np.mean(data_S1_03_S2_09_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_09_train=np.mean(data_S1_03_S2_09_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_03_S2_09_train=np.mean(data_S1_03_S2_09_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_03_S2_09_train=np.mean(data_S1_03_S2_09_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_03_S2_09_train=np.mean(data_S1_03_S2_09_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_09_train=np.mean(data_S1_03_S2_09_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_03_S2_09_train=np.mean(data_S1_03_S2_09_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_03_S2_09_train=np.mean(data_S1_03_S2_09_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_03_S2_09_train=np.mean(data_S1_03_S2_09_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_03_S2_09_train=np.mean(data_S1_03_S2_09_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_03_S2_09_train=np.mean(data_S1_03_S2_09_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_03_S2_09_train=np.mean(data_S1_03_S2_09_train['right_inhibition'])
vec_mean_accuracy_S1_03_S2_09_train=np.mean(data_S1_03_S2_09_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_03_S2_09_train=np.std(data_S1_03_S2_09_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_03_S2_09_train=np.std(data_S1_03_S2_09_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_03_S2_09_train=np.std(data_S1_03_S2_09_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_03_S2_09_train=np.std(data_S1_03_S2_09_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_03_S2_09_train=np.std(data_S1_03_S2_09_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_03_S2_09_train=np.std(data_S1_03_S2_09_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_03_S2_09_train=np.std(data_S1_03_S2_09_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_03_S2_09_train=np.std(data_S1_03_S2_09_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_03_S2_09_train=np.std(data_S1_03_S2_09_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_03_S2_09_train=np.std(data_S1_03_S2_09_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_03_S2_09_train=np.std(data_S1_03_S2_09_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_03_S2_09_train=np.std(data_S1_03_S2_09_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_03_S2_09_train=np.std(data_S1_03_S2_09_train['right_inhibition'])
vec_std_accuracy_S1_03_S2_09_train=np.std(data_S1_03_S2_09_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_03_S2_09_test=np.mean(data_S1_03_S2_09_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_03_S2_09_test=np.mean(data_S1_03_S2_09_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_09_test=np.mean(data_S1_03_S2_09_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_03_S2_09_test=np.mean(data_S1_03_S2_09_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_03_S2_09_test=np.mean(data_S1_03_S2_09_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_03_S2_09_test=np.mean(data_S1_03_S2_09_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_09_test=np.mean(data_S1_03_S2_09_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_03_S2_09_test=np.mean(data_S1_03_S2_09_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_03_S2_09_test=np.mean(data_S1_03_S2_09_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_03_S2_09_test=np.mean(data_S1_03_S2_09_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_03_S2_09_test=np.mean(data_S1_03_S2_09_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_03_S2_09_test=np.mean(data_S1_03_S2_09_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_03_S2_09_test=np.mean(data_S1_03_S2_09_test['SSRT'])
vec_mean_right_inhibition_S1_03_S2_09_test=np.mean(data_S1_03_S2_09_test['right_inhibition'])
vec_mean_accuracy_S1_03_S2_09_test=np.mean(data_S1_03_S2_09_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_03_S2_09_test=np.std(data_S1_03_S2_09_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_03_S2_09_test=np.std(data_S1_03_S2_09_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_03_S2_09_test=np.std(data_S1_03_S2_09_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_03_S2_09_test=np.std(data_S1_03_S2_09_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_03_S2_09_test=np.std(data_S1_03_S2_09_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_03_S2_09_test=np.std(data_S1_03_S2_09_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_03_S2_09_test=np.std(data_S1_03_S2_09_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_03_S2_09_test=np.std(data_S1_03_S2_09_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_03_S2_09_test=np.std(data_S1_03_S2_09_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_03_S2_09_test=np.std(data_S1_03_S2_09_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_03_S2_09_test=np.std(data_S1_03_S2_09_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_03_S2_09_test=np.std(data_S1_03_S2_09_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_03_S2_09_test=np.std(data_S1_03_S2_09_test['SSRT'])
vec_std_right_inhibition_S1_03_S2_09_test=np.std(data_S1_03_S2_09_test['right_inhibition'])
vec_std_accuracy_S1_03_S2_09_test=np.std(data_S1_03_S2_09_test['accuracy'])

#geometric mean max PMC & Pmax
#training 
vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_09_train*vec_mean_mean_Pmax_Go_S1_03_S2_09_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_03_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_09_train*vec_mean_mean_Pmax_Hold_S1_03_S2_09_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_03_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_09_train*vec_mean_mean_Pmax_Hold_correct_S1_03_S2_09_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_09_train*vec_mean_mean_Pmax_Hold_total_S1_03_S2_09_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_09_test*vec_mean_mean_Pmax_Go_S1_03_S2_09_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_03_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_09_test*vec_mean_mean_Pmax_Hold_S1_03_S2_09_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_03_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_09_test*vec_mean_mean_Pmax_Hold_correct_S1_03_S2_09_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_09_test*vec_mean_mean_Pmax_Hold_total_S1_03_S2_09_test)

#geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_09_train*vec_mean_mean_reaction_time_Go_S1_03_S2_09_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_03_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_09_train*vec_mean_mean_reaction_time_Hold_S1_03_S2_09_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_03_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_09_train*vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_09_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_09_train*vec_mean_mean_reaction_time_Hold_total_S1_03_S2_09_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_03_S2_09_test*vec_mean_mean_reaction_time_Go_S1_03_S2_09_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_03_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_03_S2_09_test*vec_mean_mean_reaction_time_Hold_S1_03_S2_09_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_03_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_09_test*vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_09_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_03_S2_09_test*vec_mean_mean_reaction_time_Hold_total_S1_03_S2_09_test)

#SEROTONIN S1 = 0.5 and S2 = 0.1
#training
vec_mean_mean_reaction_time_Go_S1_05_S2_01_train=np.mean(data_S1_05_S2_01_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_05_S2_01_train=np.mean(data_S1_05_S2_01_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_01_train=np.mean(data_S1_05_S2_01_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_05_S2_01_train=np.mean(data_S1_05_S2_01_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_05_S2_01_train=np.mean(data_S1_05_S2_01_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_05_S2_01_train=np.mean(data_S1_05_S2_01_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_01_train=np.mean(data_S1_05_S2_01_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_05_S2_01_train=np.mean(data_S1_05_S2_01_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_05_S2_01_train=np.mean(data_S1_05_S2_01_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_05_S2_01_train=np.mean(data_S1_05_S2_01_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_05_S2_01_train=np.mean(data_S1_05_S2_01_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_05_S2_01_train=np.mean(data_S1_05_S2_01_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_05_S2_01_train=np.mean(data_S1_05_S2_01_train['right_inhibition'])
vec_mean_accuracy_S1_05_S2_01_train=np.mean(data_S1_05_S2_01_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_05_S2_01_train=np.std(data_S1_05_S2_01_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_05_S2_01_train=np.std(data_S1_05_S2_01_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_05_S2_01_train=np.std(data_S1_05_S2_01_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_05_S2_01_train=np.std(data_S1_05_S2_01_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_05_S2_01_train=np.std(data_S1_05_S2_01_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_05_S2_01_train=np.std(data_S1_05_S2_01_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_05_S2_01_train=np.std(data_S1_05_S2_01_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_05_S2_01_train=np.std(data_S1_05_S2_01_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_05_S2_01_train=np.std(data_S1_05_S2_01_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_05_S2_01_train=np.std(data_S1_05_S2_01_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_05_S2_01_train=np.std(data_S1_05_S2_01_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_05_S2_01_train=np.std(data_S1_05_S2_01_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_05_S2_01_train=np.std(data_S1_05_S2_01_train['right_inhibition'])
vec_std_accuracy_S1_05_S2_01_train=np.std(data_S1_05_S2_01_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_05_S2_01_test=np.mean(data_S1_05_S2_01_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_05_S2_01_test=np.mean(data_S1_05_S2_01_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_01_test=np.mean(data_S1_05_S2_01_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_05_S2_01_test=np.mean(data_S1_05_S2_01_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_05_S2_01_test=np.mean(data_S1_05_S2_01_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_05_S2_01_test=np.mean(data_S1_05_S2_01_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_01_test=np.mean(data_S1_05_S2_01_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_05_S2_01_test=np.mean(data_S1_05_S2_01_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_05_S2_01_test=np.mean(data_S1_05_S2_01_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_05_S2_01_test=np.mean(data_S1_05_S2_01_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_05_S2_01_test=np.mean(data_S1_05_S2_01_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_05_S2_01_test=np.mean(data_S1_05_S2_01_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_05_S2_01_test=np.mean(data_S1_05_S2_01_test['SSRT'])
vec_mean_right_inhibition_S1_05_S2_01_test=np.mean(data_S1_05_S2_01_test['right_inhibition'])
vec_mean_accuracy_S1_05_S2_01_test=np.mean(data_S1_05_S2_01_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_05_S2_01_test=np.std(data_S1_05_S2_01_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_05_S2_01_test=np.std(data_S1_05_S2_01_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_05_S2_01_test=np.std(data_S1_05_S2_01_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_05_S2_01_test=np.std(data_S1_05_S2_01_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_05_S2_01_test=np.std(data_S1_05_S2_01_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_05_S2_01_test=np.std(data_S1_05_S2_01_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_05_S2_01_test=np.std(data_S1_05_S2_01_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_05_S2_01_test=np.std(data_S1_05_S2_01_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_05_S2_01_test=np.std(data_S1_05_S2_01_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_05_S2_01_test=np.std(data_S1_05_S2_01_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_05_S2_01_test=np.std(data_S1_05_S2_01_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_05_S2_01_test=np.std(data_S1_05_S2_01_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_05_S2_01_test=np.std(data_S1_05_S2_01_test['SSRT'])
vec_std_right_inhibition_S1_05_S2_01_test=np.std(data_S1_05_S2_01_test['right_inhibition'])
vec_std_accuracy_S1_05_S2_01_test=np.std(data_S1_05_S2_01_test['accuracy'])

#geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_01_train*vec_mean_mean_Pmax_Go_S1_05_S2_01_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_05_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_01_train*vec_mean_mean_Pmax_Hold_S1_05_S2_01_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_05_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_01_train*vec_mean_mean_Pmax_Hold_correct_S1_05_S2_01_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_01_train*vec_mean_mean_Pmax_Hold_total_S1_05_S2_01_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_01_test*vec_mean_mean_Pmax_Go_S1_05_S2_01_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_05_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_01_test*vec_mean_mean_Pmax_Hold_S1_05_S2_01_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_05_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_01_test*vec_mean_mean_Pmax_Hold_correct_S1_05_S2_01_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_01_test*vec_mean_mean_Pmax_Hold_total_S1_05_S2_01_test)

#geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_01_train*vec_mean_mean_reaction_time_Go_S1_05_S2_01_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_05_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_01_train*vec_mean_mean_reaction_time_Hold_S1_05_S2_01_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_05_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_01_train*vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_01_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_01_train*vec_mean_mean_reaction_time_Hold_total_S1_05_S2_01_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_01_test*vec_mean_mean_reaction_time_Go_S1_05_S2_01_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_05_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_01_test*vec_mean_mean_reaction_time_Hold_S1_05_S2_01_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_05_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_01_test*vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_01_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_01_test*vec_mean_mean_reaction_time_Hold_total_S1_05_S2_01_test)

#SEROTONIN S1 = 0.5 and S2 = 0.3
#training
vec_mean_mean_reaction_time_Go_S1_05_S2_03_train=np.mean(data_S1_05_S2_03_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_05_S2_03_train=np.mean(data_S1_05_S2_03_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_03_train=np.mean(data_S1_05_S2_03_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_05_S2_03_train=np.mean(data_S1_05_S2_03_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_05_S2_03_train=np.mean(data_S1_05_S2_03_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_05_S2_03_train=np.mean(data_S1_05_S2_03_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_03_train=np.mean(data_S1_05_S2_03_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_05_S2_03_train=np.mean(data_S1_05_S2_03_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_05_S2_03_train=np.mean(data_S1_05_S2_03_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_05_S2_03_train=np.mean(data_S1_05_S2_03_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_05_S2_03_train=np.mean(data_S1_05_S2_03_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_05_S2_03_train=np.mean(data_S1_05_S2_03_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_05_S2_03_train=np.mean(data_S1_05_S2_03_train['right_inhibition'])
vec_mean_accuracy_S1_05_S2_03_train=np.mean(data_S1_05_S2_03_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_05_S2_03_train=np.std(data_S1_05_S2_03_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_05_S2_03_train=np.std(data_S1_05_S2_03_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_05_S2_03_train=np.std(data_S1_05_S2_03_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_05_S2_03_train=np.std(data_S1_05_S2_03_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_05_S2_03_train=np.std(data_S1_05_S2_03_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_05_S2_03_train=np.std(data_S1_05_S2_03_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_05_S2_03_train=np.std(data_S1_05_S2_03_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_05_S2_03_train=np.std(data_S1_05_S2_03_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_05_S2_03_train=np.std(data_S1_05_S2_03_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_05_S2_03_train=np.std(data_S1_05_S2_03_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_05_S2_03_train=np.std(data_S1_05_S2_03_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_05_S2_03_train=np.std(data_S1_05_S2_03_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_05_S2_03_train=np.std(data_S1_05_S2_03_train['right_inhibition'])
vec_std_accuracy_S1_05_S2_03_train=np.std(data_S1_05_S2_03_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_05_S2_03_test=np.mean(data_S1_05_S2_03_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_05_S2_03_test=np.mean(data_S1_05_S2_03_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_03_test=np.mean(data_S1_05_S2_03_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_05_S2_03_test=np.mean(data_S1_05_S2_03_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_05_S2_03_test=np.mean(data_S1_05_S2_03_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_05_S2_03_test=np.mean(data_S1_05_S2_03_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_03_test=np.mean(data_S1_05_S2_03_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_05_S2_03_test=np.mean(data_S1_05_S2_03_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_05_S2_03_test=np.mean(data_S1_05_S2_03_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_05_S2_03_test=np.mean(data_S1_05_S2_03_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_05_S2_03_test=np.mean(data_S1_05_S2_03_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_05_S2_03_test=np.mean(data_S1_05_S2_03_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_05_S2_03_test=np.mean(data_S1_05_S2_03_test['SSRT'])
vec_mean_right_inhibition_S1_05_S2_03_test=np.mean(data_S1_05_S2_03_test['right_inhibition'])
vec_mean_accuracy_S1_05_S2_03_test=np.mean(data_S1_05_S2_03_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_05_S2_03_test=np.std(data_S1_05_S2_03_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_05_S2_03_test=np.std(data_S1_05_S2_03_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_05_S2_03_test=np.std(data_S1_05_S2_03_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_05_S2_03_test=np.std(data_S1_05_S2_03_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_05_S2_03_test=np.std(data_S1_05_S2_03_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_05_S2_03_test=np.std(data_S1_05_S2_03_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_05_S2_03_test=np.std(data_S1_05_S2_03_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_05_S2_03_test=np.std(data_S1_05_S2_03_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_05_S2_03_test=np.std(data_S1_05_S2_03_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_05_S2_03_test=np.std(data_S1_05_S2_03_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_05_S2_03_test=np.std(data_S1_05_S2_03_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_05_S2_03_test=np.std(data_S1_05_S2_03_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_05_S2_03_test=np.std(data_S1_05_S2_03_test['SSRT'])
vec_std_right_inhibition_S1_05_S2_03_test=np.std(data_S1_05_S2_03_test['right_inhibition'])
vec_std_accuracy_S1_05_S2_03_test=np.std(data_S1_05_S2_03_test['accuracy'])

#geometric mean max PMC & Pmax 
#training 
vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_03_train*vec_mean_mean_Pmax_Go_S1_05_S2_03_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_05_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_03_train*vec_mean_mean_Pmax_Hold_S1_05_S2_03_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_05_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_03_train*vec_mean_mean_Pmax_Hold_correct_S1_05_S2_03_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_03_train*vec_mean_mean_Pmax_Hold_total_S1_05_S2_03_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_03_test*vec_mean_mean_Pmax_Go_S1_05_S2_03_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_05_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_03_test*vec_mean_mean_Pmax_Hold_S1_05_S2_03_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_05_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_03_test*vec_mean_mean_Pmax_Hold_correct_S1_05_S2_03_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_03_test*vec_mean_mean_Pmax_Hold_total_S1_05_S2_03_test)

#geometric mean max PMC & RT 
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_03_train*vec_mean_mean_reaction_time_Go_S1_05_S2_03_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_05_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_03_train*vec_mean_mean_reaction_time_Hold_S1_05_S2_03_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_05_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_03_train*vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_03_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_03_train*vec_mean_mean_reaction_time_Hold_total_S1_05_S2_03_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_03_test*vec_mean_mean_reaction_time_Go_S1_05_S2_03_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_05_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_03_test*vec_mean_mean_reaction_time_Hold_S1_05_S2_03_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_05_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_03_test*vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_03_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_03_test*vec_mean_mean_reaction_time_Hold_total_S1_05_S2_03_test)

#SEROTONIN S1 = 0.5 and S2 = 0.5
#training
vec_mean_mean_reaction_time_Go_S1_05_S2_05_train=np.mean(data_S1_05_S2_05_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_05_S2_05_train=np.mean(data_S1_05_S2_05_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_05_train=np.mean(data_S1_05_S2_05_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_05_S2_05_train=np.mean(data_S1_05_S2_05_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_05_S2_05_train=np.mean(data_S1_05_S2_05_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_05_S2_05_train=np.mean(data_S1_05_S2_05_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_05_train=np.mean(data_S1_05_S2_05_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_05_S2_05_train=np.mean(data_S1_05_S2_05_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_05_S2_05_train=np.mean(data_S1_05_S2_05_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_05_S2_05_train=np.mean(data_S1_05_S2_05_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_05_S2_05_train=np.mean(data_S1_05_S2_05_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_05_S2_05_train=np.mean(data_S1_05_S2_05_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_05_S2_05_train=np.mean(data_S1_05_S2_05_train['right_inhibition'])
vec_mean_accuracy_S1_05_S2_05_train=np.mean(data_S1_05_S2_05_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_05_S2_05_train=np.std(data_S1_05_S2_05_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_05_S2_05_train=np.std(data_S1_05_S2_05_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_05_S2_05_train=np.std(data_S1_05_S2_05_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_05_S2_05_train=np.std(data_S1_05_S2_05_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_05_S2_05_train=np.std(data_S1_05_S2_05_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_05_S2_05_train=np.std(data_S1_05_S2_05_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_05_S2_05_train=np.std(data_S1_05_S2_05_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_05_S2_05_train=np.std(data_S1_05_S2_05_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_05_S2_05_train=np.std(data_S1_05_S2_05_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_05_S2_05_train=np.std(data_S1_05_S2_05_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_05_S2_05_train=np.std(data_S1_05_S2_05_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_05_S2_05_train=np.std(data_S1_05_S2_05_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_05_S2_05_train=np.std(data_S1_05_S2_05_train['right_inhibition'])
vec_std_accuracy_S1_05_S2_05_train=np.std(data_S1_05_S2_05_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_05_S2_05_test=np.mean(data_S1_05_S2_05_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_05_S2_05_test=np.mean(data_S1_05_S2_05_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_05_test=np.mean(data_S1_05_S2_05_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_05_S2_05_test=np.mean(data_S1_05_S2_05_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_05_S2_05_test=np.mean(data_S1_05_S2_05_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_05_S2_05_test=np.mean(data_S1_05_S2_05_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_05_test=np.mean(data_S1_05_S2_05_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_05_S2_05_test=np.mean(data_S1_05_S2_05_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_05_S2_05_test=np.mean(data_S1_05_S2_05_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_05_S2_05_test=np.mean(data_S1_05_S2_05_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_05_S2_05_test=np.mean(data_S1_05_S2_05_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_05_S2_05_test=np.mean(data_S1_05_S2_05_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_05_S2_05_test=np.mean(data_S1_05_S2_05_test['SSRT'])
vec_mean_right_inhibition_S1_05_S2_05_test=np.mean(data_S1_05_S2_05_test['right_inhibition'])
vec_mean_accuracy_S1_05_S2_05_test=np.mean(data_S1_05_S2_05_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_05_S2_05_test=np.std(data_S1_05_S2_05_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_05_S2_05_test=np.std(data_S1_05_S2_05_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_05_S2_05_test=np.std(data_S1_05_S2_05_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_05_S2_05_test=np.std(data_S1_05_S2_05_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_05_S2_05_test=np.std(data_S1_05_S2_05_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_05_S2_05_test=np.std(data_S1_05_S2_05_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_05_S2_05_test=np.std(data_S1_05_S2_05_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_05_S2_05_test=np.std(data_S1_05_S2_05_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_05_S2_05_test=np.std(data_S1_05_S2_05_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_05_S2_05_test=np.std(data_S1_05_S2_05_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_05_S2_05_test=np.std(data_S1_05_S2_05_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_05_S2_05_test=np.std(data_S1_05_S2_05_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_05_S2_05_test=np.std(data_S1_05_S2_05_test['SSRT'])
vec_std_right_inhibition_S1_05_S2_05_test=np.std(data_S1_05_S2_05_test['right_inhibition'])
vec_std_accuracy_S1_05_S2_05_test=np.std(data_S1_05_S2_05_test['accuracy'])

#geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_05_train*vec_mean_mean_Pmax_Go_S1_05_S2_05_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_05_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_05_train*vec_mean_mean_Pmax_Hold_S1_05_S2_05_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_05_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_05_train*vec_mean_mean_Pmax_Hold_correct_S1_05_S2_05_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_05_train*vec_mean_mean_Pmax_Hold_total_S1_05_S2_05_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_05_test*vec_mean_mean_Pmax_Go_S1_05_S2_05_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_05_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_05_test*vec_mean_mean_Pmax_Hold_S1_05_S2_05_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_05_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_05_test*vec_mean_mean_Pmax_Hold_correct_S1_05_S2_05_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_05_test*vec_mean_mean_Pmax_Hold_total_S1_05_S2_05_test)

#geometric mean max PMC & RT
#training 
vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_05_train*vec_mean_mean_reaction_time_Go_S1_05_S2_05_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_05_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_05_train*vec_mean_mean_reaction_time_Hold_S1_05_S2_05_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_05_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_05_train*vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_05_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_05_train*vec_mean_mean_reaction_time_Hold_total_S1_05_S2_05_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_05_test*vec_mean_mean_reaction_time_Go_S1_05_S2_05_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_05_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_05_test*vec_mean_mean_reaction_time_Hold_S1_05_S2_05_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_05_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_05_test*vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_05_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_05_test*vec_mean_mean_reaction_time_Hold_total_S1_05_S2_05_test)

#SEROTONIN S1 = 0.5 and S2 = 0.7
#training
vec_mean_mean_reaction_time_Go_S1_05_S2_07_train=np.mean(data_S1_05_S2_07_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_05_S2_07_train=np.mean(data_S1_05_S2_07_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_07_train=np.mean(data_S1_05_S2_07_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_05_S2_07_train=np.mean(data_S1_05_S2_07_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_05_S2_07_train=np.mean(data_S1_05_S2_07_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_05_S2_07_train=np.mean(data_S1_05_S2_07_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_07_train=np.mean(data_S1_05_S2_07_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_05_S2_07_train=np.mean(data_S1_05_S2_07_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_05_S2_07_train=np.mean(data_S1_05_S2_07_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_05_S2_07_train=np.mean(data_S1_05_S2_07_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_05_S2_07_train=np.mean(data_S1_05_S2_07_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_05_S2_07_train=np.mean(data_S1_05_S2_07_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_05_S2_07_train=np.mean(data_S1_05_S2_07_train['right_inhibition'])
vec_mean_accuracy_S1_05_S2_07_train=np.mean(data_S1_05_S2_07_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_05_S2_07_train=np.std(data_S1_05_S2_07_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_05_S2_07_train=np.std(data_S1_05_S2_07_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_05_S2_07_train=np.std(data_S1_05_S2_07_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_05_S2_07_train=np.std(data_S1_05_S2_07_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_05_S2_07_train=np.std(data_S1_05_S2_07_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_05_S2_07_train=np.std(data_S1_05_S2_07_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_05_S2_07_train=np.std(data_S1_05_S2_07_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_05_S2_07_train=np.std(data_S1_05_S2_07_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_05_S2_07_train=np.std(data_S1_05_S2_07_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_05_S2_07_train=np.std(data_S1_05_S2_07_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_05_S2_07_train=np.std(data_S1_05_S2_07_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_05_S2_07_train=np.std(data_S1_05_S2_07_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_05_S2_07_train=np.std(data_S1_05_S2_07_train['right_inhibition'])
vec_std_accuracy_S1_05_S2_07_train=np.std(data_S1_05_S2_07_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_05_S2_07_test=np.mean(data_S1_05_S2_07_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_05_S2_07_test=np.mean(data_S1_05_S2_07_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_07_test=np.mean(data_S1_05_S2_07_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_05_S2_07_test=np.mean(data_S1_05_S2_07_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_05_S2_07_test=np.mean(data_S1_05_S2_07_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_05_S2_07_test=np.mean(data_S1_05_S2_07_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_07_test=np.mean(data_S1_05_S2_07_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_05_S2_07_test=np.mean(data_S1_05_S2_07_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_05_S2_07_test=np.mean(data_S1_05_S2_07_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_05_S2_07_test=np.mean(data_S1_05_S2_07_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_05_S2_07_test=np.mean(data_S1_05_S2_07_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_05_S2_07_test=np.mean(data_S1_05_S2_07_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_05_S2_07_test=np.mean(data_S1_05_S2_07_test['SSRT'])
vec_mean_right_inhibition_S1_05_S2_07_test=np.mean(data_S1_05_S2_07_test['right_inhibition'])
vec_mean_accuracy_S1_05_S2_07_test=np.mean(data_S1_05_S2_07_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_05_S2_07_test=np.std(data_S1_05_S2_07_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_05_S2_07_test=np.std(data_S1_05_S2_07_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_05_S2_07_test=np.std(data_S1_05_S2_07_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_05_S2_07_test=np.std(data_S1_05_S2_07_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_05_S2_07_test=np.std(data_S1_05_S2_07_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_05_S2_07_test=np.std(data_S1_05_S2_07_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_05_S2_07_test=np.std(data_S1_05_S2_07_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_05_S2_07_test=np.std(data_S1_05_S2_07_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_05_S2_07_test=np.std(data_S1_05_S2_07_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_05_S2_07_test=np.std(data_S1_05_S2_07_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_05_S2_07_test=np.std(data_S1_05_S2_07_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_05_S2_07_test=np.std(data_S1_05_S2_07_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_05_S2_07_test=np.std(data_S1_05_S2_07_test['SSRT'])
vec_std_right_inhibition_S1_05_S2_07_test=np.std(data_S1_05_S2_07_test['right_inhibition'])
vec_std_accuracy_S1_05_S2_07_test=np.std(data_S1_05_S2_07_test['accuracy'])

#geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_07_train*vec_mean_mean_Pmax_Go_S1_05_S2_07_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_05_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_07_train*vec_mean_mean_Pmax_Hold_S1_05_S2_07_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_05_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_07_train*vec_mean_mean_Pmax_Hold_correct_S1_05_S2_07_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_07_train*vec_mean_mean_Pmax_Hold_total_S1_05_S2_07_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_07_test*vec_mean_mean_Pmax_Go_S1_05_S2_07_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_05_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_07_test*vec_mean_mean_Pmax_Hold_S1_05_S2_07_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_05_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_07_test*vec_mean_mean_Pmax_Hold_correct_S1_05_S2_07_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_07_test*vec_mean_mean_Pmax_Hold_total_S1_05_S2_07_test)

#geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_07_train*vec_mean_mean_reaction_time_Go_S1_05_S2_07_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_05_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_07_train*vec_mean_mean_reaction_time_Hold_S1_05_S2_07_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_05_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_07_train*vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_07_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_07_train*vec_mean_mean_reaction_time_Hold_total_S1_05_S2_07_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_07_test*vec_mean_mean_reaction_time_Go_S1_05_S2_07_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_05_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_07_test*vec_mean_mean_reaction_time_Hold_S1_05_S2_07_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_05_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_07_test*vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_07_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_07_test*vec_mean_mean_reaction_time_Hold_total_S1_05_S2_07_test)

#SEROTONIN S1 = 0.5 and S2 = 0.9
#training
vec_mean_mean_reaction_time_Go_S1_05_S2_09_train=np.mean(data_S1_05_S2_09_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_05_S2_09_train=np.mean(data_S1_05_S2_09_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_09_train=np.mean(data_S1_05_S2_09_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_05_S2_09_train=np.mean(data_S1_05_S2_09_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_05_S2_09_train=np.mean(data_S1_05_S2_09_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_05_S2_09_train=np.mean(data_S1_05_S2_09_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_09_train=np.mean(data_S1_05_S2_09_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_05_S2_09_train=np.mean(data_S1_05_S2_09_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_05_S2_09_train=np.mean(data_S1_05_S2_09_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_05_S2_09_train=np.mean(data_S1_05_S2_09_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_05_S2_09_train=np.mean(data_S1_05_S2_09_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_05_S2_09_train=np.mean(data_S1_05_S2_09_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_05_S2_09_train=np.mean(data_S1_05_S2_09_train['right_inhibition'])
vec_mean_accuracy_S1_05_S2_09_train=np.mean(data_S1_05_S2_09_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_05_S2_09_train=np.std(data_S1_05_S2_09_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_05_S2_09_train=np.std(data_S1_05_S2_09_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_05_S2_09_train=np.std(data_S1_05_S2_09_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_05_S2_09_train=np.std(data_S1_05_S2_09_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_05_S2_09_train=np.std(data_S1_05_S2_09_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_05_S2_09_train=np.std(data_S1_05_S2_09_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_05_S2_09_train=np.std(data_S1_05_S2_09_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_05_S2_09_train=np.std(data_S1_05_S2_09_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_05_S2_09_train=np.std(data_S1_05_S2_09_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_05_S2_09_train=np.std(data_S1_05_S2_09_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_05_S2_09_train=np.std(data_S1_05_S2_09_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_05_S2_09_train=np.std(data_S1_05_S2_09_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_05_S2_09_train=np.std(data_S1_05_S2_09_train['right_inhibition'])
vec_std_accuracy_S1_05_S2_09_train=np.std(data_S1_05_S2_09_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_05_S2_09_test=np.mean(data_S1_05_S2_09_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_05_S2_09_test=np.mean(data_S1_05_S2_09_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_09_test=np.mean(data_S1_05_S2_09_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_05_S2_09_test=np.mean(data_S1_05_S2_09_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_05_S2_09_test=np.mean(data_S1_05_S2_09_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_05_S2_09_test=np.mean(data_S1_05_S2_09_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_09_test=np.mean(data_S1_05_S2_09_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_05_S2_09_test=np.mean(data_S1_05_S2_09_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_05_S2_09_test=np.mean(data_S1_05_S2_09_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_05_S2_09_test=np.mean(data_S1_05_S2_09_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_05_S2_09_test=np.mean(data_S1_05_S2_09_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_05_S2_09_test=np.mean(data_S1_05_S2_09_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_05_S2_09_test=np.mean(data_S1_05_S2_09_test['SSRT'])
vec_mean_right_inhibition_S1_05_S2_09_test=np.mean(data_S1_05_S2_09_test['right_inhibition'])
vec_mean_accuracy_S1_05_S2_09_test=np.mean(data_S1_05_S2_09_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_05_S2_09_test=np.std(data_S1_05_S2_09_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_05_S2_09_test=np.std(data_S1_05_S2_09_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_05_S2_09_test=np.std(data_S1_05_S2_09_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_05_S2_09_test=np.std(data_S1_05_S2_09_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_05_S2_09_test=np.std(data_S1_05_S2_09_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_05_S2_09_test=np.std(data_S1_05_S2_09_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_05_S2_09_test=np.std(data_S1_05_S2_09_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_05_S2_09_test=np.std(data_S1_05_S2_09_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_05_S2_09_test=np.std(data_S1_05_S2_09_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_05_S2_09_test=np.std(data_S1_05_S2_09_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_05_S2_09_test=np.std(data_S1_05_S2_09_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_05_S2_09_test=np.std(data_S1_05_S2_09_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_05_S2_09_test=np.std(data_S1_05_S2_09_test['SSRT'])
vec_std_right_inhibition_S1_05_S2_09_test=np.std(data_S1_05_S2_09_test['right_inhibition'])
vec_std_accuracy_S1_05_S2_09_test=np.std(data_S1_05_S2_09_test['accuracy'])

##geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_09_train*vec_mean_mean_Pmax_Go_S1_05_S2_09_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_05_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_09_train*vec_mean_mean_Pmax_Hold_S1_05_S2_09_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_05_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_09_train*vec_mean_mean_Pmax_Hold_correct_S1_05_S2_09_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_09_train*vec_mean_mean_Pmax_Hold_total_S1_05_S2_09_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_09_test*vec_mean_mean_Pmax_Go_S1_05_S2_09_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_05_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_09_test*vec_mean_mean_Pmax_Hold_S1_05_S2_09_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_05_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_09_test*vec_mean_mean_Pmax_Hold_correct_S1_05_S2_09_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_09_test*vec_mean_mean_Pmax_Hold_total_S1_05_S2_09_test)

#geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_09_train*vec_mean_mean_reaction_time_Go_S1_05_S2_09_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_05_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_09_train*vec_mean_mean_reaction_time_Hold_S1_05_S2_09_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_05_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_09_train*vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_09_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_09_train*vec_mean_mean_reaction_time_Hold_total_S1_05_S2_09_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_05_S2_09_test*vec_mean_mean_reaction_time_Go_S1_05_S2_09_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_05_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_05_S2_09_test*vec_mean_mean_reaction_time_Hold_S1_05_S2_09_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_05_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_09_test*vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_09_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_05_S2_09_test*vec_mean_mean_reaction_time_Hold_total_S1_05_S2_09_test)

#SEROTONIN S1 = 0.7 and S2 = 0.1
#training
vec_mean_mean_reaction_time_Go_S1_07_S2_01_train=np.mean(data_S1_07_S2_01_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_07_S2_01_train=np.mean(data_S1_07_S2_01_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_01_train=np.mean(data_S1_07_S2_01_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_07_S2_01_train=np.mean(data_S1_07_S2_01_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_07_S2_01_train=np.mean(data_S1_07_S2_01_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_07_S2_01_train=np.mean(data_S1_07_S2_01_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_01_train=np.mean(data_S1_07_S2_01_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_07_S2_01_train=np.mean(data_S1_07_S2_01_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_07_S2_01_train=np.mean(data_S1_07_S2_01_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_07_S2_01_train=np.mean(data_S1_07_S2_01_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_07_S2_01_train=np.mean(data_S1_07_S2_01_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_07_S2_01_train=np.mean(data_S1_07_S2_01_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_07_S2_01_train=np.mean(data_S1_07_S2_01_train['right_inhibition'])
vec_mean_accuracy_S1_07_S2_01_train=np.mean(data_S1_07_S2_01_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_07_S2_01_train=np.std(data_S1_07_S2_01_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_07_S2_01_train=np.std(data_S1_07_S2_01_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_07_S2_01_train=np.std(data_S1_07_S2_01_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_07_S2_01_train=np.std(data_S1_07_S2_01_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_07_S2_01_train=np.std(data_S1_07_S2_01_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_07_S2_01_train=np.std(data_S1_07_S2_01_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_07_S2_01_train=np.std(data_S1_07_S2_01_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_07_S2_01_train=np.std(data_S1_07_S2_01_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_07_S2_01_train=np.std(data_S1_07_S2_01_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_07_S2_01_train=np.std(data_S1_07_S2_01_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_07_S2_01_train=np.std(data_S1_07_S2_01_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_07_S2_01_train=np.std(data_S1_07_S2_01_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_07_S2_01_train=np.std(data_S1_07_S2_01_train['right_inhibition'])
vec_std_accuracy_S1_07_S2_01_train=np.std(data_S1_07_S2_01_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_07_S2_01_test=np.mean(data_S1_07_S2_01_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_07_S2_01_test=np.mean(data_S1_07_S2_01_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_01_test=np.mean(data_S1_07_S2_01_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_07_S2_01_test=np.mean(data_S1_07_S2_01_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_07_S2_01_test=np.mean(data_S1_07_S2_01_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_07_S2_01_test=np.mean(data_S1_07_S2_01_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_01_test=np.mean(data_S1_07_S2_01_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_07_S2_01_test=np.mean(data_S1_07_S2_01_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_07_S2_01_test=np.mean(data_S1_07_S2_01_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_07_S2_01_test=np.mean(data_S1_07_S2_01_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_07_S2_01_test=np.mean(data_S1_07_S2_01_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_07_S2_01_test=np.mean(data_S1_07_S2_01_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_07_S2_01_test=np.mean(data_S1_07_S2_01_test['SSRT'])
vec_mean_right_inhibition_S1_07_S2_01_test=np.mean(data_S1_07_S2_01_test['right_inhibition'])
vec_mean_accuracy_S1_07_S2_01_test=np.mean(data_S1_07_S2_01_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_07_S2_01_test=np.std(data_S1_07_S2_01_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_07_S2_01_test=np.std(data_S1_07_S2_01_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_07_S2_01_test=np.std(data_S1_07_S2_01_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_07_S2_01_test=np.std(data_S1_07_S2_01_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_07_S2_01_test=np.std(data_S1_07_S2_01_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_07_S2_01_test=np.std(data_S1_07_S2_01_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_07_S2_01_test=np.std(data_S1_07_S2_01_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_07_S2_01_test=np.std(data_S1_07_S2_01_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_07_S2_01_test=np.std(data_S1_07_S2_01_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_07_S2_01_test=np.std(data_S1_07_S2_01_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_07_S2_01_test=np.std(data_S1_07_S2_01_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_07_S2_01_test=np.std(data_S1_07_S2_01_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_07_S2_01_test=np.std(data_S1_07_S2_01_test['SSRT'])
vec_std_right_inhibition_S1_07_S2_01_test=np.std(data_S1_07_S2_01_test['right_inhibition'])
vec_std_accuracy_S1_07_S2_01_test=np.std(data_S1_07_S2_01_test['accuracy'])

##geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_01_train*vec_mean_mean_Pmax_Go_S1_07_S2_01_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_07_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_01_train*vec_mean_mean_Pmax_Hold_S1_07_S2_01_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_07_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_01_train*vec_mean_mean_Pmax_Hold_correct_S1_07_S2_01_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_01_train*vec_mean_mean_Pmax_Hold_total_S1_07_S2_01_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_01_test*vec_mean_mean_Pmax_Go_S1_07_S2_01_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_07_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_01_test*vec_mean_mean_Pmax_Hold_S1_07_S2_01_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_07_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_01_test*vec_mean_mean_Pmax_Hold_correct_S1_07_S2_01_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_01_test*vec_mean_mean_Pmax_Hold_total_S1_07_S2_01_test)

##geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_01_train*vec_mean_mean_reaction_time_Go_S1_07_S2_01_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_07_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_01_train*vec_mean_mean_reaction_time_Hold_S1_07_S2_01_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_07_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_01_train*vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_01_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_01_train*vec_mean_mean_reaction_time_Hold_total_S1_07_S2_01_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_01_test*vec_mean_mean_reaction_time_Go_S1_07_S2_01_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_07_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_01_test*vec_mean_mean_reaction_time_Hold_S1_07_S2_01_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_07_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_01_test*vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_01_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_01_test*vec_mean_mean_reaction_time_Hold_total_S1_07_S2_01_test)

#SEROTONIN S1 = 0.7 and S2 = 0.3
#training
vec_mean_mean_reaction_time_Go_S1_07_S2_03_train=np.mean(data_S1_07_S2_03_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_07_S2_03_train=np.mean(data_S1_07_S2_03_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_03_train=np.mean(data_S1_07_S2_03_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_07_S2_03_train=np.mean(data_S1_07_S2_03_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_07_S2_03_train=np.mean(data_S1_07_S2_03_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_07_S2_03_train=np.mean(data_S1_07_S2_03_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_03_train=np.mean(data_S1_07_S2_03_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_07_S2_03_train=np.mean(data_S1_07_S2_03_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_07_S2_03_train=np.mean(data_S1_07_S2_03_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_07_S2_03_train=np.mean(data_S1_07_S2_03_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_07_S2_03_train=np.mean(data_S1_07_S2_03_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_07_S2_03_train=np.mean(data_S1_07_S2_03_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_07_S2_03_train=np.mean(data_S1_07_S2_03_train['right_inhibition'])
vec_mean_accuracy_S1_07_S2_03_train=np.mean(data_S1_07_S2_03_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_07_S2_03_train=np.std(data_S1_07_S2_03_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_07_S2_03_train=np.std(data_S1_07_S2_03_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_07_S2_03_train=np.std(data_S1_07_S2_03_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_07_S2_03_train=np.std(data_S1_07_S2_03_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_07_S2_03_train=np.std(data_S1_07_S2_03_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_07_S2_03_train=np.std(data_S1_07_S2_03_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_07_S2_03_train=np.std(data_S1_07_S2_03_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_07_S2_03_train=np.std(data_S1_07_S2_03_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_07_S2_03_train=np.std(data_S1_07_S2_03_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_07_S2_03_train=np.std(data_S1_07_S2_03_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_07_S2_03_train=np.std(data_S1_07_S2_03_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_07_S2_03_train=np.std(data_S1_07_S2_03_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_07_S2_03_train=np.std(data_S1_07_S2_03_train['right_inhibition'])
vec_std_accuracy_S1_07_S2_03_train=np.std(data_S1_07_S2_03_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_07_S2_03_test=np.mean(data_S1_07_S2_03_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_07_S2_03_test=np.mean(data_S1_07_S2_03_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_03_test=np.mean(data_S1_07_S2_03_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_07_S2_03_test=np.mean(data_S1_07_S2_03_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_07_S2_03_test=np.mean(data_S1_07_S2_03_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_07_S2_03_test=np.mean(data_S1_07_S2_03_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_03_test=np.mean(data_S1_07_S2_03_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_07_S2_03_test=np.mean(data_S1_07_S2_03_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_07_S2_03_test=np.mean(data_S1_07_S2_03_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_07_S2_03_test=np.mean(data_S1_07_S2_03_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_07_S2_03_test=np.mean(data_S1_07_S2_03_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_07_S2_03_test=np.mean(data_S1_07_S2_03_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_07_S2_03_test=np.mean(data_S1_07_S2_03_test['SSRT'])
vec_mean_right_inhibition_S1_07_S2_03_test=np.mean(data_S1_07_S2_03_test['right_inhibition'])
vec_mean_accuracy_S1_07_S2_03_test=np.mean(data_S1_07_S2_03_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_07_S2_03_test=np.std(data_S1_07_S2_03_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_07_S2_03_test=np.std(data_S1_07_S2_03_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_07_S2_03_test=np.std(data_S1_07_S2_03_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_07_S2_03_test=np.std(data_S1_07_S2_03_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_07_S2_03_test=np.std(data_S1_07_S2_03_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_07_S2_03_test=np.std(data_S1_07_S2_03_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_07_S2_03_test=np.std(data_S1_07_S2_03_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_07_S2_03_test=np.std(data_S1_07_S2_03_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_07_S2_03_test=np.std(data_S1_07_S2_03_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_07_S2_03_test=np.std(data_S1_07_S2_03_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_07_S2_03_test=np.std(data_S1_07_S2_03_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_07_S2_03_test=np.std(data_S1_07_S2_03_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_07_S2_03_test=np.std(data_S1_07_S2_03_test['SSRT'])
vec_std_right_inhibition_S1_07_S2_03_test=np.std(data_S1_07_S2_03_test['right_inhibition'])
vec_std_accuracy_S1_07_S2_03_test=np.std(data_S1_07_S2_03_test['accuracy'])

###geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_03_train*vec_mean_mean_Pmax_Go_S1_07_S2_03_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_07_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_03_train*vec_mean_mean_Pmax_Hold_S1_07_S2_03_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_07_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_03_train*vec_mean_mean_Pmax_Hold_correct_S1_07_S2_03_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_03_train*vec_mean_mean_Pmax_Hold_total_S1_07_S2_03_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_03_test*vec_mean_mean_Pmax_Go_S1_07_S2_03_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_07_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_03_test*vec_mean_mean_Pmax_Hold_S1_07_S2_03_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_07_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_03_test*vec_mean_mean_Pmax_Hold_correct_S1_07_S2_03_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_03_test*vec_mean_mean_Pmax_Hold_total_S1_07_S2_03_test)

##geometric mean max PMC & RT 
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_03_train*vec_mean_mean_reaction_time_Go_S1_07_S2_03_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_07_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_03_train*vec_mean_mean_reaction_time_Hold_S1_07_S2_03_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_07_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_03_train*vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_03_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_03_train*vec_mean_mean_reaction_time_Hold_total_S1_07_S2_03_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_03_test*vec_mean_mean_reaction_time_Go_S1_07_S2_03_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_07_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_03_test*vec_mean_mean_reaction_time_Hold_S1_07_S2_03_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_07_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_03_test*vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_03_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_03_test*vec_mean_mean_reaction_time_Hold_total_S1_07_S2_03_test)

#SEROTONIN S1 = 0.7 and S2 = 0.5
#training
vec_mean_mean_reaction_time_Go_S1_07_S2_05_train=np.mean(data_S1_07_S2_05_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_07_S2_05_train=np.mean(data_S1_07_S2_05_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_05_train=np.mean(data_S1_07_S2_05_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_07_S2_05_train=np.mean(data_S1_07_S2_05_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_07_S2_05_train=np.mean(data_S1_07_S2_05_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_07_S2_05_train=np.mean(data_S1_07_S2_05_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_05_train=np.mean(data_S1_07_S2_05_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_07_S2_05_train=np.mean(data_S1_07_S2_05_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_07_S2_05_train=np.mean(data_S1_07_S2_05_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_07_S2_05_train=np.mean(data_S1_07_S2_05_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_07_S2_05_train=np.mean(data_S1_07_S2_05_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_07_S2_05_train=np.mean(data_S1_07_S2_05_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_07_S2_05_train=np.mean(data_S1_07_S2_05_train['right_inhibition'])
vec_mean_accuracy_S1_07_S2_05_train=np.mean(data_S1_07_S2_05_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_07_S2_05_train=np.std(data_S1_07_S2_05_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_07_S2_05_train=np.std(data_S1_07_S2_05_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_07_S2_05_train=np.std(data_S1_07_S2_05_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_07_S2_05_train=np.std(data_S1_07_S2_05_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_07_S2_05_train=np.std(data_S1_07_S2_05_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_07_S2_05_train=np.std(data_S1_07_S2_05_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_07_S2_05_train=np.std(data_S1_07_S2_05_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_07_S2_05_train=np.std(data_S1_07_S2_05_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_07_S2_05_train=np.std(data_S1_07_S2_05_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_07_S2_05_train=np.std(data_S1_07_S2_05_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_07_S2_05_train=np.std(data_S1_07_S2_05_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_07_S2_05_train=np.std(data_S1_07_S2_05_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_07_S2_05_train=np.std(data_S1_07_S2_05_train['right_inhibition'])
vec_std_accuracy_S1_07_S2_05_train=np.std(data_S1_07_S2_05_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_07_S2_05_test=np.mean(data_S1_07_S2_05_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_07_S2_05_test=np.mean(data_S1_07_S2_05_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_05_test=np.mean(data_S1_07_S2_05_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_07_S2_05_test=np.mean(data_S1_07_S2_05_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_07_S2_05_test=np.mean(data_S1_07_S2_05_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_07_S2_05_test=np.mean(data_S1_07_S2_05_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_05_test=np.mean(data_S1_07_S2_05_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_07_S2_05_test=np.mean(data_S1_07_S2_05_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_07_S2_05_test=np.mean(data_S1_07_S2_05_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_07_S2_05_test=np.mean(data_S1_07_S2_05_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_07_S2_05_test=np.mean(data_S1_07_S2_05_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_07_S2_05_test=np.mean(data_S1_07_S2_05_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_07_S2_05_test=np.mean(data_S1_07_S2_05_test['SSRT'])
vec_mean_right_inhibition_S1_07_S2_05_test=np.mean(data_S1_07_S2_05_test['right_inhibition'])
vec_mean_accuracy_S1_07_S2_05_test=np.mean(data_S1_07_S2_05_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_07_S2_05_test=np.std(data_S1_07_S2_05_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_07_S2_05_test=np.std(data_S1_07_S2_05_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_07_S2_05_test=np.std(data_S1_07_S2_05_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_07_S2_05_test=np.std(data_S1_07_S2_05_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_07_S2_05_test=np.std(data_S1_07_S2_05_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_07_S2_05_test=np.std(data_S1_07_S2_05_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_07_S2_05_test=np.std(data_S1_07_S2_05_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_07_S2_05_test=np.std(data_S1_07_S2_05_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_07_S2_05_test=np.std(data_S1_07_S2_05_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_07_S2_05_test=np.std(data_S1_07_S2_05_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_07_S2_05_test=np.std(data_S1_07_S2_05_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_07_S2_05_test=np.std(data_S1_07_S2_05_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_07_S2_05_test=np.std(data_S1_07_S2_05_test['SSRT'])
vec_std_right_inhibition_S1_07_S2_05_test=np.std(data_S1_07_S2_05_test['right_inhibition'])
vec_std_accuracy_S1_07_S2_05_test=np.std(data_S1_07_S2_05_test['accuracy'])

##geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_05_train*vec_mean_mean_Pmax_Go_S1_07_S2_05_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_07_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_05_train*vec_mean_mean_Pmax_Hold_S1_07_S2_05_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_07_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_05_train*vec_mean_mean_Pmax_Hold_correct_S1_07_S2_05_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_05_train*vec_mean_mean_Pmax_Hold_total_S1_07_S2_05_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_05_test*vec_mean_mean_Pmax_Go_S1_07_S2_05_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_07_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_05_test*vec_mean_mean_Pmax_Hold_S1_07_S2_05_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_07_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_05_test*vec_mean_mean_Pmax_Hold_correct_S1_07_S2_05_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_05_test*vec_mean_mean_Pmax_Hold_total_S1_07_S2_05_test)

##geometric mean max PMC & RT 
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_05_train*vec_mean_mean_reaction_time_Go_S1_07_S2_05_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_07_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_05_train*vec_mean_mean_reaction_time_Hold_S1_07_S2_05_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_07_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_05_train*vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_05_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_05_train*vec_mean_mean_reaction_time_Hold_total_S1_07_S2_05_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_05_test*vec_mean_mean_reaction_time_Go_S1_07_S2_05_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_07_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_05_test*vec_mean_mean_reaction_time_Hold_S1_07_S2_05_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_07_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_05_test*vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_05_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_05_test*vec_mean_mean_reaction_time_Hold_total_S1_07_S2_05_test)

#SEROTONIN S1 = 0.7 and S2 = 0.7
#training
vec_mean_mean_reaction_time_Go_S1_07_S2_07_train=np.mean(data_S1_07_S2_07_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_07_S2_07_train=np.mean(data_S1_07_S2_07_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_07_train=np.mean(data_S1_07_S2_07_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_07_S2_07_train=np.mean(data_S1_07_S2_07_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_07_S2_07_train=np.mean(data_S1_07_S2_07_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_07_S2_07_train=np.mean(data_S1_07_S2_07_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_07_train=np.mean(data_S1_07_S2_07_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_07_S2_07_train=np.mean(data_S1_07_S2_07_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_07_S2_07_train=np.mean(data_S1_07_S2_07_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_07_S2_07_train=np.mean(data_S1_07_S2_07_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_07_S2_07_train=np.mean(data_S1_07_S2_07_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_07_S2_07_train=np.mean(data_S1_07_S2_07_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_07_S2_07_train=np.mean(data_S1_07_S2_07_train['right_inhibition'])
vec_mean_accuracy_S1_07_S2_07_train=np.mean(data_S1_07_S2_07_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_07_S2_07_train=np.std(data_S1_07_S2_07_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_07_S2_07_train=np.std(data_S1_07_S2_07_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_07_S2_07_train=np.std(data_S1_07_S2_07_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_07_S2_07_train=np.std(data_S1_07_S2_07_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_07_S2_07_train=np.std(data_S1_07_S2_07_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_07_S2_07_train=np.std(data_S1_07_S2_07_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_07_S2_07_train=np.std(data_S1_07_S2_07_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_07_S2_07_train=np.std(data_S1_07_S2_07_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_07_S2_07_train=np.std(data_S1_07_S2_07_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_07_S2_07_train=np.std(data_S1_07_S2_07_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_07_S2_07_train=np.std(data_S1_07_S2_07_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_07_S2_07_train=np.std(data_S1_07_S2_07_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_07_S2_07_train=np.std(data_S1_07_S2_07_train['right_inhibition'])
vec_std_accuracy_S1_07_S2_07_train=np.std(data_S1_07_S2_07_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_07_S2_07_test=np.mean(data_S1_07_S2_07_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_07_S2_07_test=np.mean(data_S1_07_S2_07_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_07_test=np.mean(data_S1_07_S2_07_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_07_S2_07_test=np.mean(data_S1_07_S2_07_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_07_S2_07_test=np.mean(data_S1_07_S2_07_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_07_S2_07_test=np.mean(data_S1_07_S2_07_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_07_test=np.mean(data_S1_07_S2_07_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_07_S2_07_test=np.mean(data_S1_07_S2_07_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_07_S2_07_test=np.mean(data_S1_07_S2_07_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_07_S2_07_test=np.mean(data_S1_07_S2_07_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_07_S2_07_test=np.mean(data_S1_07_S2_07_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_07_S2_07_test=np.mean(data_S1_07_S2_07_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_07_S2_07_test=np.mean(data_S1_07_S2_07_test['SSRT'])
vec_mean_right_inhibition_S1_07_S2_07_test=np.mean(data_S1_07_S2_07_test['right_inhibition'])
vec_mean_accuracy_S1_07_S2_07_test=np.mean(data_S1_07_S2_07_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_07_S2_07_test=np.std(data_S1_07_S2_07_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_07_S2_07_test=np.std(data_S1_07_S2_07_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_07_S2_07_test=np.std(data_S1_07_S2_07_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_07_S2_07_test=np.std(data_S1_07_S2_07_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_07_S2_07_test=np.std(data_S1_07_S2_07_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_07_S2_07_test=np.std(data_S1_07_S2_07_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_07_S2_07_test=np.std(data_S1_07_S2_07_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_07_S2_07_test=np.std(data_S1_07_S2_07_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_07_S2_07_test=np.std(data_S1_07_S2_07_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_07_S2_07_test=np.std(data_S1_07_S2_07_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_07_S2_07_test=np.std(data_S1_07_S2_07_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_07_S2_07_test=np.std(data_S1_07_S2_07_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_07_S2_07_test=np.std(data_S1_07_S2_07_test['SSRT'])
vec_std_right_inhibition_S1_07_S2_07_test=np.std(data_S1_07_S2_07_test['right_inhibition'])
vec_std_accuracy_S1_07_S2_07_test=np.std(data_S1_07_S2_07_test['accuracy'])

##geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_07_train*vec_mean_mean_Pmax_Go_S1_07_S2_07_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_07_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_07_train*vec_mean_mean_Pmax_Hold_S1_07_S2_07_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_07_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_07_train*vec_mean_mean_Pmax_Hold_correct_S1_07_S2_07_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_07_train*vec_mean_mean_Pmax_Hold_total_S1_07_S2_07_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_07_test*vec_mean_mean_Pmax_Go_S1_07_S2_07_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_07_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_07_test*vec_mean_mean_Pmax_Hold_S1_07_S2_07_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_07_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_07_test*vec_mean_mean_Pmax_Hold_correct_S1_07_S2_07_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_07_test*vec_mean_mean_Pmax_Hold_total_S1_07_S2_07_test)

##geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_07_train*vec_mean_mean_reaction_time_Go_S1_07_S2_07_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_07_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_07_train*vec_mean_mean_reaction_time_Hold_S1_07_S2_07_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_07_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_07_train*vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_07_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_07_train*vec_mean_mean_reaction_time_Hold_total_S1_07_S2_07_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_07_test*vec_mean_mean_reaction_time_Go_S1_07_S2_07_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_07_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_07_test*vec_mean_mean_reaction_time_Hold_S1_07_S2_07_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_07_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_07_test*vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_07_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_07_test*vec_mean_mean_reaction_time_Hold_total_S1_07_S2_07_test)

#SEROTONIN S1 = 0.7 and S2 = 0.9
#training
vec_mean_mean_reaction_time_Go_S1_07_S2_09_train=np.mean(data_S1_07_S2_09_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_07_S2_09_train=np.mean(data_S1_07_S2_09_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_09_train=np.mean(data_S1_07_S2_09_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_07_S2_09_train=np.mean(data_S1_07_S2_09_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_07_S2_09_train=np.mean(data_S1_07_S2_09_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_07_S2_09_train=np.mean(data_S1_07_S2_09_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_09_train=np.mean(data_S1_07_S2_09_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_07_S2_09_train=np.mean(data_S1_07_S2_09_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_07_S2_09_train=np.mean(data_S1_07_S2_09_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_07_S2_09_train=np.mean(data_S1_07_S2_09_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_07_S2_09_train=np.mean(data_S1_07_S2_09_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_07_S2_09_train=np.mean(data_S1_07_S2_09_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_07_S2_09_train=np.mean(data_S1_07_S2_09_train['right_inhibition'])
vec_mean_accuracy_S1_07_S2_09_train=np.mean(data_S1_07_S2_09_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_07_S2_09_train=np.std(data_S1_07_S2_09_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_07_S2_09_train=np.std(data_S1_07_S2_09_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_07_S2_09_train=np.std(data_S1_07_S2_09_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_07_S2_09_train=np.std(data_S1_07_S2_09_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_07_S2_09_train=np.std(data_S1_07_S2_09_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_07_S2_09_train=np.std(data_S1_07_S2_09_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_07_S2_09_train=np.std(data_S1_07_S2_09_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_07_S2_09_train=np.std(data_S1_07_S2_09_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_07_S2_09_train=np.std(data_S1_07_S2_09_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_07_S2_09_train=np.std(data_S1_07_S2_09_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_07_S2_09_train=np.std(data_S1_07_S2_09_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_07_S2_09_train=np.std(data_S1_07_S2_09_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_07_S2_09_train=np.std(data_S1_07_S2_09_train['right_inhibition'])
vec_std_accuracy_S1_07_S2_09_train=np.std(data_S1_07_S2_09_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_07_S2_09_test=np.mean(data_S1_07_S2_09_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_07_S2_09_test=np.mean(data_S1_07_S2_09_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_09_test=np.mean(data_S1_07_S2_09_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_07_S2_09_test=np.mean(data_S1_07_S2_09_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_07_S2_09_test=np.mean(data_S1_07_S2_09_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_07_S2_09_test=np.mean(data_S1_07_S2_09_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_09_test=np.mean(data_S1_07_S2_09_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_07_S2_09_test=np.mean(data_S1_07_S2_09_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_07_S2_09_test=np.mean(data_S1_07_S2_09_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_07_S2_09_test=np.mean(data_S1_07_S2_09_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_07_S2_09_test=np.mean(data_S1_07_S2_09_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_07_S2_09_test=np.mean(data_S1_07_S2_09_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_07_S2_09_test=np.mean(data_S1_07_S2_09_test['SSRT'])
vec_mean_right_inhibition_S1_07_S2_09_test=np.mean(data_S1_07_S2_09_test['right_inhibition'])
vec_mean_accuracy_S1_07_S2_09_test=np.mean(data_S1_07_S2_09_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_07_S2_09_test=np.std(data_S1_07_S2_09_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_07_S2_09_test=np.std(data_S1_07_S2_09_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_07_S2_09_test=np.std(data_S1_07_S2_09_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_07_S2_09_test=np.std(data_S1_07_S2_09_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_07_S2_09_test=np.std(data_S1_07_S2_09_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_07_S2_09_test=np.std(data_S1_07_S2_09_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_07_S2_09_test=np.std(data_S1_07_S2_09_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_07_S2_09_test=np.std(data_S1_07_S2_09_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_07_S2_09_test=np.std(data_S1_07_S2_09_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_07_S2_09_test=np.std(data_S1_07_S2_09_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_07_S2_09_test=np.std(data_S1_07_S2_09_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_07_S2_09_test=np.std(data_S1_07_S2_09_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_07_S2_09_test=np.std(data_S1_07_S2_09_test['SSRT'])
vec_std_right_inhibition_S1_07_S2_09_test=np.std(data_S1_07_S2_09_test['right_inhibition'])
vec_std_accuracy_S1_07_S2_09_test=np.std(data_S1_07_S2_09_test['accuracy'])

##geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_09_train*vec_mean_mean_Pmax_Go_S1_07_S2_09_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_07_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_09_train*vec_mean_mean_Pmax_Hold_S1_07_S2_09_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_07_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_09_train*vec_mean_mean_Pmax_Hold_correct_S1_07_S2_09_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_09_train*vec_mean_mean_Pmax_Hold_total_S1_07_S2_09_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_09_test*vec_mean_mean_Pmax_Go_S1_07_S2_09_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_07_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_09_test*vec_mean_mean_Pmax_Hold_S1_07_S2_09_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_07_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_09_test*vec_mean_mean_Pmax_Hold_correct_S1_07_S2_09_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_09_test*vec_mean_mean_Pmax_Hold_total_S1_07_S2_09_test)

##geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_09_train*vec_mean_mean_reaction_time_Go_S1_07_S2_09_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_07_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_09_train*vec_mean_mean_reaction_time_Hold_S1_07_S2_09_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_07_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_09_train*vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_09_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_09_train*vec_mean_mean_reaction_time_Hold_total_S1_07_S2_09_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_07_S2_09_test*vec_mean_mean_reaction_time_Go_S1_07_S2_09_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_07_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_07_S2_09_test*vec_mean_mean_reaction_time_Hold_S1_07_S2_09_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_07_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_09_test*vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_09_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_07_S2_09_test*vec_mean_mean_reaction_time_Hold_total_S1_07_S2_09_test)

#SEROTONIN S1 = 0.9 and S2 = 0.1
#training
vec_mean_mean_reaction_time_Go_S1_09_S2_01_train=np.mean(data_S1_09_S2_01_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_09_S2_01_train=np.mean(data_S1_09_S2_01_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_01_train=np.mean(data_S1_09_S2_01_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_09_S2_01_train=np.mean(data_S1_09_S2_01_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_09_S2_01_train=np.mean(data_S1_09_S2_01_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_09_S2_01_train=np.mean(data_S1_09_S2_01_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_01_train=np.mean(data_S1_09_S2_01_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_09_S2_01_train=np.mean(data_S1_09_S2_01_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_09_S2_01_train=np.mean(data_S1_09_S2_01_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_09_S2_01_train=np.mean(data_S1_09_S2_01_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_09_S2_01_train=np.mean(data_S1_09_S2_01_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_09_S2_01_train=np.mean(data_S1_09_S2_01_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_09_S2_01_train=np.mean(data_S1_09_S2_01_train['right_inhibition'])
vec_mean_accuracy_S1_09_S2_01_train=np.mean(data_S1_09_S2_01_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_09_S2_01_train=np.std(data_S1_09_S2_01_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_09_S2_01_train=np.std(data_S1_09_S2_01_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_09_S2_01_train=np.std(data_S1_09_S2_01_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_09_S2_01_train=np.std(data_S1_09_S2_01_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_09_S2_01_train=np.std(data_S1_09_S2_01_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_09_S2_01_train=np.std(data_S1_09_S2_01_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_09_S2_01_train=np.std(data_S1_09_S2_01_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_09_S2_01_train=np.std(data_S1_09_S2_01_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_09_S2_01_train=np.std(data_S1_09_S2_01_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_09_S2_01_train=np.std(data_S1_09_S2_01_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_09_S2_01_train=np.std(data_S1_09_S2_01_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_09_S2_01_train=np.std(data_S1_09_S2_01_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_09_S2_01_train=np.std(data_S1_09_S2_01_train['right_inhibition'])
vec_std_accuracy_S1_09_S2_01_train=np.std(data_S1_09_S2_01_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_09_S2_01_test=np.mean(data_S1_09_S2_01_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_09_S2_01_test=np.mean(data_S1_09_S2_01_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_01_test=np.mean(data_S1_09_S2_01_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_09_S2_01_test=np.mean(data_S1_09_S2_01_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_09_S2_01_test=np.mean(data_S1_09_S2_01_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_09_S2_01_test=np.mean(data_S1_09_S2_01_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_01_test=np.mean(data_S1_09_S2_01_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_09_S2_01_test=np.mean(data_S1_09_S2_01_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_09_S2_01_test=np.mean(data_S1_09_S2_01_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_09_S2_01_test=np.mean(data_S1_09_S2_01_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_09_S2_01_test=np.mean(data_S1_09_S2_01_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_09_S2_01_test=np.mean(data_S1_09_S2_01_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_09_S2_01_test=np.mean(data_S1_09_S2_01_test['SSRT'])
vec_mean_right_inhibition_S1_09_S2_01_test=np.mean(data_S1_09_S2_01_test['right_inhibition'])
vec_mean_accuracy_S1_09_S2_01_test=np.mean(data_S1_09_S2_01_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_09_S2_01_test=np.std(data_S1_09_S2_01_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_09_S2_01_test=np.std(data_S1_09_S2_01_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_09_S2_01_test=np.std(data_S1_09_S2_01_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_09_S2_01_test=np.std(data_S1_09_S2_01_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_09_S2_01_test=np.std(data_S1_09_S2_01_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_09_S2_01_test=np.std(data_S1_09_S2_01_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_09_S2_01_test=np.std(data_S1_09_S2_01_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_09_S2_01_test=np.std(data_S1_09_S2_01_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_09_S2_01_test=np.std(data_S1_09_S2_01_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_09_S2_01_test=np.std(data_S1_09_S2_01_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_09_S2_01_test=np.std(data_S1_09_S2_01_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_09_S2_01_test=np.std(data_S1_09_S2_01_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_09_S2_01_test=np.std(data_S1_09_S2_01_test['SSRT'])
vec_std_right_inhibition_S1_09_S2_01_test=np.std(data_S1_09_S2_01_test['right_inhibition'])
vec_std_accuracy_S1_09_S2_01_test=np.std(data_S1_09_S2_01_test['accuracy'])

##geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_01_train*vec_mean_mean_Pmax_Go_S1_09_S2_01_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_09_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_01_train*vec_mean_mean_Pmax_Hold_S1_09_S2_01_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_09_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_01_train*vec_mean_mean_Pmax_Hold_correct_S1_09_S2_01_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_01_train*vec_mean_mean_Pmax_Hold_total_S1_09_S2_01_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_01_test*vec_mean_mean_Pmax_Go_S1_09_S2_01_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_09_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_01_test*vec_mean_mean_Pmax_Hold_S1_09_S2_01_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_09_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_01_test*vec_mean_mean_Pmax_Hold_correct_S1_09_S2_01_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_01_test*vec_mean_mean_Pmax_Hold_total_S1_09_S2_01_test)

##geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_01_train*vec_mean_mean_reaction_time_Go_S1_09_S2_01_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_09_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_01_train*vec_mean_mean_reaction_time_Hold_S1_09_S2_01_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_09_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_01_train*vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_01_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_01_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_01_train*vec_mean_mean_reaction_time_Hold_total_S1_09_S2_01_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_01_test*vec_mean_mean_reaction_time_Go_S1_09_S2_01_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_09_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_01_test*vec_mean_mean_reaction_time_Hold_S1_09_S2_01_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_09_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_01_test*vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_01_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_01_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_01_test*vec_mean_mean_reaction_time_Hold_total_S1_09_S2_01_test)

#SEROTONIN S1 = 0.9 and S2 = 0.3
#training
vec_mean_mean_reaction_time_Go_S1_09_S2_03_train=np.mean(data_S1_09_S2_03_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_09_S2_03_train=np.mean(data_S1_09_S2_03_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_03_train=np.mean(data_S1_09_S2_03_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_09_S2_03_train=np.mean(data_S1_09_S2_03_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_09_S2_03_train=np.mean(data_S1_09_S2_03_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_09_S2_03_train=np.mean(data_S1_09_S2_03_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_03_train=np.mean(data_S1_09_S2_03_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_09_S2_03_train=np.mean(data_S1_09_S2_03_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_09_S2_03_train=np.mean(data_S1_09_S2_03_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_09_S2_03_train=np.mean(data_S1_09_S2_03_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_09_S2_03_train=np.mean(data_S1_09_S2_03_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_09_S2_03_train=np.mean(data_S1_09_S2_03_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_09_S2_03_train=np.mean(data_S1_09_S2_03_train['right_inhibition'])
vec_mean_accuracy_S1_09_S2_03_train=np.mean(data_S1_09_S2_03_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_09_S2_03_train=np.std(data_S1_09_S2_03_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_09_S2_03_train=np.std(data_S1_09_S2_03_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_09_S2_03_train=np.std(data_S1_09_S2_03_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_09_S2_03_train=np.std(data_S1_09_S2_03_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_09_S2_03_train=np.std(data_S1_09_S2_03_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_09_S2_03_train=np.std(data_S1_09_S2_03_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_09_S2_03_train=np.std(data_S1_09_S2_03_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_09_S2_03_train=np.std(data_S1_09_S2_03_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_09_S2_03_train=np.std(data_S1_09_S2_03_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_09_S2_03_train=np.std(data_S1_09_S2_03_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_09_S2_03_train=np.std(data_S1_09_S2_03_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_09_S2_03_train=np.std(data_S1_09_S2_03_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_09_S2_03_train=np.std(data_S1_09_S2_03_train['right_inhibition'])
vec_std_accuracy_S1_09_S2_03_train=np.std(data_S1_09_S2_03_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_09_S2_03_test=np.mean(data_S1_09_S2_03_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_09_S2_03_test=np.mean(data_S1_09_S2_03_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_03_test=np.mean(data_S1_09_S2_03_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_09_S2_03_test=np.mean(data_S1_09_S2_03_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_09_S2_03_test=np.mean(data_S1_09_S2_03_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_09_S2_03_test=np.mean(data_S1_09_S2_03_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_03_test=np.mean(data_S1_09_S2_03_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_09_S2_03_test=np.mean(data_S1_09_S2_03_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_09_S2_03_test=np.mean(data_S1_09_S2_03_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_09_S2_03_test=np.mean(data_S1_09_S2_03_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_09_S2_03_test=np.mean(data_S1_09_S2_03_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_09_S2_03_test=np.mean(data_S1_09_S2_03_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_09_S2_03_test=np.mean(data_S1_09_S2_03_test['SSRT'])
vec_mean_right_inhibition_S1_09_S2_03_test=np.mean(data_S1_09_S2_03_test['right_inhibition'])
vec_mean_accuracy_S1_09_S2_03_test=np.mean(data_S1_09_S2_03_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_09_S2_03_test=np.std(data_S1_09_S2_03_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_09_S2_03_test=np.std(data_S1_09_S2_03_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_09_S2_03_test=np.std(data_S1_09_S2_03_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_09_S2_03_test=np.std(data_S1_09_S2_03_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_09_S2_03_test=np.std(data_S1_09_S2_03_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_09_S2_03_test=np.std(data_S1_09_S2_03_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_09_S2_03_test=np.std(data_S1_09_S2_03_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_09_S2_03_test=np.std(data_S1_09_S2_03_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_09_S2_03_test=np.std(data_S1_09_S2_03_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_09_S2_03_test=np.std(data_S1_09_S2_03_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_09_S2_03_test=np.std(data_S1_09_S2_03_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_09_S2_03_test=np.std(data_S1_09_S2_03_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_09_S2_03_test=np.std(data_S1_09_S2_03_test['SSRT'])
vec_std_right_inhibition_S1_09_S2_03_test=np.std(data_S1_09_S2_03_test['right_inhibition'])
vec_std_accuracy_S1_09_S2_03_test=np.std(data_S1_09_S2_03_test['accuracy'])

##geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_03_train*vec_mean_mean_Pmax_Go_S1_09_S2_03_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_09_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_03_train*vec_mean_mean_Pmax_Hold_S1_09_S2_03_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_09_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_03_train*vec_mean_mean_Pmax_Hold_correct_S1_09_S2_03_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_03_train*vec_mean_mean_Pmax_Hold_total_S1_09_S2_03_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_03_test*vec_mean_mean_Pmax_Go_S1_09_S2_03_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_09_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_03_test*vec_mean_mean_Pmax_Hold_S1_09_S2_03_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_09_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_03_test*vec_mean_mean_Pmax_Hold_correct_S1_09_S2_03_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_03_test*vec_mean_mean_Pmax_Hold_total_S1_09_S2_03_test)

##geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_03_train*vec_mean_mean_reaction_time_Go_S1_09_S2_03_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_09_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_03_train*vec_mean_mean_reaction_time_Hold_S1_09_S2_03_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_09_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_03_train*vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_03_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_03_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_03_train*vec_mean_mean_reaction_time_Hold_total_S1_09_S2_03_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_03_test*vec_mean_mean_reaction_time_Go_S1_09_S2_03_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_09_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_03_test*vec_mean_mean_reaction_time_Hold_S1_09_S2_03_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_09_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_03_test*vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_03_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_03_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_03_test*vec_mean_mean_reaction_time_Hold_total_S1_09_S2_03_test)

#SEROTONIN S1 = 0.9 and S2 = 0.5
#training
vec_mean_mean_reaction_time_Go_S1_09_S2_05_train=np.mean(data_S1_09_S2_05_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_09_S2_05_train=np.mean(data_S1_09_S2_05_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_05_train=np.mean(data_S1_09_S2_05_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_09_S2_05_train=np.mean(data_S1_09_S2_05_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_09_S2_05_train=np.mean(data_S1_09_S2_05_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_09_S2_05_train=np.mean(data_S1_09_S2_05_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_05_train=np.mean(data_S1_09_S2_05_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_09_S2_05_train=np.mean(data_S1_09_S2_05_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_09_S2_05_train=np.mean(data_S1_09_S2_05_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_09_S2_05_train=np.mean(data_S1_09_S2_05_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_09_S2_05_train=np.mean(data_S1_09_S2_05_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_09_S2_05_train=np.mean(data_S1_09_S2_05_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_09_S2_05_train=np.mean(data_S1_09_S2_05_train['right_inhibition'])
vec_mean_accuracy_S1_09_S2_05_train=np.mean(data_S1_09_S2_05_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_09_S2_05_train=np.std(data_S1_09_S2_05_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_09_S2_05_train=np.std(data_S1_09_S2_05_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_09_S2_05_train=np.std(data_S1_09_S2_05_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_09_S2_05_train=np.std(data_S1_09_S2_05_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_09_S2_05_train=np.std(data_S1_09_S2_05_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_09_S2_05_train=np.std(data_S1_09_S2_05_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_09_S2_05_train=np.std(data_S1_09_S2_05_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_09_S2_05_train=np.std(data_S1_09_S2_05_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_09_S2_05_train=np.std(data_S1_09_S2_05_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_09_S2_05_train=np.std(data_S1_09_S2_05_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_09_S2_05_train=np.std(data_S1_09_S2_05_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_09_S2_05_train=np.std(data_S1_09_S2_05_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_09_S2_05_train=np.std(data_S1_09_S2_05_train['right_inhibition'])
vec_std_accuracy_S1_09_S2_05_train=np.std(data_S1_09_S2_05_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_09_S2_05_test=np.mean(data_S1_09_S2_05_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_09_S2_05_test=np.mean(data_S1_09_S2_05_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_05_test=np.mean(data_S1_09_S2_05_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_09_S2_05_test=np.mean(data_S1_09_S2_05_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_09_S2_05_test=np.mean(data_S1_09_S2_05_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_09_S2_05_test=np.mean(data_S1_09_S2_05_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_05_test=np.mean(data_S1_09_S2_05_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_09_S2_05_test=np.mean(data_S1_09_S2_05_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_09_S2_05_test=np.mean(data_S1_09_S2_05_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_09_S2_05_test=np.mean(data_S1_09_S2_05_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_09_S2_05_test=np.mean(data_S1_09_S2_05_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_09_S2_05_test=np.mean(data_S1_09_S2_05_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_09_S2_05_test=np.mean(data_S1_09_S2_05_test['SSRT'])
vec_mean_right_inhibition_S1_09_S2_05_test=np.mean(data_S1_09_S2_05_test['right_inhibition'])
vec_mean_accuracy_S1_09_S2_05_test=np.mean(data_S1_09_S2_05_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_09_S2_05_test=np.std(data_S1_09_S2_05_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_09_S2_05_test=np.std(data_S1_09_S2_05_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_09_S2_05_test=np.std(data_S1_09_S2_05_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_09_S2_05_test=np.std(data_S1_09_S2_05_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_09_S2_05_test=np.std(data_S1_09_S2_05_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_09_S2_05_test=np.std(data_S1_09_S2_05_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_09_S2_05_test=np.std(data_S1_09_S2_05_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_09_S2_05_test=np.std(data_S1_09_S2_05_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_09_S2_05_test=np.std(data_S1_09_S2_05_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_09_S2_05_test=np.std(data_S1_09_S2_05_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_09_S2_05_test=np.std(data_S1_09_S2_05_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_09_S2_05_test=np.std(data_S1_09_S2_05_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_09_S2_05_test=np.std(data_S1_09_S2_05_test['SSRT'])
vec_std_right_inhibition_S1_09_S2_05_test=np.std(data_S1_09_S2_05_test['right_inhibition'])
vec_std_accuracy_S1_09_S2_05_test=np.std(data_S1_09_S2_05_test['accuracy'])

##geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_05_train*vec_mean_mean_Pmax_Go_S1_09_S2_05_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_09_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_05_train*vec_mean_mean_Pmax_Hold_S1_09_S2_05_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_09_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_05_train*vec_mean_mean_Pmax_Hold_correct_S1_09_S2_05_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_05_train*vec_mean_mean_Pmax_Hold_total_S1_09_S2_05_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_05_test*vec_mean_mean_Pmax_Go_S1_09_S2_05_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_09_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_05_test*vec_mean_mean_Pmax_Hold_S1_09_S2_05_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_09_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_05_test*vec_mean_mean_Pmax_Hold_correct_S1_09_S2_05_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_05_test*vec_mean_mean_Pmax_Hold_total_S1_09_S2_05_test)

##geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_05_train*vec_mean_mean_reaction_time_Go_S1_09_S2_05_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_09_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_05_train*vec_mean_mean_reaction_time_Hold_S1_09_S2_05_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_09_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_05_train*vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_05_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_05_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_05_train*vec_mean_mean_reaction_time_Hold_total_S1_09_S2_05_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_05_test*vec_mean_mean_reaction_time_Go_S1_09_S2_05_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_09_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_05_test*vec_mean_mean_reaction_time_Hold_S1_09_S2_05_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_09_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_05_test*vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_05_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_05_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_05_test*vec_mean_mean_reaction_time_Hold_total_S1_09_S2_05_test)

#SEROTONIN S1 = 0.9 and S2 = 0.7
#training
vec_mean_mean_reaction_time_Go_S1_09_S2_07_train=np.mean(data_S1_09_S2_07_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_09_S2_07_train=np.mean(data_S1_09_S2_07_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_07_train=np.mean(data_S1_09_S2_07_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_09_S2_07_train=np.mean(data_S1_09_S2_07_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_09_S2_07_train=np.mean(data_S1_09_S2_07_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_09_S2_07_train=np.mean(data_S1_09_S2_07_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_07_train=np.mean(data_S1_09_S2_07_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_09_S2_07_train=np.mean(data_S1_09_S2_07_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_09_S2_07_train=np.mean(data_S1_09_S2_07_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_09_S2_07_train=np.mean(data_S1_09_S2_07_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_09_S2_07_train=np.mean(data_S1_09_S2_07_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_09_S2_07_train=np.mean(data_S1_09_S2_07_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_09_S2_07_train=np.mean(data_S1_09_S2_07_train['right_inhibition'])
vec_mean_accuracy_S1_09_S2_07_train=np.mean(data_S1_09_S2_07_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_09_S2_07_train=np.std(data_S1_09_S2_07_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_09_S2_07_train=np.std(data_S1_09_S2_07_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_09_S2_07_train=np.std(data_S1_09_S2_07_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_09_S2_07_train=np.std(data_S1_09_S2_07_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_09_S2_07_train=np.std(data_S1_09_S2_07_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_09_S2_07_train=np.std(data_S1_09_S2_07_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_09_S2_07_train=np.std(data_S1_09_S2_07_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_09_S2_07_train=np.std(data_S1_09_S2_07_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_09_S2_07_train=np.std(data_S1_09_S2_07_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_09_S2_07_train=np.std(data_S1_09_S2_07_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_09_S2_07_train=np.std(data_S1_09_S2_07_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_09_S2_07_train=np.std(data_S1_09_S2_07_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_09_S2_07_train=np.std(data_S1_09_S2_07_train['right_inhibition'])
vec_std_accuracy_S1_09_S2_07_train=np.std(data_S1_09_S2_07_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_09_S2_07_test=np.mean(data_S1_09_S2_07_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_09_S2_07_test=np.mean(data_S1_09_S2_07_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_07_test=np.mean(data_S1_09_S2_07_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_09_S2_07_test=np.mean(data_S1_09_S2_07_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_09_S2_07_test=np.mean(data_S1_09_S2_07_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_09_S2_07_test=np.mean(data_S1_09_S2_07_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_07_test=np.mean(data_S1_09_S2_07_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_09_S2_07_test=np.mean(data_S1_09_S2_07_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_09_S2_07_test=np.mean(data_S1_09_S2_07_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_09_S2_07_test=np.mean(data_S1_09_S2_07_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_09_S2_07_test=np.mean(data_S1_09_S2_07_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_09_S2_07_test=np.mean(data_S1_09_S2_07_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_09_S2_07_test=np.mean(data_S1_09_S2_07_test['SSRT'])
vec_mean_right_inhibition_S1_09_S2_07_test=np.mean(data_S1_09_S2_07_test['right_inhibition'])
vec_mean_accuracy_S1_09_S2_07_test=np.mean(data_S1_09_S2_07_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_09_S2_07_test=np.std(data_S1_09_S2_07_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_09_S2_07_test=np.std(data_S1_09_S2_07_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_09_S2_07_test=np.std(data_S1_09_S2_07_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_09_S2_07_test=np.std(data_S1_09_S2_07_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_09_S2_07_test=np.std(data_S1_09_S2_07_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_09_S2_07_test=np.std(data_S1_09_S2_07_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_09_S2_07_test=np.std(data_S1_09_S2_07_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_09_S2_07_test=np.std(data_S1_09_S2_07_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_09_S2_07_test=np.std(data_S1_09_S2_07_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_09_S2_07_test=np.std(data_S1_09_S2_07_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_09_S2_07_test=np.std(data_S1_09_S2_07_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_09_S2_07_test=np.std(data_S1_09_S2_07_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_09_S2_07_test=np.std(data_S1_09_S2_07_test['SSRT'])
vec_std_right_inhibition_S1_09_S2_07_test=np.std(data_S1_09_S2_07_test['right_inhibition'])
vec_std_accuracy_S1_09_S2_07_test=np.std(data_S1_09_S2_07_test['accuracy'])

##geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_07_train*vec_mean_mean_Pmax_Go_S1_09_S2_07_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_09_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_07_train*vec_mean_mean_Pmax_Hold_S1_09_S2_07_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_09_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_07_train*vec_mean_mean_Pmax_Hold_correct_S1_09_S2_07_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_07_train*vec_mean_mean_Pmax_Hold_total_S1_09_S2_07_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_07_test*vec_mean_mean_Pmax_Go_S1_09_S2_07_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_09_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_07_test*vec_mean_mean_Pmax_Hold_S1_09_S2_07_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_09_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_07_test*vec_mean_mean_Pmax_Hold_correct_S1_09_S2_07_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_07_test*vec_mean_mean_Pmax_Hold_total_S1_09_S2_07_test)

##geometric mean max PMC & RT 
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_07_train*vec_mean_mean_reaction_time_Go_S1_09_S2_07_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_09_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_07_train*vec_mean_mean_reaction_time_Hold_S1_09_S2_07_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_09_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_07_train*vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_07_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_07_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_07_train*vec_mean_mean_reaction_time_Hold_total_S1_09_S2_07_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_07_test*vec_mean_mean_reaction_time_Go_S1_09_S2_07_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_09_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_07_test*vec_mean_mean_reaction_time_Hold_S1_09_S2_07_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_09_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_07_test*vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_07_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_07_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_07_test*vec_mean_mean_reaction_time_Hold_total_S1_09_S2_07_test)

#SEROTONIN S1 = 0.9 and S2 = 0.9
#training
vec_mean_mean_reaction_time_Go_S1_09_S2_09_train=np.mean(data_S1_09_S2_09_train['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_09_S2_09_train=np.mean(data_S1_09_S2_09_train['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_09_train=np.mean(data_S1_09_S2_09_train['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_09_S2_09_train=np.mean(data_S1_09_S2_09_train['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_09_S2_09_train=np.mean(data_S1_09_S2_09_train['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_09_S2_09_train=np.mean(data_S1_09_S2_09_train['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_09_train=np.mean(data_S1_09_S2_09_train['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_09_S2_09_train=np.mean(data_S1_09_S2_09_train['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_09_S2_09_train=np.mean(data_S1_09_S2_09_train['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_09_S2_09_train=np.mean(data_S1_09_S2_09_train['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_09_S2_09_train=np.mean(data_S1_09_S2_09_train['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_09_S2_09_train=np.mean(data_S1_09_S2_09_train['mean_Pmax_Hold_total'])

vec_mean_right_inhibition_S1_09_S2_09_train=np.mean(data_S1_09_S2_09_train['right_inhibition'])
vec_mean_accuracy_S1_09_S2_09_train=np.mean(data_S1_09_S2_09_train['accuracy'])

vec_std_mean_reaction_time_Go_S1_09_S2_09_train=np.std(data_S1_09_S2_09_train['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_09_S2_09_train=np.std(data_S1_09_S2_09_train['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_09_S2_09_train=np.std(data_S1_09_S2_09_train['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_09_S2_09_train=np.std(data_S1_09_S2_09_train['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_09_S2_09_train=np.std(data_S1_09_S2_09_train['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_09_S2_09_train=np.std(data_S1_09_S2_09_train['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_09_S2_09_train=np.std(data_S1_09_S2_09_train['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_09_S2_09_train=np.std(data_S1_09_S2_09_train['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_09_S2_09_train=np.std(data_S1_09_S2_09_train['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_09_S2_09_train=np.std(data_S1_09_S2_09_train['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_09_S2_09_train=np.std(data_S1_09_S2_09_train['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_09_S2_09_train=np.std(data_S1_09_S2_09_train['mean_Pmax_Hold_total'])

vec_std_right_inhibition_S1_09_S2_09_train=np.std(data_S1_09_S2_09_train['right_inhibition'])
vec_std_accuracy_S1_09_S2_09_train=np.std(data_S1_09_S2_09_train['accuracy'])

#test
vec_mean_mean_reaction_time_Go_S1_09_S2_09_test=np.mean(data_S1_09_S2_09_test['mean_reaction_time_Go_1'])
vec_mean_mean_reaction_time_Hold_S1_09_S2_09_test=np.mean(data_S1_09_S2_09_test['mean_reaction_time_Hold_1'])
vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_09_test=np.mean(data_S1_09_S2_09_test['mean_reaction_time_Hold_correct_1'])
vec_mean_mean_reaction_time_Hold_total_S1_09_S2_09_test=np.mean(data_S1_09_S2_09_test['mean_reaction_time_Hold_total_1'])

vec_mean_mean_max_PMC_Go_S1_09_S2_09_test=np.mean(data_S1_09_S2_09_test['mean_max_PMC_Go'])
vec_mean_mean_max_PMC_Hold_S1_09_S2_09_test=np.mean(data_S1_09_S2_09_test['mean_max_PMC_Hold'])
vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_09_test=np.mean(data_S1_09_S2_09_test['mean_max_PMC_Hold_correct'])
vec_mean_mean_max_PMC_Hold_total_S1_09_S2_09_test=np.mean(data_S1_09_S2_09_test['mean_max_PMC_Hold_total'])

vec_mean_mean_Pmax_Go_S1_09_S2_09_test=np.mean(data_S1_09_S2_09_test['mean_Pmax_Go'])
vec_mean_mean_Pmax_Hold_S1_09_S2_09_test=np.mean(data_S1_09_S2_09_test['mean_Pmax_Hold'])
vec_mean_mean_Pmax_Hold_correct_S1_09_S2_09_test=np.mean(data_S1_09_S2_09_test['mean_Pmax_Hold_correct'])
vec_mean_mean_Pmax_Hold_total_S1_09_S2_09_test=np.mean(data_S1_09_S2_09_test['mean_Pmax_Hold_total'])

vec_mean_mean_SSRT_S1_09_S2_09_test=np.mean(data_S1_09_S2_09_test['SSRT'])
vec_mean_right_inhibition_S1_09_S2_09_test=np.mean(data_S1_09_S2_09_test['right_inhibition'])
vec_mean_accuracy_S1_09_S2_09_test=np.mean(data_S1_09_S2_09_test['accuracy'])

vec_std_mean_reaction_time_Go_S1_09_S2_09_test=np.std(data_S1_09_S2_09_test['mean_reaction_time_Go_1'])
vec_std_mean_reaction_time_Hold_S1_09_S2_09_test=np.std(data_S1_09_S2_09_test['mean_reaction_time_Hold_1'])
vec_std_mean_reaction_time_Hold_correct_S1_09_S2_09_test=np.std(data_S1_09_S2_09_test['mean_reaction_time_Hold_correct_1'])
vec_std_mean_reaction_time_Hold_total_S1_09_S2_09_test=np.std(data_S1_09_S2_09_test['mean_reaction_time_Hold_total_1'])

vec_std_mean_max_PMC_Go_S1_09_S2_09_test=np.std(data_S1_09_S2_09_test['mean_max_PMC_Go'])
vec_std_mean_max_PMC_Hold_S1_09_S2_09_test=np.std(data_S1_09_S2_09_test['mean_max_PMC_Hold'])
vec_std_mean_max_PMC_Hold_correct_S1_09_S2_09_test=np.std(data_S1_09_S2_09_test['mean_max_PMC_Hold_correct'])
vec_std_mean_max_PMC_Hold_total_S1_09_S2_09_test=np.std(data_S1_09_S2_09_test['mean_max_PMC_Hold_total'])

vec_std_mean_Pmax_Go_S1_09_S2_09_test=np.std(data_S1_09_S2_09_test['mean_Pmax_Go'])
vec_std_mean_Pmax_Hold_S1_09_S2_09_test=np.std(data_S1_09_S2_09_test['mean_Pmax_Hold'])
vec_std_mean_Pmax_Hold_correct_S1_09_S2_09_test=np.std(data_S1_09_S2_09_test['mean_Pmax_Hold_correct'])
vec_std_mean_Pmax_Hold_total_S1_09_S2_09_test=np.std(data_S1_09_S2_09_test['mean_Pmax_Hold_total'])

vec_std_mean_SSRT_S1_09_S2_09_test=np.std(data_S1_09_S2_09_test['SSRT'])
vec_std_right_inhibition_S1_09_S2_09_test=np.std(data_S1_09_S2_09_test['right_inhibition'])
vec_std_accuracy_S1_09_S2_09_test=np.std(data_S1_09_S2_09_test['accuracy'])

##geometric mean max PMC & Pmax 
#training
vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_09_train*vec_mean_mean_Pmax_Go_S1_09_S2_09_train)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_09_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_09_train*vec_mean_mean_Pmax_Hold_S1_09_S2_09_train)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_09_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_09_train*vec_mean_mean_Pmax_Hold_correct_S1_09_S2_09_train)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_09_train*vec_mean_mean_Pmax_Hold_total_S1_09_S2_09_train)

#test
vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_09_test*vec_mean_mean_Pmax_Go_S1_09_S2_09_test)
vec_meanG_mean_max_PMC_Pmax_Hold_S1_09_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_09_test*vec_mean_mean_Pmax_Hold_S1_09_S2_09_test)
vec_meanG_mean_max_PMC_Pmax_Hold_correct_S1_09_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_09_test*vec_mean_mean_Pmax_Hold_correct_S1_09_S2_09_test)
vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_09_test*vec_mean_mean_Pmax_Hold_total_S1_09_S2_09_test)

##geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_09_train*vec_mean_mean_reaction_time_Go_S1_09_S2_09_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_09_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_09_train*vec_mean_mean_reaction_time_Hold_S1_09_S2_09_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_09_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_09_train*vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_09_train)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_09_train=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_09_train*vec_mean_mean_reaction_time_Hold_total_S1_09_S2_09_train)

#test
vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Go_S1_09_S2_09_test*vec_mean_mean_reaction_time_Go_S1_09_S2_09_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_S1_09_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_S1_09_S2_09_test*vec_mean_mean_reaction_time_Hold_S1_09_S2_09_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_correct_S1_09_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_09_test*vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_09_test)
vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_09_test=np.sqrt(vec_mean_mean_max_PMC_Hold_total_S1_09_S2_09_test*vec_mean_mean_reaction_time_Hold_total_S1_09_S2_09_test)

#reaction time Go
#training
vec_mean_mean_reaction_time_Go_training=[[vec_mean_mean_reaction_time_Go_S1_01_S2_01_train,vec_mean_mean_reaction_time_Go_S1_01_S2_03_train,vec_mean_mean_reaction_time_Go_S1_01_S2_05_train,vec_mean_mean_reaction_time_Go_S1_01_S2_07_train,vec_mean_mean_reaction_time_Go_S1_01_S2_09_train],
                                         [vec_mean_mean_reaction_time_Go_S1_03_S2_01_train,vec_mean_mean_reaction_time_Go_S1_03_S2_03_train,vec_mean_mean_reaction_time_Go_S1_03_S2_05_train,vec_mean_mean_reaction_time_Go_S1_03_S2_07_train,vec_mean_mean_reaction_time_Go_S1_03_S2_09_train],
                                         [vec_mean_mean_reaction_time_Go_S1_05_S2_01_train,vec_mean_mean_reaction_time_Go_S1_05_S2_03_train,vec_mean_mean_reaction_time_Go_S1_05_S2_05_train,vec_mean_mean_reaction_time_Go_S1_05_S2_07_train,vec_mean_mean_reaction_time_Go_S1_05_S2_09_train],
                                         [vec_mean_mean_reaction_time_Go_S1_07_S2_01_train,vec_mean_mean_reaction_time_Go_S1_07_S2_03_train,vec_mean_mean_reaction_time_Go_S1_07_S2_05_train,vec_mean_mean_reaction_time_Go_S1_07_S2_07_train,vec_mean_mean_reaction_time_Go_S1_07_S2_09_train],
                                         [vec_mean_mean_reaction_time_Go_S1_09_S2_01_train,vec_mean_mean_reaction_time_Go_S1_09_S2_03_train,vec_mean_mean_reaction_time_Go_S1_09_S2_05_train,vec_mean_mean_reaction_time_Go_S1_09_S2_07_train,vec_mean_mean_reaction_time_Go_S1_09_S2_09_train]]

vec_std_mean_reaction_time_Go_training=[[vec_std_mean_reaction_time_Go_S1_01_S2_01_train,vec_std_mean_reaction_time_Go_S1_01_S2_03_train,vec_std_mean_reaction_time_Go_S1_01_S2_05_train,vec_std_mean_reaction_time_Go_S1_01_S2_07_train,vec_std_mean_reaction_time_Go_S1_01_S2_09_train],
                                        [vec_std_mean_reaction_time_Go_S1_03_S2_01_train,vec_std_mean_reaction_time_Go_S1_03_S2_03_train,vec_std_mean_reaction_time_Go_S1_03_S2_05_train,vec_std_mean_reaction_time_Go_S1_03_S2_07_train,vec_std_mean_reaction_time_Go_S1_03_S2_09_train],
                                        [vec_std_mean_reaction_time_Go_S1_05_S2_01_train,vec_std_mean_reaction_time_Go_S1_05_S2_03_train,vec_std_mean_reaction_time_Go_S1_05_S2_05_train,vec_std_mean_reaction_time_Go_S1_05_S2_07_train,vec_std_mean_reaction_time_Go_S1_05_S2_09_train],
                                        [vec_std_mean_reaction_time_Go_S1_07_S2_01_train,vec_std_mean_reaction_time_Go_S1_07_S2_03_train,vec_std_mean_reaction_time_Go_S1_07_S2_05_train,vec_std_mean_reaction_time_Go_S1_07_S2_07_train,vec_std_mean_reaction_time_Go_S1_07_S2_09_train],
                                        [vec_std_mean_reaction_time_Go_S1_09_S2_01_train,vec_std_mean_reaction_time_Go_S1_09_S2_03_train,vec_std_mean_reaction_time_Go_S1_09_S2_05_train,vec_std_mean_reaction_time_Go_S1_09_S2_07_train,vec_std_mean_reaction_time_Go_S1_09_S2_09_train]]

#test
vec_mean_mean_reaction_time_Go_test=    [[vec_mean_mean_reaction_time_Go_S1_01_S2_01_test,vec_mean_mean_reaction_time_Go_S1_01_S2_03_test,vec_mean_mean_reaction_time_Go_S1_01_S2_05_test,vec_mean_mean_reaction_time_Go_S1_01_S2_07_test,vec_mean_mean_reaction_time_Go_S1_01_S2_09_test],
                                         [vec_mean_mean_reaction_time_Go_S1_03_S2_01_test,vec_mean_mean_reaction_time_Go_S1_03_S2_03_test,vec_mean_mean_reaction_time_Go_S1_03_S2_05_test,vec_mean_mean_reaction_time_Go_S1_03_S2_07_test,vec_mean_mean_reaction_time_Go_S1_03_S2_09_test],
                                         [vec_mean_mean_reaction_time_Go_S1_05_S2_01_test,vec_mean_mean_reaction_time_Go_S1_05_S2_03_test,vec_mean_mean_reaction_time_Go_S1_05_S2_05_test,vec_mean_mean_reaction_time_Go_S1_05_S2_07_test,vec_mean_mean_reaction_time_Go_S1_05_S2_09_test],
                                         [vec_mean_mean_reaction_time_Go_S1_07_S2_01_test,vec_mean_mean_reaction_time_Go_S1_07_S2_03_test,vec_mean_mean_reaction_time_Go_S1_07_S2_05_test,vec_mean_mean_reaction_time_Go_S1_07_S2_07_test,vec_mean_mean_reaction_time_Go_S1_07_S2_09_test],
                                         [vec_mean_mean_reaction_time_Go_S1_09_S2_01_test,vec_mean_mean_reaction_time_Go_S1_09_S2_03_test,vec_mean_mean_reaction_time_Go_S1_09_S2_05_test,vec_mean_mean_reaction_time_Go_S1_09_S2_07_test,vec_mean_mean_reaction_time_Go_S1_09_S2_09_test]]

vec_std_mean_reaction_time_Go_test=    [[vec_std_mean_reaction_time_Go_S1_01_S2_01_test,vec_std_mean_reaction_time_Go_S1_01_S2_03_test,vec_std_mean_reaction_time_Go_S1_01_S2_05_test,vec_std_mean_reaction_time_Go_S1_01_S2_07_test,vec_std_mean_reaction_time_Go_S1_01_S2_09_test],
                                        [vec_std_mean_reaction_time_Go_S1_03_S2_01_test,vec_std_mean_reaction_time_Go_S1_03_S2_03_test,vec_std_mean_reaction_time_Go_S1_03_S2_05_test,vec_std_mean_reaction_time_Go_S1_03_S2_07_test,vec_std_mean_reaction_time_Go_S1_03_S2_09_test],
                                        [vec_std_mean_reaction_time_Go_S1_05_S2_01_test,vec_std_mean_reaction_time_Go_S1_05_S2_03_test,vec_std_mean_reaction_time_Go_S1_05_S2_05_test,vec_std_mean_reaction_time_Go_S1_05_S2_07_test,vec_std_mean_reaction_time_Go_S1_05_S2_09_test],
                                        [vec_std_mean_reaction_time_Go_S1_07_S2_01_test,vec_std_mean_reaction_time_Go_S1_07_S2_03_test,vec_std_mean_reaction_time_Go_S1_07_S2_05_test,vec_std_mean_reaction_time_Go_S1_07_S2_07_test,vec_std_mean_reaction_time_Go_S1_07_S2_09_test],
                                        [vec_std_mean_reaction_time_Go_S1_09_S2_01_test,vec_std_mean_reaction_time_Go_S1_09_S2_03_test,vec_std_mean_reaction_time_Go_S1_09_S2_05_test,vec_std_mean_reaction_time_Go_S1_09_S2_07_test,vec_std_mean_reaction_time_Go_S1_09_S2_09_test]]

D1_marg_vec_mean_mean_reaction_time_Go_test=np.mean(vec_mean_mean_reaction_time_Go_test,1)
D2_marg_vec_mean_mean_reaction_time_Go_test=np.mean(vec_mean_mean_reaction_time_Go_test,0)

#reaction time Hold failure
#training
vec_mean_mean_reaction_time_Hold_training=[[vec_mean_mean_reaction_time_Hold_S1_01_S2_01_train,vec_mean_mean_reaction_time_Hold_S1_01_S2_03_train,vec_mean_mean_reaction_time_Hold_S1_01_S2_05_train,vec_mean_mean_reaction_time_Hold_S1_01_S2_07_train,vec_mean_mean_reaction_time_Hold_S1_01_S2_09_train],
                                           [vec_mean_mean_reaction_time_Hold_S1_03_S2_01_train,vec_mean_mean_reaction_time_Hold_S1_03_S2_03_train,vec_mean_mean_reaction_time_Hold_S1_03_S2_05_train,vec_mean_mean_reaction_time_Hold_S1_03_S2_07_train,vec_mean_mean_reaction_time_Hold_S1_03_S2_09_train],
                                           [vec_mean_mean_reaction_time_Hold_S1_05_S2_01_train,vec_mean_mean_reaction_time_Hold_S1_05_S2_03_train,vec_mean_mean_reaction_time_Hold_S1_05_S2_05_train,vec_mean_mean_reaction_time_Hold_S1_05_S2_07_train,vec_mean_mean_reaction_time_Hold_S1_05_S2_09_train],
                                           [vec_mean_mean_reaction_time_Hold_S1_07_S2_01_train,vec_mean_mean_reaction_time_Hold_S1_07_S2_03_train,vec_mean_mean_reaction_time_Hold_S1_07_S2_05_train,vec_mean_mean_reaction_time_Hold_S1_07_S2_07_train,vec_mean_mean_reaction_time_Hold_S1_07_S2_09_train],
                                           [vec_mean_mean_reaction_time_Hold_S1_09_S2_01_train,vec_mean_mean_reaction_time_Hold_S1_09_S2_03_train,vec_mean_mean_reaction_time_Hold_S1_09_S2_05_train,vec_mean_mean_reaction_time_Hold_S1_09_S2_07_train,vec_mean_mean_reaction_time_Hold_S1_09_S2_09_train]]

vec_std_mean_reaction_time_Hold_training=[[vec_std_mean_reaction_time_Hold_S1_01_S2_01_train,vec_std_mean_reaction_time_Hold_S1_01_S2_03_train,vec_std_mean_reaction_time_Hold_S1_01_S2_05_train,vec_std_mean_reaction_time_Hold_S1_01_S2_07_train,vec_std_mean_reaction_time_Hold_S1_01_S2_09_train],
                                          [vec_std_mean_reaction_time_Hold_S1_03_S2_01_train,vec_std_mean_reaction_time_Hold_S1_03_S2_03_train,vec_std_mean_reaction_time_Hold_S1_03_S2_05_train,vec_std_mean_reaction_time_Hold_S1_03_S2_07_train,vec_std_mean_reaction_time_Hold_S1_03_S2_09_train],
                                          [vec_std_mean_reaction_time_Hold_S1_05_S2_01_train,vec_std_mean_reaction_time_Hold_S1_05_S2_03_train,vec_std_mean_reaction_time_Hold_S1_05_S2_05_train,vec_std_mean_reaction_time_Hold_S1_05_S2_07_train,vec_std_mean_reaction_time_Hold_S1_05_S2_09_train],
                                          [vec_std_mean_reaction_time_Hold_S1_07_S2_01_train,vec_std_mean_reaction_time_Hold_S1_07_S2_03_train,vec_std_mean_reaction_time_Hold_S1_07_S2_05_train,vec_std_mean_reaction_time_Hold_S1_07_S2_07_train,vec_std_mean_reaction_time_Hold_S1_07_S2_09_train],
                                          [vec_std_mean_reaction_time_Hold_S1_09_S2_01_train,vec_std_mean_reaction_time_Hold_S1_09_S2_03_train,vec_std_mean_reaction_time_Hold_S1_09_S2_05_train,vec_std_mean_reaction_time_Hold_S1_09_S2_07_train,vec_std_mean_reaction_time_Hold_S1_09_S2_09_train]]
#test
vec_mean_mean_reaction_time_Hold_test=  [[vec_mean_mean_reaction_time_Hold_S1_01_S2_01_test,vec_mean_mean_reaction_time_Hold_S1_01_S2_03_test,vec_mean_mean_reaction_time_Hold_S1_01_S2_05_test,vec_mean_mean_reaction_time_Hold_S1_01_S2_07_test,vec_mean_mean_reaction_time_Hold_S1_01_S2_09_test],
                                         [vec_mean_mean_reaction_time_Hold_S1_03_S2_01_test,vec_mean_mean_reaction_time_Hold_S1_03_S2_03_test,vec_mean_mean_reaction_time_Hold_S1_03_S2_05_test,vec_mean_mean_reaction_time_Hold_S1_03_S2_07_test,vec_mean_mean_reaction_time_Hold_S1_03_S2_09_test],
                                         [vec_mean_mean_reaction_time_Hold_S1_05_S2_01_test,vec_mean_mean_reaction_time_Hold_S1_05_S2_03_test,vec_mean_mean_reaction_time_Hold_S1_05_S2_05_test,vec_mean_mean_reaction_time_Hold_S1_05_S2_07_test,vec_mean_mean_reaction_time_Hold_S1_05_S2_09_test],
                                         [vec_mean_mean_reaction_time_Hold_S1_07_S2_01_test,vec_mean_mean_reaction_time_Hold_S1_07_S2_03_test,vec_mean_mean_reaction_time_Hold_S1_07_S2_05_test,vec_mean_mean_reaction_time_Hold_S1_07_S2_07_test,vec_mean_mean_reaction_time_Hold_S1_07_S2_09_test],
                                         [vec_mean_mean_reaction_time_Hold_S1_09_S2_01_test,vec_mean_mean_reaction_time_Hold_S1_09_S2_03_test,vec_mean_mean_reaction_time_Hold_S1_09_S2_05_test,vec_mean_mean_reaction_time_Hold_S1_09_S2_07_test,vec_mean_mean_reaction_time_Hold_S1_09_S2_09_test]]

vec_std_mean_reaction_time_Hold_test=  [[vec_std_mean_reaction_time_Hold_S1_01_S2_01_test,vec_std_mean_reaction_time_Hold_S1_01_S2_03_test,vec_std_mean_reaction_time_Hold_S1_01_S2_05_test,vec_std_mean_reaction_time_Hold_S1_01_S2_07_test,vec_std_mean_reaction_time_Hold_S1_01_S2_09_test],
                                        [vec_std_mean_reaction_time_Hold_S1_03_S2_01_test,vec_std_mean_reaction_time_Hold_S1_03_S2_03_test,vec_std_mean_reaction_time_Hold_S1_03_S2_05_test,vec_std_mean_reaction_time_Hold_S1_03_S2_07_test,vec_std_mean_reaction_time_Hold_S1_03_S2_09_test],
                                        [vec_std_mean_reaction_time_Hold_S1_05_S2_01_test,vec_std_mean_reaction_time_Hold_S1_05_S2_03_test,vec_std_mean_reaction_time_Hold_S1_05_S2_05_test,vec_std_mean_reaction_time_Hold_S1_05_S2_07_test,vec_std_mean_reaction_time_Hold_S1_05_S2_09_test],
                                        [vec_std_mean_reaction_time_Hold_S1_07_S2_01_test,vec_std_mean_reaction_time_Hold_S1_07_S2_03_test,vec_std_mean_reaction_time_Hold_S1_07_S2_05_test,vec_std_mean_reaction_time_Hold_S1_07_S2_07_test,vec_std_mean_reaction_time_Hold_S1_07_S2_09_test],
                                        [vec_std_mean_reaction_time_Hold_S1_09_S2_01_test,vec_std_mean_reaction_time_Hold_S1_09_S2_03_test,vec_std_mean_reaction_time_Hold_S1_09_S2_05_test,vec_std_mean_reaction_time_Hold_S1_09_S2_07_test,vec_std_mean_reaction_time_Hold_S1_09_S2_09_test]]

D1_marg_vec_mean_mean_reaction_time_Hold_test=np.mean(vec_mean_mean_reaction_time_Hold_test,1)
D2_marg_vec_mean_mean_reaction_time_Hold_test=np.mean(vec_mean_mean_reaction_time_Hold_test,0)

#reaction time Hold correct
#training
vec_mean_mean_reaction_time_Hold_correct_training=[[vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_01_train,vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_03_train,vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_05_train,vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_07_train,vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_09_train],
                                                   [vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_01_train,vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_03_train,vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_05_train,vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_07_train,vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_09_train],
                                                   [vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_01_train,vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_03_train,vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_05_train,vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_07_train,vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_09_train],
                                                   [vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_01_train,vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_03_train,vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_05_train,vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_07_train,vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_09_train],
                                                   [vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_01_train,vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_03_train,vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_05_train,vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_07_train,vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_09_train]]

vec_std_mean_reaction_time_Hold_correct_training=[[vec_std_mean_reaction_time_Hold_correct_S1_01_S2_01_train,vec_std_mean_reaction_time_Hold_correct_S1_01_S2_03_train,vec_std_mean_reaction_time_Hold_correct_S1_01_S2_05_train,vec_std_mean_reaction_time_Hold_correct_S1_01_S2_07_train,vec_std_mean_reaction_time_Hold_correct_S1_01_S2_09_train],
                                                  [vec_std_mean_reaction_time_Hold_correct_S1_03_S2_01_train,vec_std_mean_reaction_time_Hold_correct_S1_03_S2_03_train,vec_std_mean_reaction_time_Hold_correct_S1_03_S2_05_train,vec_std_mean_reaction_time_Hold_correct_S1_03_S2_07_train,vec_std_mean_reaction_time_Hold_correct_S1_03_S2_09_train],
                                                  [vec_std_mean_reaction_time_Hold_correct_S1_05_S2_01_train,vec_std_mean_reaction_time_Hold_correct_S1_05_S2_03_train,vec_std_mean_reaction_time_Hold_correct_S1_05_S2_05_train,vec_std_mean_reaction_time_Hold_correct_S1_05_S2_07_train,vec_std_mean_reaction_time_Hold_correct_S1_05_S2_09_train],
                                                  [vec_std_mean_reaction_time_Hold_correct_S1_07_S2_01_train,vec_std_mean_reaction_time_Hold_correct_S1_07_S2_03_train,vec_std_mean_reaction_time_Hold_correct_S1_07_S2_05_train,vec_std_mean_reaction_time_Hold_correct_S1_07_S2_07_train,vec_std_mean_reaction_time_Hold_correct_S1_07_S2_09_train],
                                                  [vec_std_mean_reaction_time_Hold_correct_S1_09_S2_01_train,vec_std_mean_reaction_time_Hold_correct_S1_09_S2_03_train,vec_std_mean_reaction_time_Hold_correct_S1_09_S2_05_train,vec_std_mean_reaction_time_Hold_correct_S1_09_S2_07_train,vec_std_mean_reaction_time_Hold_correct_S1_09_S2_09_train]]
#test
vec_mean_mean_reaction_time_Hold_correct_test=  [[vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_01_test,vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_03_test,vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_05_test,vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_07_test,vec_mean_mean_reaction_time_Hold_correct_S1_01_S2_09_test],
                                                 [vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_01_test,vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_03_test,vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_05_test,vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_07_test,vec_mean_mean_reaction_time_Hold_correct_S1_03_S2_09_test],
                                                 [vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_01_test,vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_03_test,vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_05_test,vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_07_test,vec_mean_mean_reaction_time_Hold_correct_S1_05_S2_09_test],
                                                 [vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_01_test,vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_03_test,vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_05_test,vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_07_test,vec_mean_mean_reaction_time_Hold_correct_S1_07_S2_09_test],
                                                 [vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_01_test,vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_03_test,vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_05_test,vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_07_test,vec_mean_mean_reaction_time_Hold_correct_S1_09_S2_09_test]]

vec_std_mean_reaction_time_Hold_correct_test=  [[vec_std_mean_reaction_time_Hold_correct_S1_01_S2_01_test,vec_std_mean_reaction_time_Hold_correct_S1_01_S2_03_test,vec_std_mean_reaction_time_Hold_correct_S1_01_S2_05_test,vec_std_mean_reaction_time_Hold_correct_S1_01_S2_07_test,vec_std_mean_reaction_time_Hold_correct_S1_01_S2_09_test],
                                                [vec_std_mean_reaction_time_Hold_correct_S1_03_S2_01_test,vec_std_mean_reaction_time_Hold_correct_S1_03_S2_03_test,vec_std_mean_reaction_time_Hold_correct_S1_03_S2_05_test,vec_std_mean_reaction_time_Hold_correct_S1_03_S2_07_test,vec_std_mean_reaction_time_Hold_correct_S1_03_S2_09_test],
                                                [vec_std_mean_reaction_time_Hold_correct_S1_05_S2_01_test,vec_std_mean_reaction_time_Hold_correct_S1_05_S2_03_test,vec_std_mean_reaction_time_Hold_correct_S1_05_S2_05_test,vec_std_mean_reaction_time_Hold_correct_S1_05_S2_07_test,vec_std_mean_reaction_time_Hold_correct_S1_05_S2_09_test],
                                                [vec_std_mean_reaction_time_Hold_correct_S1_07_S2_01_test,vec_std_mean_reaction_time_Hold_correct_S1_07_S2_03_test,vec_std_mean_reaction_time_Hold_correct_S1_07_S2_05_test,vec_std_mean_reaction_time_Hold_correct_S1_07_S2_07_test,vec_std_mean_reaction_time_Hold_correct_S1_07_S2_09_test],
                                                [vec_std_mean_reaction_time_Hold_correct_S1_09_S2_01_test,vec_std_mean_reaction_time_Hold_correct_S1_09_S2_03_test,vec_std_mean_reaction_time_Hold_correct_S1_09_S2_05_test,vec_std_mean_reaction_time_Hold_correct_S1_09_S2_07_test,vec_std_mean_reaction_time_Hold_correct_S1_09_S2_09_test]]

D1_marg_vec_mean_mean_reaction_time_Hold_correct_test=np.mean(vec_mean_mean_reaction_time_Hold_correct_test,1)
D2_marg_vec_mean_mean_reaction_time_Hold_correct_test=np.mean(vec_mean_mean_reaction_time_Hold_correct_test,0)

#reaction time Hold total
#training
vec_mean_mean_reaction_time_Hold_total_training=  [[vec_mean_mean_reaction_time_Hold_total_S1_01_S2_01_train,vec_mean_mean_reaction_time_Hold_total_S1_01_S2_03_train,vec_mean_mean_reaction_time_Hold_total_S1_01_S2_05_train,vec_mean_mean_reaction_time_Hold_total_S1_01_S2_07_train,vec_mean_mean_reaction_time_Hold_total_S1_01_S2_09_train],
                                                   [vec_mean_mean_reaction_time_Hold_total_S1_03_S2_01_train,vec_mean_mean_reaction_time_Hold_total_S1_03_S2_03_train,vec_mean_mean_reaction_time_Hold_total_S1_03_S2_05_train,vec_mean_mean_reaction_time_Hold_total_S1_03_S2_07_train,vec_mean_mean_reaction_time_Hold_total_S1_03_S2_09_train],
                                                   [vec_mean_mean_reaction_time_Hold_total_S1_05_S2_01_train,vec_mean_mean_reaction_time_Hold_total_S1_05_S2_03_train,vec_mean_mean_reaction_time_Hold_total_S1_05_S2_05_train,vec_mean_mean_reaction_time_Hold_total_S1_05_S2_07_train,vec_mean_mean_reaction_time_Hold_total_S1_05_S2_09_train],
                                                   [vec_mean_mean_reaction_time_Hold_total_S1_07_S2_01_train,vec_mean_mean_reaction_time_Hold_total_S1_07_S2_03_train,vec_mean_mean_reaction_time_Hold_total_S1_07_S2_05_train,vec_mean_mean_reaction_time_Hold_total_S1_07_S2_07_train,vec_mean_mean_reaction_time_Hold_total_S1_07_S2_09_train],
                                                   [vec_mean_mean_reaction_time_Hold_total_S1_09_S2_01_train,vec_mean_mean_reaction_time_Hold_total_S1_09_S2_03_train,vec_mean_mean_reaction_time_Hold_total_S1_09_S2_05_train,vec_mean_mean_reaction_time_Hold_total_S1_09_S2_07_train,vec_mean_mean_reaction_time_Hold_total_S1_09_S2_09_train]]

vec_std_mean_reaction_time_Hold_total_training=  [[vec_std_mean_reaction_time_Hold_total_S1_01_S2_01_train,vec_std_mean_reaction_time_Hold_total_S1_01_S2_03_train,vec_std_mean_reaction_time_Hold_total_S1_01_S2_05_train,vec_std_mean_reaction_time_Hold_total_S1_01_S2_07_train,vec_std_mean_reaction_time_Hold_total_S1_01_S2_09_train],
                                                  [vec_std_mean_reaction_time_Hold_total_S1_03_S2_01_train,vec_std_mean_reaction_time_Hold_total_S1_03_S2_03_train,vec_std_mean_reaction_time_Hold_total_S1_03_S2_05_train,vec_std_mean_reaction_time_Hold_total_S1_03_S2_07_train,vec_std_mean_reaction_time_Hold_total_S1_03_S2_09_train],
                                                  [vec_std_mean_reaction_time_Hold_total_S1_05_S2_01_train,vec_std_mean_reaction_time_Hold_total_S1_05_S2_03_train,vec_std_mean_reaction_time_Hold_total_S1_05_S2_05_train,vec_std_mean_reaction_time_Hold_total_S1_05_S2_07_train,vec_std_mean_reaction_time_Hold_total_S1_05_S2_09_train],
                                                  [vec_std_mean_reaction_time_Hold_total_S1_07_S2_01_train,vec_std_mean_reaction_time_Hold_total_S1_07_S2_03_train,vec_std_mean_reaction_time_Hold_total_S1_07_S2_05_train,vec_std_mean_reaction_time_Hold_total_S1_07_S2_07_train,vec_std_mean_reaction_time_Hold_total_S1_07_S2_09_train],
                                                  [vec_std_mean_reaction_time_Hold_total_S1_09_S2_01_train,vec_std_mean_reaction_time_Hold_total_S1_09_S2_03_train,vec_std_mean_reaction_time_Hold_total_S1_09_S2_05_train,vec_std_mean_reaction_time_Hold_total_S1_09_S2_07_train,vec_std_mean_reaction_time_Hold_total_S1_09_S2_09_train]]
#test
vec_mean_mean_reaction_time_Hold_total_test=    [[vec_mean_mean_reaction_time_Hold_total_S1_01_S2_01_test,vec_mean_mean_reaction_time_Hold_total_S1_01_S2_03_test,vec_mean_mean_reaction_time_Hold_total_S1_01_S2_05_test,vec_mean_mean_reaction_time_Hold_total_S1_01_S2_07_test,vec_mean_mean_reaction_time_Hold_total_S1_01_S2_09_test],
                                                 [vec_mean_mean_reaction_time_Hold_total_S1_03_S2_01_test,vec_mean_mean_reaction_time_Hold_total_S1_03_S2_03_test,vec_mean_mean_reaction_time_Hold_total_S1_03_S2_05_test,vec_mean_mean_reaction_time_Hold_total_S1_03_S2_07_test,vec_mean_mean_reaction_time_Hold_total_S1_03_S2_09_test],
                                                 [vec_mean_mean_reaction_time_Hold_total_S1_05_S2_01_test,vec_mean_mean_reaction_time_Hold_total_S1_05_S2_03_test,vec_mean_mean_reaction_time_Hold_total_S1_05_S2_05_test,vec_mean_mean_reaction_time_Hold_total_S1_05_S2_07_test,vec_mean_mean_reaction_time_Hold_total_S1_05_S2_09_test],
                                                 [vec_mean_mean_reaction_time_Hold_total_S1_07_S2_01_test,vec_mean_mean_reaction_time_Hold_total_S1_07_S2_03_test,vec_mean_mean_reaction_time_Hold_total_S1_07_S2_05_test,vec_mean_mean_reaction_time_Hold_total_S1_07_S2_07_test,vec_mean_mean_reaction_time_Hold_total_S1_07_S2_09_test],
                                                 [vec_mean_mean_reaction_time_Hold_total_S1_09_S2_01_test,vec_mean_mean_reaction_time_Hold_total_S1_09_S2_03_test,vec_mean_mean_reaction_time_Hold_total_S1_09_S2_05_test,vec_mean_mean_reaction_time_Hold_total_S1_09_S2_07_test,vec_mean_mean_reaction_time_Hold_total_S1_09_S2_09_test]]

vec_std_mean_reaction_time_Hold_total_test=    [[vec_std_mean_reaction_time_Hold_total_S1_01_S2_01_test,vec_std_mean_reaction_time_Hold_total_S1_01_S2_03_test,vec_std_mean_reaction_time_Hold_total_S1_01_S2_05_test,vec_std_mean_reaction_time_Hold_total_S1_01_S2_07_test,vec_std_mean_reaction_time_Hold_total_S1_01_S2_09_test],
                                                [vec_std_mean_reaction_time_Hold_total_S1_03_S2_01_test,vec_std_mean_reaction_time_Hold_total_S1_03_S2_03_test,vec_std_mean_reaction_time_Hold_total_S1_03_S2_05_test,vec_std_mean_reaction_time_Hold_total_S1_03_S2_07_test,vec_std_mean_reaction_time_Hold_total_S1_03_S2_09_test],
                                                [vec_std_mean_reaction_time_Hold_total_S1_05_S2_01_test,vec_std_mean_reaction_time_Hold_total_S1_05_S2_03_test,vec_std_mean_reaction_time_Hold_total_S1_05_S2_05_test,vec_std_mean_reaction_time_Hold_total_S1_05_S2_07_test,vec_std_mean_reaction_time_Hold_total_S1_05_S2_09_test],
                                                [vec_std_mean_reaction_time_Hold_total_S1_07_S2_01_test,vec_std_mean_reaction_time_Hold_total_S1_07_S2_03_test,vec_std_mean_reaction_time_Hold_total_S1_07_S2_05_test,vec_std_mean_reaction_time_Hold_total_S1_07_S2_07_test,vec_std_mean_reaction_time_Hold_total_S1_07_S2_09_test],
                                                [vec_std_mean_reaction_time_Hold_total_S1_09_S2_01_test,vec_std_mean_reaction_time_Hold_total_S1_09_S2_03_test,vec_std_mean_reaction_time_Hold_total_S1_09_S2_05_test,vec_std_mean_reaction_time_Hold_total_S1_09_S2_07_test,vec_std_mean_reaction_time_Hold_total_S1_09_S2_09_test]]

D1_marg_vec_mean_mean_reaction_time_Hold_total_test=np.mean(vec_mean_mean_reaction_time_Hold_total_test,1)
D2_marg_vec_mean_mean_reaction_time_Hold_total_test=np.mean(vec_mean_mean_reaction_time_Hold_total_test,0)

#max PMC Go
#training
vec_mean_mean_max_PMC_Go_training=[[vec_mean_mean_max_PMC_Go_S1_01_S2_01_train,vec_mean_mean_max_PMC_Go_S1_01_S2_03_train,vec_mean_mean_max_PMC_Go_S1_01_S2_05_train,vec_mean_mean_max_PMC_Go_S1_01_S2_07_train,vec_mean_mean_max_PMC_Go_S1_01_S2_09_train],
                                   [vec_mean_mean_max_PMC_Go_S1_03_S2_01_train,vec_mean_mean_max_PMC_Go_S1_03_S2_03_train,vec_mean_mean_max_PMC_Go_S1_03_S2_05_train,vec_mean_mean_max_PMC_Go_S1_03_S2_07_train,vec_mean_mean_max_PMC_Go_S1_03_S2_09_train],
                                   [vec_mean_mean_max_PMC_Go_S1_05_S2_01_train,vec_mean_mean_max_PMC_Go_S1_05_S2_03_train,vec_mean_mean_max_PMC_Go_S1_05_S2_05_train,vec_mean_mean_max_PMC_Go_S1_05_S2_07_train,vec_mean_mean_max_PMC_Go_S1_05_S2_09_train],
                                   [vec_mean_mean_max_PMC_Go_S1_07_S2_01_train,vec_mean_mean_max_PMC_Go_S1_07_S2_03_train,vec_mean_mean_max_PMC_Go_S1_07_S2_05_train,vec_mean_mean_max_PMC_Go_S1_07_S2_07_train,vec_mean_mean_max_PMC_Go_S1_07_S2_09_train],
                                   [vec_mean_mean_max_PMC_Go_S1_09_S2_01_train,vec_mean_mean_max_PMC_Go_S1_09_S2_03_train,vec_mean_mean_max_PMC_Go_S1_09_S2_05_train,vec_mean_mean_max_PMC_Go_S1_09_S2_07_train,vec_mean_mean_max_PMC_Go_S1_09_S2_09_train]]

vec_std_mean_max_PMC_Go_training=[[vec_std_mean_max_PMC_Go_S1_01_S2_01_train,vec_std_mean_max_PMC_Go_S1_01_S2_03_train,vec_std_mean_max_PMC_Go_S1_01_S2_05_train,vec_std_mean_max_PMC_Go_S1_01_S2_07_train,vec_std_mean_max_PMC_Go_S1_01_S2_09_train],
                                  [vec_std_mean_max_PMC_Go_S1_03_S2_01_train,vec_std_mean_max_PMC_Go_S1_03_S2_03_train,vec_std_mean_max_PMC_Go_S1_03_S2_05_train,vec_std_mean_max_PMC_Go_S1_03_S2_07_train,vec_std_mean_max_PMC_Go_S1_03_S2_09_train],
                                  [vec_std_mean_max_PMC_Go_S1_05_S2_01_train,vec_std_mean_max_PMC_Go_S1_05_S2_03_train,vec_std_mean_max_PMC_Go_S1_05_S2_05_train,vec_std_mean_max_PMC_Go_S1_05_S2_07_train,vec_std_mean_max_PMC_Go_S1_05_S2_09_train],
                                  [vec_std_mean_max_PMC_Go_S1_07_S2_01_train,vec_std_mean_max_PMC_Go_S1_07_S2_03_train,vec_std_mean_max_PMC_Go_S1_07_S2_05_train,vec_std_mean_max_PMC_Go_S1_07_S2_07_train,vec_std_mean_max_PMC_Go_S1_07_S2_09_train],
                                  [vec_std_mean_max_PMC_Go_S1_09_S2_01_train,vec_std_mean_max_PMC_Go_S1_09_S2_03_train,vec_std_mean_max_PMC_Go_S1_09_S2_05_train,vec_std_mean_max_PMC_Go_S1_09_S2_07_train,vec_std_mean_max_PMC_Go_S1_09_S2_09_train]]
#test
vec_mean_mean_max_PMC_Go_test=[[vec_mean_mean_max_PMC_Go_S1_01_S2_01_test,vec_mean_mean_max_PMC_Go_S1_01_S2_03_test,vec_mean_mean_max_PMC_Go_S1_01_S2_05_test,vec_mean_mean_max_PMC_Go_S1_01_S2_07_test,vec_mean_mean_max_PMC_Go_S1_01_S2_09_test],
                                   [vec_mean_mean_max_PMC_Go_S1_03_S2_01_test,vec_mean_mean_max_PMC_Go_S1_03_S2_03_test,vec_mean_mean_max_PMC_Go_S1_03_S2_05_test,vec_mean_mean_max_PMC_Go_S1_03_S2_07_test,vec_mean_mean_max_PMC_Go_S1_03_S2_09_test],
                                   [vec_mean_mean_max_PMC_Go_S1_05_S2_01_test,vec_mean_mean_max_PMC_Go_S1_05_S2_03_test,vec_mean_mean_max_PMC_Go_S1_05_S2_05_test,vec_mean_mean_max_PMC_Go_S1_05_S2_07_test,vec_mean_mean_max_PMC_Go_S1_05_S2_09_test],
                                   [vec_mean_mean_max_PMC_Go_S1_07_S2_01_test,vec_mean_mean_max_PMC_Go_S1_07_S2_03_test,vec_mean_mean_max_PMC_Go_S1_07_S2_05_test,vec_mean_mean_max_PMC_Go_S1_07_S2_07_test,vec_mean_mean_max_PMC_Go_S1_07_S2_09_test],
                                   [vec_mean_mean_max_PMC_Go_S1_09_S2_01_test,vec_mean_mean_max_PMC_Go_S1_09_S2_03_test,vec_mean_mean_max_PMC_Go_S1_09_S2_05_test,vec_mean_mean_max_PMC_Go_S1_09_S2_07_test,vec_mean_mean_max_PMC_Go_S1_09_S2_09_test]]

vec_std_mean_max_PMC_Go_test=[[vec_std_mean_max_PMC_Go_S1_01_S2_01_test,vec_std_mean_max_PMC_Go_S1_01_S2_03_test,vec_std_mean_max_PMC_Go_S1_01_S2_05_test,vec_std_mean_max_PMC_Go_S1_01_S2_07_test,vec_std_mean_max_PMC_Go_S1_01_S2_09_test],
                                  [vec_std_mean_max_PMC_Go_S1_03_S2_01_test,vec_std_mean_max_PMC_Go_S1_03_S2_03_test,vec_std_mean_max_PMC_Go_S1_03_S2_05_test,vec_std_mean_max_PMC_Go_S1_03_S2_07_test,vec_std_mean_max_PMC_Go_S1_03_S2_09_test],
                                  [vec_std_mean_max_PMC_Go_S1_05_S2_01_test,vec_std_mean_max_PMC_Go_S1_05_S2_03_test,vec_std_mean_max_PMC_Go_S1_05_S2_05_test,vec_std_mean_max_PMC_Go_S1_05_S2_07_test,vec_std_mean_max_PMC_Go_S1_05_S2_09_test],
                                  [vec_std_mean_max_PMC_Go_S1_07_S2_01_test,vec_std_mean_max_PMC_Go_S1_07_S2_03_test,vec_std_mean_max_PMC_Go_S1_07_S2_05_test,vec_std_mean_max_PMC_Go_S1_07_S2_07_test,vec_std_mean_max_PMC_Go_S1_07_S2_09_test],
                                  [vec_std_mean_max_PMC_Go_S1_09_S2_01_test,vec_std_mean_max_PMC_Go_S1_09_S2_03_test,vec_std_mean_max_PMC_Go_S1_09_S2_05_test,vec_std_mean_max_PMC_Go_S1_09_S2_07_test,vec_std_mean_max_PMC_Go_S1_09_S2_09_test]]

D1_marg_vec_mean_mean_max_PMC_Go_test=np.mean(vec_mean_mean_max_PMC_Go_test,1)
D2_marg_vec_mean_mean_max_PMC_Go_test=np.mean(vec_mean_mean_max_PMC_Go_test,0)

#geometric mean max PMC & Pmax 
vec_meanG_mean_max_PMC_Pmax_Go_training=[[vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_01_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_03_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_05_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_07_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_09_train],
                                         [vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_01_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_03_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_05_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_07_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_09_train],
                                         [vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_01_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_03_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_05_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_07_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_09_train],
                                         [vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_01_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_03_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_05_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_07_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_09_train],
                                         [vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_01_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_03_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_05_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_07_train,vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_09_train]]

vec_meanG_mean_max_PMC_Pmax_Go_test=    [[vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_01_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_03_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_05_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_07_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_01_S2_09_test],
                                         [vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_01_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_03_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_05_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_07_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_03_S2_09_test],
                                         [vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_01_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_03_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_05_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_07_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_05_S2_09_test],
                                         [vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_01_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_03_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_05_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_07_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_07_S2_09_test],
                                         [vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_01_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_03_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_05_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_07_test,vec_meanG_mean_max_PMC_Pmax_Go_S1_09_S2_09_test]]

D1_marg_vec_meanG_mean_max_PMC_Pmax_Go_test=np.mean(vec_meanG_mean_max_PMC_Pmax_Go_test,1)
D2_marg_vec_meanG_mean_max_PMC_Pmax_Go_test=np.mean(vec_meanG_mean_max_PMC_Pmax_Go_test,0)

vec_meanG_mean_max_PMC_Pmax_Hold_total_training=[[vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_01_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_03_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_05_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_07_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_09_train],
                                                 [vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_01_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_03_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_05_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_07_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_09_train],
                                                 [vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_01_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_03_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_05_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_07_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_09_train],
                                                 [vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_01_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_03_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_05_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_07_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_09_train],
                                                 [vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_01_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_03_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_05_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_07_train,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_09_train]]

vec_meanG_mean_max_PMC_Pmax_Hold_total_test=    [[vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_01_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_03_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_05_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_07_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_01_S2_09_test],
                                                 [vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_01_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_03_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_05_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_07_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_03_S2_09_test],
                                                 [vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_01_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_03_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_05_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_07_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_05_S2_09_test],
                                                 [vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_01_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_03_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_05_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_07_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_07_S2_09_test],
                                                 [vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_01_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_03_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_05_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_07_test,vec_meanG_mean_max_PMC_Pmax_Hold_total_S1_09_S2_09_test]]

D1_marg_vec_meanG_mean_max_PMC_Pmax_Hold_total_test=np.mean(vec_meanG_mean_max_PMC_Pmax_Hold_total_test,1)
D2_marg_vec_meanG_mean_max_PMC_Pmax_Hold_total_test=np.mean(vec_meanG_mean_max_PMC_Pmax_Hold_total_test,0)

#geometric mean max PMC & RT
#training
vec_meanG_mean_max_PMC_reaction_time_Go_training=[[vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_01_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_03_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_05_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_07_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_09_train],
                                                  [vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_01_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_03_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_05_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_07_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_09_train],
                                                  [vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_01_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_03_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_05_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_07_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_09_train],
                                                  [vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_01_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_03_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_05_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_07_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_09_train],
                                                  [vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_01_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_03_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_05_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_07_train,vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_09_train]]
#test
vec_meanG_mean_max_PMC_reaction_time_Go_test=    [[vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_01_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_03_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_05_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_07_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_01_S2_09_test],
                                                  [vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_01_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_03_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_05_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_07_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_03_S2_09_test],
                                                  [vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_01_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_03_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_05_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_07_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_05_S2_09_test],
                                                  [vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_01_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_03_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_05_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_07_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_07_S2_09_test],
                                                  [vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_01_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_03_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_05_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_07_test,vec_meanG_mean_max_PMC_reaction_time_Go_S1_09_S2_09_test]]

D1_marg_vec_meanG_mean_max_PMC_reaction_time_Go_test=np.mean(vec_meanG_mean_max_PMC_reaction_time_Go_test,1)
D2_marg_vec_meanG_mean_max_PMC_reaction_time_Go_test=np.mean(vec_meanG_mean_max_PMC_reaction_time_Go_test,0)

vec_meanG_mean_max_PMC_reaction_time_Hold_total_training=[[vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_01_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_03_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_05_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_07_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_09_train],
                                                          [vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_01_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_03_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_05_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_07_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_09_train],
                                                          [vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_01_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_03_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_05_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_07_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_09_train],
                                                          [vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_01_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_03_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_05_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_07_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_09_train],
                                                          [vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_01_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_03_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_05_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_07_train,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_09_train]]

vec_meanG_mean_max_PMC_reaction_time_Hold_total_test=    [[vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_01_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_03_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_05_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_07_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_01_S2_09_test],
                                                          [vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_01_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_03_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_05_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_07_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_03_S2_09_test],
                                                          [vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_01_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_03_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_05_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_07_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_05_S2_09_test],
                                                          [vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_01_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_03_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_05_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_07_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_07_S2_09_test],
                                                          [vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_01_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_03_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_05_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_07_test,vec_meanG_mean_max_PMC_reaction_time_Hold_total_S1_09_S2_09_test]]

D1_marg_vec_meanG_mean_max_PMC_reaction_time_Hold_total_test=np.mean(vec_meanG_mean_max_PMC_reaction_time_Hold_total_test,1)
D2_marg_vec_meanG_mean_max_PMC_reaction_time_Hold_total_test=np.mean(vec_meanG_mean_max_PMC_reaction_time_Hold_total_test,0)

#max PMC Hold failure
#training
vec_mean_mean_max_PMC_Hold_training=[[vec_mean_mean_max_PMC_Hold_S1_01_S2_01_train,vec_mean_mean_max_PMC_Hold_S1_01_S2_03_train,vec_mean_mean_max_PMC_Hold_S1_01_S2_05_train,vec_mean_mean_max_PMC_Hold_S1_01_S2_07_train,vec_mean_mean_max_PMC_Hold_S1_01_S2_09_train],
                                     [vec_mean_mean_max_PMC_Hold_S1_03_S2_01_train,vec_mean_mean_max_PMC_Hold_S1_03_S2_03_train,vec_mean_mean_max_PMC_Hold_S1_03_S2_05_train,vec_mean_mean_max_PMC_Hold_S1_03_S2_07_train,vec_mean_mean_max_PMC_Hold_S1_03_S2_09_train],
                                     [vec_mean_mean_max_PMC_Hold_S1_05_S2_01_train,vec_mean_mean_max_PMC_Hold_S1_05_S2_03_train,vec_mean_mean_max_PMC_Hold_S1_05_S2_05_train,vec_mean_mean_max_PMC_Hold_S1_05_S2_07_train,vec_mean_mean_max_PMC_Hold_S1_05_S2_09_train],
                                     [vec_mean_mean_max_PMC_Hold_S1_07_S2_01_train,vec_mean_mean_max_PMC_Hold_S1_07_S2_03_train,vec_mean_mean_max_PMC_Hold_S1_07_S2_05_train,vec_mean_mean_max_PMC_Hold_S1_07_S2_07_train,vec_mean_mean_max_PMC_Hold_S1_07_S2_09_train],
                                     [vec_mean_mean_max_PMC_Hold_S1_09_S2_01_train,vec_mean_mean_max_PMC_Hold_S1_09_S2_03_train,vec_mean_mean_max_PMC_Hold_S1_09_S2_05_train,vec_mean_mean_max_PMC_Hold_S1_09_S2_07_train,vec_mean_mean_max_PMC_Hold_S1_09_S2_09_train]]

vec_std_mean_max_PMC_Hold_training=[[vec_std_mean_max_PMC_Hold_S1_01_S2_01_train,vec_std_mean_max_PMC_Hold_S1_01_S2_03_train,vec_std_mean_max_PMC_Hold_S1_01_S2_05_train,vec_std_mean_max_PMC_Hold_S1_01_S2_07_train,vec_std_mean_max_PMC_Hold_S1_01_S2_09_train],
                                    [vec_std_mean_max_PMC_Hold_S1_03_S2_01_train,vec_std_mean_max_PMC_Hold_S1_03_S2_03_train,vec_std_mean_max_PMC_Hold_S1_03_S2_05_train,vec_std_mean_max_PMC_Hold_S1_03_S2_07_train,vec_std_mean_max_PMC_Hold_S1_03_S2_09_train],
                                    [vec_std_mean_max_PMC_Hold_S1_05_S2_01_train,vec_std_mean_max_PMC_Hold_S1_05_S2_03_train,vec_std_mean_max_PMC_Hold_S1_05_S2_05_train,vec_std_mean_max_PMC_Hold_S1_05_S2_07_train,vec_std_mean_max_PMC_Hold_S1_05_S2_09_train],
                                    [vec_std_mean_max_PMC_Hold_S1_07_S2_01_train,vec_std_mean_max_PMC_Hold_S1_07_S2_03_train,vec_std_mean_max_PMC_Hold_S1_07_S2_05_train,vec_std_mean_max_PMC_Hold_S1_07_S2_07_train,vec_std_mean_max_PMC_Hold_S1_07_S2_09_train],
                                    [vec_std_mean_max_PMC_Hold_S1_09_S2_01_train,vec_std_mean_max_PMC_Hold_S1_09_S2_03_train,vec_std_mean_max_PMC_Hold_S1_09_S2_05_train,vec_std_mean_max_PMC_Hold_S1_09_S2_07_train,vec_std_mean_max_PMC_Hold_S1_09_S2_09_train]]
#test
vec_mean_mean_max_PMC_Hold_test=  [[vec_mean_mean_max_PMC_Hold_S1_01_S2_01_test,vec_mean_mean_max_PMC_Hold_S1_01_S2_03_test,vec_mean_mean_max_PMC_Hold_S1_01_S2_05_test,vec_mean_mean_max_PMC_Hold_S1_01_S2_07_test,vec_mean_mean_max_PMC_Hold_S1_01_S2_09_test],
                                   [vec_mean_mean_max_PMC_Hold_S1_03_S2_01_test,vec_mean_mean_max_PMC_Hold_S1_03_S2_03_test,vec_mean_mean_max_PMC_Hold_S1_03_S2_05_test,vec_mean_mean_max_PMC_Hold_S1_03_S2_07_test,vec_mean_mean_max_PMC_Hold_S1_03_S2_09_test],
                                   [vec_mean_mean_max_PMC_Hold_S1_05_S2_01_test,vec_mean_mean_max_PMC_Hold_S1_05_S2_03_test,vec_mean_mean_max_PMC_Hold_S1_05_S2_05_test,vec_mean_mean_max_PMC_Hold_S1_05_S2_07_test,vec_mean_mean_max_PMC_Hold_S1_05_S2_09_test],
                                   [vec_mean_mean_max_PMC_Hold_S1_07_S2_01_test,vec_mean_mean_max_PMC_Hold_S1_07_S2_03_test,vec_mean_mean_max_PMC_Hold_S1_07_S2_05_test,vec_mean_mean_max_PMC_Hold_S1_07_S2_07_test,vec_mean_mean_max_PMC_Hold_S1_07_S2_09_test],
                                   [vec_mean_mean_max_PMC_Hold_S1_09_S2_01_test,vec_mean_mean_max_PMC_Hold_S1_09_S2_03_test,vec_mean_mean_max_PMC_Hold_S1_09_S2_05_test,vec_mean_mean_max_PMC_Hold_S1_09_S2_07_test,vec_mean_mean_max_PMC_Hold_S1_09_S2_09_test]]

vec_std_mean_max_PMC_Hold_test=  [[vec_std_mean_max_PMC_Hold_S1_01_S2_01_test,vec_std_mean_max_PMC_Hold_S1_01_S2_03_test,vec_std_mean_max_PMC_Hold_S1_01_S2_05_test,vec_std_mean_max_PMC_Hold_S1_01_S2_07_test,vec_std_mean_max_PMC_Hold_S1_01_S2_09_test],
                                  [vec_std_mean_max_PMC_Hold_S1_03_S2_01_test,vec_std_mean_max_PMC_Hold_S1_03_S2_03_test,vec_std_mean_max_PMC_Hold_S1_03_S2_05_test,vec_std_mean_max_PMC_Hold_S1_03_S2_07_test,vec_std_mean_max_PMC_Hold_S1_03_S2_09_test],
                                  [vec_std_mean_max_PMC_Hold_S1_05_S2_01_test,vec_std_mean_max_PMC_Hold_S1_05_S2_03_test,vec_std_mean_max_PMC_Hold_S1_05_S2_05_test,vec_std_mean_max_PMC_Hold_S1_05_S2_07_test,vec_std_mean_max_PMC_Hold_S1_05_S2_09_test],
                                  [vec_std_mean_max_PMC_Hold_S1_07_S2_01_test,vec_std_mean_max_PMC_Hold_S1_07_S2_03_test,vec_std_mean_max_PMC_Hold_S1_07_S2_05_test,vec_std_mean_max_PMC_Hold_S1_07_S2_07_test,vec_std_mean_max_PMC_Hold_S1_07_S2_09_test],
                                  [vec_std_mean_max_PMC_Hold_S1_09_S2_01_test,vec_std_mean_max_PMC_Hold_S1_09_S2_03_test,vec_std_mean_max_PMC_Hold_S1_09_S2_05_test,vec_std_mean_max_PMC_Hold_S1_09_S2_07_test,vec_std_mean_max_PMC_Hold_S1_09_S2_09_test]]

D1_marg_vec_mean_mean_max_PMC_Hold_test=np.mean(vec_mean_mean_max_PMC_Hold_test,1)
D2_marg_vec_mean_mean_max_PMC_Hold_test=np.mean(vec_mean_mean_max_PMC_Hold_test,0)

#max PMC Hold correct
#training
vec_mean_mean_max_PMC_Hold_correct_training=[[vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_01_train,vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_03_train,vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_05_train,vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_07_train,vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_09_train],
                                             [vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_01_train,vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_03_train,vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_05_train,vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_07_train,vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_09_train],
                                             [vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_01_train,vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_03_train,vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_05_train,vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_07_train,vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_09_train],
                                             [vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_01_train,vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_03_train,vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_05_train,vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_07_train,vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_09_train],
                                             [vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_01_train,vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_03_train,vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_05_train,vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_07_train,vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_09_train]]


vec_std_mean_max_PMC_Hold_correct_training=[[vec_std_mean_max_PMC_Hold_correct_S1_01_S2_01_train,vec_std_mean_max_PMC_Hold_correct_S1_01_S2_03_train,vec_std_mean_max_PMC_Hold_correct_S1_01_S2_05_train,vec_std_mean_max_PMC_Hold_correct_S1_01_S2_07_train,vec_std_mean_max_PMC_Hold_correct_S1_01_S2_09_train],
                                            [vec_std_mean_max_PMC_Hold_correct_S1_03_S2_01_train,vec_std_mean_max_PMC_Hold_correct_S1_03_S2_03_train,vec_std_mean_max_PMC_Hold_correct_S1_03_S2_05_train,vec_std_mean_max_PMC_Hold_correct_S1_03_S2_07_train,vec_std_mean_max_PMC_Hold_correct_S1_03_S2_09_train],
                                            [vec_std_mean_max_PMC_Hold_correct_S1_05_S2_01_train,vec_std_mean_max_PMC_Hold_correct_S1_05_S2_03_train,vec_std_mean_max_PMC_Hold_correct_S1_05_S2_05_train,vec_std_mean_max_PMC_Hold_correct_S1_05_S2_07_train,vec_std_mean_max_PMC_Hold_correct_S1_05_S2_09_train],
                                            [vec_std_mean_max_PMC_Hold_correct_S1_07_S2_01_train,vec_std_mean_max_PMC_Hold_correct_S1_07_S2_03_train,vec_std_mean_max_PMC_Hold_correct_S1_07_S2_05_train,vec_std_mean_max_PMC_Hold_correct_S1_07_S2_07_train,vec_std_mean_max_PMC_Hold_correct_S1_07_S2_09_train],
                                            [vec_std_mean_max_PMC_Hold_correct_S1_09_S2_01_train,vec_std_mean_max_PMC_Hold_correct_S1_09_S2_03_train,vec_std_mean_max_PMC_Hold_correct_S1_09_S2_05_train,vec_std_mean_max_PMC_Hold_correct_S1_09_S2_07_train,vec_std_mean_max_PMC_Hold_correct_S1_09_S2_09_train]]
#test
vec_mean_mean_max_PMC_Hold_correct_test=  [[vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_01_test,vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_03_test,vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_05_test,vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_07_test,vec_mean_mean_max_PMC_Hold_correct_S1_01_S2_09_test],
                                           [vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_01_test,vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_03_test,vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_05_test,vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_07_test,vec_mean_mean_max_PMC_Hold_correct_S1_03_S2_09_test],
                                           [vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_01_test,vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_03_test,vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_05_test,vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_07_test,vec_mean_mean_max_PMC_Hold_correct_S1_05_S2_09_test],
                                           [vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_01_test,vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_03_test,vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_05_test,vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_07_test,vec_mean_mean_max_PMC_Hold_correct_S1_07_S2_09_test],
                                           [vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_01_test,vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_03_test,vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_05_test,vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_07_test,vec_mean_mean_max_PMC_Hold_correct_S1_09_S2_09_test]]

vec_std_mean_max_PMC_Hold_correct_test=  [[vec_std_mean_max_PMC_Hold_correct_S1_01_S2_01_test,vec_std_mean_max_PMC_Hold_correct_S1_01_S2_03_test,vec_std_mean_max_PMC_Hold_correct_S1_01_S2_05_test,vec_std_mean_max_PMC_Hold_correct_S1_01_S2_07_test,vec_std_mean_max_PMC_Hold_correct_S1_01_S2_09_test],
                                          [vec_std_mean_max_PMC_Hold_correct_S1_03_S2_01_test,vec_std_mean_max_PMC_Hold_correct_S1_03_S2_03_test,vec_std_mean_max_PMC_Hold_correct_S1_03_S2_05_test,vec_std_mean_max_PMC_Hold_correct_S1_03_S2_07_test,vec_std_mean_max_PMC_Hold_correct_S1_03_S2_09_test],
                                          [vec_std_mean_max_PMC_Hold_correct_S1_05_S2_01_test,vec_std_mean_max_PMC_Hold_correct_S1_05_S2_03_test,vec_std_mean_max_PMC_Hold_correct_S1_05_S2_05_test,vec_std_mean_max_PMC_Hold_correct_S1_05_S2_07_test,vec_std_mean_max_PMC_Hold_correct_S1_05_S2_09_test],
                                          [vec_std_mean_max_PMC_Hold_correct_S1_07_S2_01_test,vec_std_mean_max_PMC_Hold_correct_S1_07_S2_03_test,vec_std_mean_max_PMC_Hold_correct_S1_07_S2_05_test,vec_std_mean_max_PMC_Hold_correct_S1_07_S2_07_test,vec_std_mean_max_PMC_Hold_correct_S1_07_S2_09_test],
                                          [vec_std_mean_max_PMC_Hold_correct_S1_09_S2_01_test,vec_std_mean_max_PMC_Hold_correct_S1_09_S2_03_test,vec_std_mean_max_PMC_Hold_correct_S1_09_S2_05_test,vec_std_mean_max_PMC_Hold_correct_S1_09_S2_07_test,vec_std_mean_max_PMC_Hold_correct_S1_09_S2_09_test]]

D1_marg_vec_mean_mean_max_PMC_Hold_correct_test=np.mean(vec_mean_mean_max_PMC_Hold_correct_test,1)
D2_marg_vec_mean_mean_max_PMC_Hold_correct_test=np.mean(vec_mean_mean_max_PMC_Hold_correct_test,0)

#max PMC Hold total
#training
vec_mean_mean_max_PMC_Hold_total_training=[[vec_mean_mean_max_PMC_Hold_total_S1_01_S2_01_train,vec_mean_mean_max_PMC_Hold_total_S1_01_S2_03_train,vec_mean_mean_max_PMC_Hold_total_S1_01_S2_05_train,vec_mean_mean_max_PMC_Hold_total_S1_01_S2_07_train,vec_mean_mean_max_PMC_Hold_total_S1_01_S2_09_train],
                                           [vec_mean_mean_max_PMC_Hold_total_S1_03_S2_01_train,vec_mean_mean_max_PMC_Hold_total_S1_03_S2_03_train,vec_mean_mean_max_PMC_Hold_total_S1_03_S2_05_train,vec_mean_mean_max_PMC_Hold_total_S1_03_S2_07_train,vec_mean_mean_max_PMC_Hold_total_S1_03_S2_09_train],
                                           [vec_mean_mean_max_PMC_Hold_total_S1_05_S2_01_train,vec_mean_mean_max_PMC_Hold_total_S1_05_S2_03_train,vec_mean_mean_max_PMC_Hold_total_S1_05_S2_05_train,vec_mean_mean_max_PMC_Hold_total_S1_05_S2_07_train,vec_mean_mean_max_PMC_Hold_total_S1_05_S2_09_train],
                                           [vec_mean_mean_max_PMC_Hold_total_S1_07_S2_01_train,vec_mean_mean_max_PMC_Hold_total_S1_07_S2_03_train,vec_mean_mean_max_PMC_Hold_total_S1_07_S2_05_train,vec_mean_mean_max_PMC_Hold_total_S1_07_S2_07_train,vec_mean_mean_max_PMC_Hold_total_S1_07_S2_09_train],
                                           [vec_mean_mean_max_PMC_Hold_total_S1_09_S2_01_train,vec_mean_mean_max_PMC_Hold_total_S1_09_S2_03_train,vec_mean_mean_max_PMC_Hold_total_S1_09_S2_05_train,vec_mean_mean_max_PMC_Hold_total_S1_09_S2_07_train,vec_mean_mean_max_PMC_Hold_total_S1_09_S2_09_train]]


vec_std_mean_max_PMC_Hold_total_training=[[vec_std_mean_max_PMC_Hold_total_S1_01_S2_01_train,vec_std_mean_max_PMC_Hold_total_S1_01_S2_03_train,vec_std_mean_max_PMC_Hold_total_S1_01_S2_05_train,vec_std_mean_max_PMC_Hold_total_S1_01_S2_07_train,vec_std_mean_max_PMC_Hold_total_S1_01_S2_09_train],
                                          [vec_std_mean_max_PMC_Hold_total_S1_03_S2_01_train,vec_std_mean_max_PMC_Hold_total_S1_03_S2_03_train,vec_std_mean_max_PMC_Hold_total_S1_03_S2_05_train,vec_std_mean_max_PMC_Hold_total_S1_03_S2_07_train,vec_std_mean_max_PMC_Hold_total_S1_03_S2_09_train],
                                          [vec_std_mean_max_PMC_Hold_total_S1_05_S2_01_train,vec_std_mean_max_PMC_Hold_total_S1_05_S2_03_train,vec_std_mean_max_PMC_Hold_total_S1_05_S2_05_train,vec_std_mean_max_PMC_Hold_total_S1_05_S2_07_train,vec_std_mean_max_PMC_Hold_total_S1_05_S2_09_train],
                                          [vec_std_mean_max_PMC_Hold_total_S1_07_S2_01_train,vec_std_mean_max_PMC_Hold_total_S1_07_S2_03_train,vec_std_mean_max_PMC_Hold_total_S1_07_S2_05_train,vec_std_mean_max_PMC_Hold_total_S1_07_S2_07_train,vec_std_mean_max_PMC_Hold_total_S1_07_S2_09_train],
                                          [vec_std_mean_max_PMC_Hold_total_S1_09_S2_01_train,vec_std_mean_max_PMC_Hold_total_S1_09_S2_03_train,vec_std_mean_max_PMC_Hold_total_S1_09_S2_05_train,vec_std_mean_max_PMC_Hold_total_S1_09_S2_07_train,vec_std_mean_max_PMC_Hold_total_S1_09_S2_09_train]]

#test
vec_mean_mean_max_PMC_Hold_total_test=  [[vec_mean_mean_max_PMC_Hold_total_S1_01_S2_01_test,vec_mean_mean_max_PMC_Hold_total_S1_01_S2_03_test,vec_mean_mean_max_PMC_Hold_total_S1_01_S2_05_test,vec_mean_mean_max_PMC_Hold_total_S1_01_S2_07_test,vec_mean_mean_max_PMC_Hold_total_S1_01_S2_09_test],
                                         [vec_mean_mean_max_PMC_Hold_total_S1_03_S2_01_test,vec_mean_mean_max_PMC_Hold_total_S1_03_S2_03_test,vec_mean_mean_max_PMC_Hold_total_S1_03_S2_05_test,vec_mean_mean_max_PMC_Hold_total_S1_03_S2_07_test,vec_mean_mean_max_PMC_Hold_total_S1_03_S2_09_test],
                                         [vec_mean_mean_max_PMC_Hold_total_S1_05_S2_01_test,vec_mean_mean_max_PMC_Hold_total_S1_05_S2_03_test,vec_mean_mean_max_PMC_Hold_total_S1_05_S2_05_test,vec_mean_mean_max_PMC_Hold_total_S1_05_S2_07_test,vec_mean_mean_max_PMC_Hold_total_S1_05_S2_09_test],
                                         [vec_mean_mean_max_PMC_Hold_total_S1_07_S2_01_test,vec_mean_mean_max_PMC_Hold_total_S1_07_S2_03_test,vec_mean_mean_max_PMC_Hold_total_S1_07_S2_05_test,vec_mean_mean_max_PMC_Hold_total_S1_07_S2_07_test,vec_mean_mean_max_PMC_Hold_total_S1_07_S2_09_test],
                                         [vec_mean_mean_max_PMC_Hold_total_S1_09_S2_01_test,vec_mean_mean_max_PMC_Hold_total_S1_09_S2_03_test,vec_mean_mean_max_PMC_Hold_total_S1_09_S2_05_test,vec_mean_mean_max_PMC_Hold_total_S1_09_S2_07_test,vec_mean_mean_max_PMC_Hold_total_S1_09_S2_09_test]]

vec_std_mean_max_PMC_Hold_total_test=  [[vec_std_mean_max_PMC_Hold_total_S1_01_S2_01_test,vec_std_mean_max_PMC_Hold_total_S1_01_S2_03_test,vec_std_mean_max_PMC_Hold_total_S1_01_S2_05_test,vec_std_mean_max_PMC_Hold_total_S1_01_S2_07_test,vec_std_mean_max_PMC_Hold_total_S1_01_S2_09_test],
                                        [vec_std_mean_max_PMC_Hold_total_S1_03_S2_01_test,vec_std_mean_max_PMC_Hold_total_S1_03_S2_03_test,vec_std_mean_max_PMC_Hold_total_S1_03_S2_05_test,vec_std_mean_max_PMC_Hold_total_S1_03_S2_07_test,vec_std_mean_max_PMC_Hold_total_S1_03_S2_09_test],
                                        [vec_std_mean_max_PMC_Hold_total_S1_05_S2_01_test,vec_std_mean_max_PMC_Hold_total_S1_05_S2_03_test,vec_std_mean_max_PMC_Hold_total_S1_05_S2_05_test,vec_std_mean_max_PMC_Hold_total_S1_05_S2_07_test,vec_std_mean_max_PMC_Hold_total_S1_05_S2_09_test],
                                        [vec_std_mean_max_PMC_Hold_total_S1_07_S2_01_test,vec_std_mean_max_PMC_Hold_total_S1_07_S2_03_test,vec_std_mean_max_PMC_Hold_total_S1_07_S2_05_test,vec_std_mean_max_PMC_Hold_total_S1_07_S2_07_test,vec_std_mean_max_PMC_Hold_total_S1_07_S2_09_test],
                                        [vec_std_mean_max_PMC_Hold_total_S1_09_S2_01_test,vec_std_mean_max_PMC_Hold_total_S1_09_S2_03_test,vec_std_mean_max_PMC_Hold_total_S1_09_S2_05_test,vec_std_mean_max_PMC_Hold_total_S1_09_S2_07_test,vec_std_mean_max_PMC_Hold_total_S1_09_S2_09_test]]

D1_marg_vec_mean_mean_max_PMC_Hold_total_test=np.mean(vec_mean_mean_max_PMC_Hold_total_test,1)
D2_marg_vec_mean_mean_max_PMC_Hold_total_test=np.mean(vec_mean_mean_max_PMC_Hold_total_test,0)

#Pmax Go
#training
vec_mean_mean_Pmax_Go_training=   [[vec_mean_mean_Pmax_Go_S1_01_S2_01_train,vec_mean_mean_Pmax_Go_S1_01_S2_03_train,vec_mean_mean_Pmax_Go_S1_01_S2_05_train,vec_mean_mean_Pmax_Go_S1_01_S2_07_train,vec_mean_mean_Pmax_Go_S1_01_S2_09_train],
                                   [vec_mean_mean_Pmax_Go_S1_03_S2_01_train,vec_mean_mean_Pmax_Go_S1_03_S2_03_train,vec_mean_mean_Pmax_Go_S1_03_S2_05_train,vec_mean_mean_Pmax_Go_S1_03_S2_07_train,vec_mean_mean_Pmax_Go_S1_03_S2_09_train],
                                   [vec_mean_mean_Pmax_Go_S1_05_S2_01_train,vec_mean_mean_Pmax_Go_S1_05_S2_03_train,vec_mean_mean_Pmax_Go_S1_05_S2_05_train,vec_mean_mean_Pmax_Go_S1_05_S2_07_train,vec_mean_mean_Pmax_Go_S1_05_S2_09_train],
                                   [vec_mean_mean_Pmax_Go_S1_07_S2_01_train,vec_mean_mean_Pmax_Go_S1_07_S2_03_train,vec_mean_mean_Pmax_Go_S1_07_S2_05_train,vec_mean_mean_Pmax_Go_S1_07_S2_07_train,vec_mean_mean_Pmax_Go_S1_07_S2_09_train],
                                   [vec_mean_mean_Pmax_Go_S1_09_S2_01_train,vec_mean_mean_Pmax_Go_S1_09_S2_03_train,vec_mean_mean_Pmax_Go_S1_09_S2_05_train,vec_mean_mean_Pmax_Go_S1_09_S2_07_train,vec_mean_mean_Pmax_Go_S1_09_S2_09_train]]


vec_std_mean_Pmax_Go_training=   [[vec_std_mean_Pmax_Go_S1_01_S2_01_train,vec_std_mean_Pmax_Go_S1_01_S2_03_train,vec_std_mean_Pmax_Go_S1_01_S2_05_train,vec_std_mean_Pmax_Go_S1_01_S2_07_train,vec_std_mean_Pmax_Go_S1_01_S2_09_train],
                                  [vec_std_mean_Pmax_Go_S1_03_S2_01_train,vec_std_mean_Pmax_Go_S1_03_S2_03_train,vec_std_mean_Pmax_Go_S1_03_S2_05_train,vec_std_mean_Pmax_Go_S1_03_S2_07_train,vec_std_mean_Pmax_Go_S1_03_S2_09_train],
                                  [vec_std_mean_Pmax_Go_S1_05_S2_01_train,vec_std_mean_Pmax_Go_S1_05_S2_03_train,vec_std_mean_Pmax_Go_S1_05_S2_05_train,vec_std_mean_Pmax_Go_S1_05_S2_07_train,vec_std_mean_Pmax_Go_S1_05_S2_09_train],
                                  [vec_std_mean_Pmax_Go_S1_07_S2_01_train,vec_std_mean_Pmax_Go_S1_07_S2_03_train,vec_std_mean_Pmax_Go_S1_07_S2_05_train,vec_std_mean_Pmax_Go_S1_07_S2_07_train,vec_std_mean_Pmax_Go_S1_07_S2_09_train],
                                  [vec_std_mean_Pmax_Go_S1_09_S2_01_train,vec_std_mean_Pmax_Go_S1_09_S2_03_train,vec_std_mean_Pmax_Go_S1_09_S2_05_train,vec_std_mean_Pmax_Go_S1_09_S2_07_train,vec_std_mean_Pmax_Go_S1_09_S2_09_train]]
#test
vec_mean_mean_Pmax_Go_test=       [[vec_mean_mean_Pmax_Go_S1_01_S2_01_test,vec_mean_mean_Pmax_Go_S1_01_S2_03_test,vec_mean_mean_Pmax_Go_S1_01_S2_05_test,vec_mean_mean_Pmax_Go_S1_01_S2_07_test,vec_mean_mean_Pmax_Go_S1_01_S2_09_test],
                                   [vec_mean_mean_Pmax_Go_S1_03_S2_01_test,vec_mean_mean_Pmax_Go_S1_03_S2_03_test,vec_mean_mean_Pmax_Go_S1_03_S2_05_test,vec_mean_mean_Pmax_Go_S1_03_S2_07_test,vec_mean_mean_Pmax_Go_S1_03_S2_09_test],
                                   [vec_mean_mean_Pmax_Go_S1_05_S2_01_test,vec_mean_mean_Pmax_Go_S1_05_S2_03_test,vec_mean_mean_Pmax_Go_S1_05_S2_05_test,vec_mean_mean_Pmax_Go_S1_05_S2_07_test,vec_mean_mean_Pmax_Go_S1_05_S2_09_test],
                                   [vec_mean_mean_Pmax_Go_S1_07_S2_01_test,vec_mean_mean_Pmax_Go_S1_07_S2_03_test,vec_mean_mean_Pmax_Go_S1_07_S2_05_test,vec_mean_mean_Pmax_Go_S1_07_S2_07_test,vec_mean_mean_Pmax_Go_S1_07_S2_09_test],
                                   [vec_mean_mean_Pmax_Go_S1_09_S2_01_test,vec_mean_mean_Pmax_Go_S1_09_S2_03_test,vec_mean_mean_Pmax_Go_S1_09_S2_05_test,vec_mean_mean_Pmax_Go_S1_09_S2_07_test,vec_mean_mean_Pmax_Go_S1_09_S2_09_test]]

vec_std_mean_Pmax_Go_test=[[vec_std_mean_Pmax_Go_S1_01_S2_01_test,vec_std_mean_Pmax_Go_S1_01_S2_03_test,vec_std_mean_Pmax_Go_S1_01_S2_05_test,vec_std_mean_Pmax_Go_S1_01_S2_07_test,vec_std_mean_Pmax_Go_S1_01_S2_09_test],
                                  [vec_std_mean_Pmax_Go_S1_03_S2_01_test,vec_std_mean_Pmax_Go_S1_03_S2_03_test,vec_std_mean_Pmax_Go_S1_03_S2_05_test,vec_std_mean_Pmax_Go_S1_03_S2_07_test,vec_std_mean_Pmax_Go_S1_03_S2_09_test],
                                  [vec_std_mean_Pmax_Go_S1_05_S2_01_test,vec_std_mean_Pmax_Go_S1_05_S2_03_test,vec_std_mean_Pmax_Go_S1_05_S2_05_test,vec_std_mean_Pmax_Go_S1_05_S2_07_test,vec_std_mean_Pmax_Go_S1_05_S2_09_test],
                                  [vec_std_mean_Pmax_Go_S1_07_S2_01_test,vec_std_mean_Pmax_Go_S1_07_S2_03_test,vec_std_mean_Pmax_Go_S1_07_S2_05_test,vec_std_mean_Pmax_Go_S1_07_S2_07_test,vec_std_mean_Pmax_Go_S1_07_S2_09_test],
                                  [vec_std_mean_Pmax_Go_S1_09_S2_01_test,vec_std_mean_Pmax_Go_S1_09_S2_03_test,vec_std_mean_Pmax_Go_S1_09_S2_05_test,vec_std_mean_Pmax_Go_S1_09_S2_07_test,vec_std_mean_Pmax_Go_S1_09_S2_09_test]]

D1_marg_vec_mean_mean_Pmax_Go_test=np.mean(vec_mean_mean_Pmax_Go_test,1)
D2_marg_vec_mean_mean_Pmax_Go_test=np.mean(vec_mean_mean_Pmax_Go_test,0)

#Pmax Hold failure
#training
vec_mean_mean_Pmax_Hold_training=[[vec_mean_mean_Pmax_Hold_S1_01_S2_01_train,vec_mean_mean_Pmax_Hold_S1_01_S2_03_train,vec_mean_mean_Pmax_Hold_S1_01_S2_05_train,vec_mean_mean_Pmax_Hold_S1_01_S2_07_train,vec_mean_mean_Pmax_Hold_S1_01_S2_09_train],
                                   [vec_mean_mean_Pmax_Hold_S1_03_S2_01_train,vec_mean_mean_Pmax_Hold_S1_03_S2_03_train,vec_mean_mean_Pmax_Hold_S1_03_S2_05_train,vec_mean_mean_Pmax_Hold_S1_03_S2_07_train,vec_mean_mean_Pmax_Hold_S1_03_S2_09_train],
                                   [vec_mean_mean_Pmax_Hold_S1_05_S2_01_train,vec_mean_mean_Pmax_Hold_S1_05_S2_03_train,vec_mean_mean_Pmax_Hold_S1_05_S2_05_train,vec_mean_mean_Pmax_Hold_S1_05_S2_07_train,vec_mean_mean_Pmax_Hold_S1_05_S2_09_train],
                                   [vec_mean_mean_Pmax_Hold_S1_07_S2_01_train,vec_mean_mean_Pmax_Hold_S1_07_S2_03_train,vec_mean_mean_Pmax_Hold_S1_07_S2_05_train,vec_mean_mean_Pmax_Hold_S1_07_S2_07_train,vec_mean_mean_Pmax_Hold_S1_07_S2_09_train],
                                   [vec_mean_mean_Pmax_Hold_S1_09_S2_01_train,vec_mean_mean_Pmax_Hold_S1_09_S2_03_train,vec_mean_mean_Pmax_Hold_S1_09_S2_05_train,vec_mean_mean_Pmax_Hold_S1_09_S2_07_train,vec_mean_mean_Pmax_Hold_S1_09_S2_09_train]]

vec_std_mean_Pmax_Hold_training=[[vec_std_mean_Pmax_Hold_S1_01_S2_01_train,vec_std_mean_Pmax_Hold_S1_01_S2_03_train,vec_std_mean_Pmax_Hold_S1_01_S2_05_train,vec_std_mean_Pmax_Hold_S1_01_S2_07_train,vec_std_mean_Pmax_Hold_S1_01_S2_09_train],
                                  [vec_std_mean_Pmax_Hold_S1_03_S2_01_train,vec_std_mean_Pmax_Hold_S1_03_S2_03_train,vec_std_mean_Pmax_Hold_S1_03_S2_05_train,vec_std_mean_Pmax_Hold_S1_03_S2_07_train,vec_std_mean_Pmax_Hold_S1_03_S2_09_train],
                                  [vec_std_mean_Pmax_Hold_S1_05_S2_01_train,vec_std_mean_Pmax_Hold_S1_05_S2_03_train,vec_std_mean_Pmax_Hold_S1_05_S2_05_train,vec_std_mean_Pmax_Hold_S1_05_S2_07_train,vec_std_mean_Pmax_Hold_S1_05_S2_09_train],
                                  [vec_std_mean_Pmax_Hold_S1_07_S2_01_train,vec_std_mean_Pmax_Hold_S1_07_S2_03_train,vec_std_mean_Pmax_Hold_S1_07_S2_05_train,vec_std_mean_Pmax_Hold_S1_07_S2_07_train,vec_std_mean_Pmax_Hold_S1_07_S2_09_train],
                                  [vec_std_mean_Pmax_Hold_S1_09_S2_01_train,vec_std_mean_Pmax_Hold_S1_09_S2_03_train,vec_std_mean_Pmax_Hold_S1_09_S2_05_train,vec_std_mean_Pmax_Hold_S1_09_S2_07_train,vec_std_mean_Pmax_Hold_S1_09_S2_09_train]]

#test
vec_mean_mean_Pmax_Hold_test=     [[vec_mean_mean_Pmax_Hold_S1_01_S2_01_test,vec_mean_mean_Pmax_Hold_S1_01_S2_03_test,vec_mean_mean_Pmax_Hold_S1_01_S2_05_test,vec_mean_mean_Pmax_Hold_S1_01_S2_07_test,vec_mean_mean_Pmax_Hold_S1_01_S2_09_test],
                                   [vec_mean_mean_Pmax_Hold_S1_03_S2_01_test,vec_mean_mean_Pmax_Hold_S1_03_S2_03_test,vec_mean_mean_Pmax_Hold_S1_03_S2_05_test,vec_mean_mean_Pmax_Hold_S1_03_S2_07_test,vec_mean_mean_Pmax_Hold_S1_03_S2_09_test],
                                   [vec_mean_mean_Pmax_Hold_S1_05_S2_01_test,vec_mean_mean_Pmax_Hold_S1_05_S2_03_test,vec_mean_mean_Pmax_Hold_S1_05_S2_05_test,vec_mean_mean_Pmax_Hold_S1_05_S2_07_test,vec_mean_mean_Pmax_Hold_S1_05_S2_09_test],
                                   [vec_mean_mean_Pmax_Hold_S1_07_S2_01_test,vec_mean_mean_Pmax_Hold_S1_07_S2_03_test,vec_mean_mean_Pmax_Hold_S1_07_S2_05_test,vec_mean_mean_Pmax_Hold_S1_07_S2_07_test,vec_mean_mean_Pmax_Hold_S1_07_S2_09_test],
                                   [vec_mean_mean_Pmax_Hold_S1_09_S2_01_test,vec_mean_mean_Pmax_Hold_S1_09_S2_03_test,vec_mean_mean_Pmax_Hold_S1_09_S2_05_test,vec_mean_mean_Pmax_Hold_S1_09_S2_07_test,vec_mean_mean_Pmax_Hold_S1_09_S2_09_test]]

vec_std_mean_Pmax_Hold_test=[[vec_std_mean_Pmax_Hold_S1_01_S2_01_test,vec_std_mean_Pmax_Hold_S1_01_S2_03_test,vec_std_mean_Pmax_Hold_S1_01_S2_05_test,vec_std_mean_Pmax_Hold_S1_01_S2_07_test,vec_std_mean_Pmax_Hold_S1_01_S2_09_test],
                                  [vec_std_mean_Pmax_Hold_S1_03_S2_01_test,vec_std_mean_Pmax_Hold_S1_03_S2_03_test,vec_std_mean_Pmax_Hold_S1_03_S2_05_test,vec_std_mean_Pmax_Hold_S1_03_S2_07_test,vec_std_mean_Pmax_Hold_S1_03_S2_09_test],
                                  [vec_std_mean_Pmax_Hold_S1_05_S2_01_test,vec_std_mean_Pmax_Hold_S1_05_S2_03_test,vec_std_mean_Pmax_Hold_S1_05_S2_05_test,vec_std_mean_Pmax_Hold_S1_05_S2_07_test,vec_std_mean_Pmax_Hold_S1_05_S2_09_test],
                                  [vec_std_mean_Pmax_Hold_S1_07_S2_01_test,vec_std_mean_Pmax_Hold_S1_07_S2_03_test,vec_std_mean_Pmax_Hold_S1_07_S2_05_test,vec_std_mean_Pmax_Hold_S1_07_S2_07_test,vec_std_mean_Pmax_Hold_S1_07_S2_09_test],
                                  [vec_std_mean_Pmax_Hold_S1_09_S2_01_test,vec_std_mean_Pmax_Hold_S1_09_S2_03_test,vec_std_mean_Pmax_Hold_S1_09_S2_05_test,vec_std_mean_Pmax_Hold_S1_09_S2_07_test,vec_std_mean_Pmax_Hold_S1_09_S2_09_test]]

D1_marg_vec_mean_mean_Pmax_Hold_test=np.mean(vec_mean_mean_Pmax_Hold_test,1)
D2_marg_vec_mean_mean_Pmax_Hold_test=np.mean(vec_mean_mean_Pmax_Hold_test,0)

#Pmax Hold correct
#training
vec_mean_mean_Pmax_Hold_correct_training=[[vec_mean_mean_Pmax_Hold_correct_S1_01_S2_01_train,vec_mean_mean_Pmax_Hold_correct_S1_01_S2_03_train,vec_mean_mean_Pmax_Hold_correct_S1_01_S2_05_train,vec_mean_mean_Pmax_Hold_correct_S1_01_S2_07_train,vec_mean_mean_Pmax_Hold_correct_S1_01_S2_09_train],
                                          [vec_mean_mean_Pmax_Hold_correct_S1_03_S2_01_train,vec_mean_mean_Pmax_Hold_correct_S1_03_S2_03_train,vec_mean_mean_Pmax_Hold_correct_S1_03_S2_05_train,vec_mean_mean_Pmax_Hold_correct_S1_03_S2_07_train,vec_mean_mean_Pmax_Hold_correct_S1_03_S2_09_train],
                                          [vec_mean_mean_Pmax_Hold_correct_S1_05_S2_01_train,vec_mean_mean_Pmax_Hold_correct_S1_05_S2_03_train,vec_mean_mean_Pmax_Hold_correct_S1_05_S2_05_train,vec_mean_mean_Pmax_Hold_correct_S1_05_S2_07_train,vec_mean_mean_Pmax_Hold_correct_S1_05_S2_09_train],
                                          [vec_mean_mean_Pmax_Hold_correct_S1_07_S2_01_train,vec_mean_mean_Pmax_Hold_correct_S1_07_S2_03_train,vec_mean_mean_Pmax_Hold_correct_S1_07_S2_05_train,vec_mean_mean_Pmax_Hold_correct_S1_07_S2_07_train,vec_mean_mean_Pmax_Hold_correct_S1_07_S2_09_train],
                                          [vec_mean_mean_Pmax_Hold_correct_S1_09_S2_01_train,vec_mean_mean_Pmax_Hold_correct_S1_09_S2_03_train,vec_mean_mean_Pmax_Hold_correct_S1_09_S2_05_train,vec_mean_mean_Pmax_Hold_correct_S1_09_S2_07_train,vec_mean_mean_Pmax_Hold_correct_S1_09_S2_09_train]]


vec_std_mean_Pmax_Hold_correct_training=[[vec_std_mean_Pmax_Hold_correct_S1_01_S2_01_train,vec_std_mean_Pmax_Hold_correct_S1_01_S2_03_train,vec_std_mean_Pmax_Hold_correct_S1_01_S2_05_train,vec_std_mean_Pmax_Hold_correct_S1_01_S2_07_train,vec_std_mean_Pmax_Hold_correct_S1_01_S2_09_train],
                                         [vec_std_mean_Pmax_Hold_correct_S1_03_S2_01_train,vec_std_mean_Pmax_Hold_correct_S1_03_S2_03_train,vec_std_mean_Pmax_Hold_correct_S1_03_S2_05_train,vec_std_mean_Pmax_Hold_correct_S1_03_S2_07_train,vec_std_mean_Pmax_Hold_correct_S1_03_S2_09_train],
                                         [vec_std_mean_Pmax_Hold_correct_S1_05_S2_01_train,vec_std_mean_Pmax_Hold_correct_S1_05_S2_03_train,vec_std_mean_Pmax_Hold_correct_S1_05_S2_05_train,vec_std_mean_Pmax_Hold_correct_S1_05_S2_07_train,vec_std_mean_Pmax_Hold_correct_S1_05_S2_09_train],
                                         [vec_std_mean_Pmax_Hold_correct_S1_07_S2_01_train,vec_std_mean_Pmax_Hold_correct_S1_07_S2_03_train,vec_std_mean_Pmax_Hold_correct_S1_07_S2_05_train,vec_std_mean_Pmax_Hold_correct_S1_07_S2_07_train,vec_std_mean_Pmax_Hold_correct_S1_07_S2_09_train],
                                         [vec_std_mean_Pmax_Hold_correct_S1_09_S2_01_train,vec_std_mean_Pmax_Hold_correct_S1_09_S2_03_train,vec_std_mean_Pmax_Hold_correct_S1_09_S2_05_train,vec_std_mean_Pmax_Hold_correct_S1_09_S2_07_train,vec_std_mean_Pmax_Hold_correct_S1_09_S2_09_train]]

#test
vec_mean_mean_Pmax_Hold_correct_test=     [[vec_mean_mean_Pmax_Hold_correct_S1_01_S2_01_test,vec_mean_mean_Pmax_Hold_correct_S1_01_S2_03_test,vec_mean_mean_Pmax_Hold_correct_S1_01_S2_05_test,vec_mean_mean_Pmax_Hold_correct_S1_01_S2_07_test,vec_mean_mean_Pmax_Hold_correct_S1_01_S2_09_test],
                                           [vec_mean_mean_Pmax_Hold_correct_S1_03_S2_01_test,vec_mean_mean_Pmax_Hold_correct_S1_03_S2_03_test,vec_mean_mean_Pmax_Hold_correct_S1_03_S2_05_test,vec_mean_mean_Pmax_Hold_correct_S1_03_S2_07_test,vec_mean_mean_Pmax_Hold_correct_S1_03_S2_09_test],
                                           [vec_mean_mean_Pmax_Hold_correct_S1_05_S2_01_test,vec_mean_mean_Pmax_Hold_correct_S1_05_S2_03_test,vec_mean_mean_Pmax_Hold_correct_S1_05_S2_05_test,vec_mean_mean_Pmax_Hold_correct_S1_05_S2_07_test,vec_mean_mean_Pmax_Hold_correct_S1_05_S2_09_test],
                                           [vec_mean_mean_Pmax_Hold_correct_S1_07_S2_01_test,vec_mean_mean_Pmax_Hold_correct_S1_07_S2_03_test,vec_mean_mean_Pmax_Hold_correct_S1_07_S2_05_test,vec_mean_mean_Pmax_Hold_correct_S1_07_S2_07_test,vec_mean_mean_Pmax_Hold_correct_S1_07_S2_09_test],
                                           [vec_mean_mean_Pmax_Hold_correct_S1_09_S2_01_test,vec_mean_mean_Pmax_Hold_correct_S1_09_S2_03_test,vec_mean_mean_Pmax_Hold_correct_S1_09_S2_05_test,vec_mean_mean_Pmax_Hold_correct_S1_09_S2_07_test,vec_mean_mean_Pmax_Hold_correct_S1_09_S2_09_test]]

vec_std_mean_Pmax_Hold_correct_test=[[vec_std_mean_Pmax_Hold_correct_S1_01_S2_01_test,vec_std_mean_Pmax_Hold_correct_S1_01_S2_03_test,vec_std_mean_Pmax_Hold_correct_S1_01_S2_05_test,vec_std_mean_Pmax_Hold_correct_S1_01_S2_07_test,vec_std_mean_Pmax_Hold_correct_S1_01_S2_09_test],
                                     [vec_std_mean_Pmax_Hold_correct_S1_03_S2_01_test,vec_std_mean_Pmax_Hold_correct_S1_03_S2_03_test,vec_std_mean_Pmax_Hold_correct_S1_03_S2_05_test,vec_std_mean_Pmax_Hold_correct_S1_03_S2_07_test,vec_std_mean_Pmax_Hold_correct_S1_03_S2_09_test],
                                     [vec_std_mean_Pmax_Hold_correct_S1_05_S2_01_test,vec_std_mean_Pmax_Hold_correct_S1_05_S2_03_test,vec_std_mean_Pmax_Hold_correct_S1_05_S2_05_test,vec_std_mean_Pmax_Hold_correct_S1_05_S2_07_test,vec_std_mean_Pmax_Hold_correct_S1_05_S2_09_test],
                                     [vec_std_mean_Pmax_Hold_correct_S1_07_S2_01_test,vec_std_mean_Pmax_Hold_correct_S1_07_S2_03_test,vec_std_mean_Pmax_Hold_correct_S1_07_S2_05_test,vec_std_mean_Pmax_Hold_correct_S1_07_S2_07_test,vec_std_mean_Pmax_Hold_correct_S1_07_S2_09_test],
                                     [vec_std_mean_Pmax_Hold_correct_S1_09_S2_01_test,vec_std_mean_Pmax_Hold_correct_S1_09_S2_03_test,vec_std_mean_Pmax_Hold_correct_S1_09_S2_05_test,vec_std_mean_Pmax_Hold_correct_S1_09_S2_07_test,vec_std_mean_Pmax_Hold_correct_S1_09_S2_09_test]]

D1_marg_vec_mean_mean_Pmax_Hold_correct_test=np.mean(vec_mean_mean_Pmax_Hold_correct_test,1)
D2_marg_vec_mean_mean_Pmax_Hold_correct_test=np.mean(vec_mean_mean_Pmax_Hold_correct_test,0)

#Pmax Hold total
#training
vec_mean_mean_Pmax_Hold_total_training=  [[vec_mean_mean_Pmax_Hold_total_S1_01_S2_01_train,vec_mean_mean_Pmax_Hold_total_S1_01_S2_03_train,vec_mean_mean_Pmax_Hold_total_S1_01_S2_05_train,vec_mean_mean_Pmax_Hold_total_S1_01_S2_07_train,vec_mean_mean_Pmax_Hold_total_S1_01_S2_09_train],
                                          [vec_mean_mean_Pmax_Hold_total_S1_03_S2_01_train,vec_mean_mean_Pmax_Hold_total_S1_03_S2_03_train,vec_mean_mean_Pmax_Hold_total_S1_03_S2_05_train,vec_mean_mean_Pmax_Hold_total_S1_03_S2_07_train,vec_mean_mean_Pmax_Hold_total_S1_03_S2_09_train],
                                          [vec_mean_mean_Pmax_Hold_total_S1_05_S2_01_train,vec_mean_mean_Pmax_Hold_total_S1_05_S2_03_train,vec_mean_mean_Pmax_Hold_total_S1_05_S2_05_train,vec_mean_mean_Pmax_Hold_total_S1_05_S2_07_train,vec_mean_mean_Pmax_Hold_total_S1_05_S2_09_train],
                                          [vec_mean_mean_Pmax_Hold_total_S1_07_S2_01_train,vec_mean_mean_Pmax_Hold_total_S1_07_S2_03_train,vec_mean_mean_Pmax_Hold_total_S1_07_S2_05_train,vec_mean_mean_Pmax_Hold_total_S1_07_S2_07_train,vec_mean_mean_Pmax_Hold_total_S1_07_S2_09_train],
                                          [vec_mean_mean_Pmax_Hold_total_S1_09_S2_01_train,vec_mean_mean_Pmax_Hold_total_S1_09_S2_03_train,vec_mean_mean_Pmax_Hold_total_S1_09_S2_05_train,vec_mean_mean_Pmax_Hold_total_S1_09_S2_07_train,vec_mean_mean_Pmax_Hold_total_S1_09_S2_09_train]]


vec_std_mean_Pmax_Hold_total_training=  [[vec_std_mean_Pmax_Hold_total_S1_01_S2_01_train,vec_std_mean_Pmax_Hold_total_S1_01_S2_03_train,vec_std_mean_Pmax_Hold_total_S1_01_S2_05_train,vec_std_mean_Pmax_Hold_total_S1_01_S2_07_train,vec_std_mean_Pmax_Hold_total_S1_01_S2_09_train],
                                         [vec_std_mean_Pmax_Hold_total_S1_03_S2_01_train,vec_std_mean_Pmax_Hold_total_S1_03_S2_03_train,vec_std_mean_Pmax_Hold_total_S1_03_S2_05_train,vec_std_mean_Pmax_Hold_total_S1_03_S2_07_train,vec_std_mean_Pmax_Hold_total_S1_03_S2_09_train],
                                         [vec_std_mean_Pmax_Hold_total_S1_05_S2_01_train,vec_std_mean_Pmax_Hold_total_S1_05_S2_03_train,vec_std_mean_Pmax_Hold_total_S1_05_S2_05_train,vec_std_mean_Pmax_Hold_total_S1_05_S2_07_train,vec_std_mean_Pmax_Hold_total_S1_05_S2_09_train],
                                         [vec_std_mean_Pmax_Hold_total_S1_07_S2_01_train,vec_std_mean_Pmax_Hold_total_S1_07_S2_03_train,vec_std_mean_Pmax_Hold_total_S1_07_S2_05_train,vec_std_mean_Pmax_Hold_total_S1_07_S2_07_train,vec_std_mean_Pmax_Hold_total_S1_07_S2_09_train],
                                         [vec_std_mean_Pmax_Hold_total_S1_09_S2_01_train,vec_std_mean_Pmax_Hold_total_S1_09_S2_03_train,vec_std_mean_Pmax_Hold_total_S1_09_S2_05_train,vec_std_mean_Pmax_Hold_total_S1_09_S2_07_train,vec_std_mean_Pmax_Hold_total_S1_09_S2_09_train]]

#test
vec_mean_mean_Pmax_Hold_total_test=     [[vec_mean_mean_Pmax_Hold_total_S1_01_S2_01_test,vec_mean_mean_Pmax_Hold_total_S1_01_S2_03_test,vec_mean_mean_Pmax_Hold_total_S1_01_S2_05_test,vec_mean_mean_Pmax_Hold_total_S1_01_S2_07_test,vec_mean_mean_Pmax_Hold_total_S1_01_S2_09_test],
                                         [vec_mean_mean_Pmax_Hold_total_S1_03_S2_01_test,vec_mean_mean_Pmax_Hold_total_S1_03_S2_03_test,vec_mean_mean_Pmax_Hold_total_S1_03_S2_05_test,vec_mean_mean_Pmax_Hold_total_S1_03_S2_07_test,vec_mean_mean_Pmax_Hold_total_S1_03_S2_09_test],
                                         [vec_mean_mean_Pmax_Hold_total_S1_05_S2_01_test,vec_mean_mean_Pmax_Hold_total_S1_05_S2_03_test,vec_mean_mean_Pmax_Hold_total_S1_05_S2_05_test,vec_mean_mean_Pmax_Hold_total_S1_05_S2_07_test,vec_mean_mean_Pmax_Hold_total_S1_05_S2_09_test],
                                         [vec_mean_mean_Pmax_Hold_total_S1_07_S2_01_test,vec_mean_mean_Pmax_Hold_total_S1_07_S2_03_test,vec_mean_mean_Pmax_Hold_total_S1_07_S2_05_test,vec_mean_mean_Pmax_Hold_total_S1_07_S2_07_test,vec_mean_mean_Pmax_Hold_total_S1_07_S2_09_test],
                                         [vec_mean_mean_Pmax_Hold_total_S1_09_S2_01_test,vec_mean_mean_Pmax_Hold_total_S1_09_S2_03_test,vec_mean_mean_Pmax_Hold_total_S1_09_S2_05_test,vec_mean_mean_Pmax_Hold_total_S1_09_S2_07_test,vec_mean_mean_Pmax_Hold_total_S1_09_S2_09_test]]

vec_std_mean_Pmax_Hold_total_test=  [[vec_std_mean_Pmax_Hold_total_S1_01_S2_01_test,vec_std_mean_Pmax_Hold_total_S1_01_S2_03_test,vec_std_mean_Pmax_Hold_total_S1_01_S2_05_test,vec_std_mean_Pmax_Hold_total_S1_01_S2_07_test,vec_std_mean_Pmax_Hold_total_S1_01_S2_09_test],
                                     [vec_std_mean_Pmax_Hold_total_S1_03_S2_01_test,vec_std_mean_Pmax_Hold_total_S1_03_S2_03_test,vec_std_mean_Pmax_Hold_total_S1_03_S2_05_test,vec_std_mean_Pmax_Hold_total_S1_03_S2_07_test,vec_std_mean_Pmax_Hold_total_S1_03_S2_09_test],
                                     [vec_std_mean_Pmax_Hold_total_S1_05_S2_01_test,vec_std_mean_Pmax_Hold_total_S1_05_S2_03_test,vec_std_mean_Pmax_Hold_total_S1_05_S2_05_test,vec_std_mean_Pmax_Hold_total_S1_05_S2_07_test,vec_std_mean_Pmax_Hold_total_S1_05_S2_09_test],
                                     [vec_std_mean_Pmax_Hold_total_S1_07_S2_01_test,vec_std_mean_Pmax_Hold_total_S1_07_S2_03_test,vec_std_mean_Pmax_Hold_total_S1_07_S2_05_test,vec_std_mean_Pmax_Hold_total_S1_07_S2_07_test,vec_std_mean_Pmax_Hold_total_S1_07_S2_09_test],
                                     [vec_std_mean_Pmax_Hold_total_S1_09_S2_01_test,vec_std_mean_Pmax_Hold_total_S1_09_S2_03_test,vec_std_mean_Pmax_Hold_total_S1_09_S2_05_test,vec_std_mean_Pmax_Hold_total_S1_09_S2_07_test,vec_std_mean_Pmax_Hold_total_S1_09_S2_09_test]]

D1_marg_vec_mean_mean_Pmax_Hold_total_test=np.mean(vec_mean_mean_Pmax_Hold_total_test,1)
D2_marg_vec_mean_mean_Pmax_Hold_total_test=np.mean(vec_mean_mean_Pmax_Hold_total_test,0)

#SSRT
#test
vec_mean_mean_SSRT_test=          [[vec_mean_mean_SSRT_S1_01_S2_01_test,vec_mean_mean_SSRT_S1_01_S2_03_test,vec_mean_mean_SSRT_S1_01_S2_05_test,vec_mean_mean_SSRT_S1_01_S2_07_test,vec_mean_mean_SSRT_S1_01_S2_09_test],
                                   [vec_mean_mean_SSRT_S1_03_S2_01_test,vec_mean_mean_SSRT_S1_03_S2_03_test,vec_mean_mean_SSRT_S1_03_S2_05_test,vec_mean_mean_SSRT_S1_03_S2_07_test,vec_mean_mean_SSRT_S1_03_S2_09_test],
                                   [vec_mean_mean_SSRT_S1_05_S2_01_test,vec_mean_mean_SSRT_S1_05_S2_03_test,vec_mean_mean_SSRT_S1_05_S2_05_test,vec_mean_mean_SSRT_S1_05_S2_07_test,vec_mean_mean_SSRT_S1_05_S2_09_test],
                                   [vec_mean_mean_SSRT_S1_07_S2_01_test,vec_mean_mean_SSRT_S1_07_S2_03_test,vec_mean_mean_SSRT_S1_07_S2_05_test,vec_mean_mean_SSRT_S1_07_S2_07_test,vec_mean_mean_SSRT_S1_07_S2_09_test],
                                   [vec_mean_mean_SSRT_S1_09_S2_01_test,vec_mean_mean_SSRT_S1_09_S2_03_test,vec_mean_mean_SSRT_S1_09_S2_05_test,vec_mean_mean_SSRT_S1_09_S2_07_test,vec_mean_mean_SSRT_S1_09_S2_09_test]]

vec_std_mean_SSRT_test=          [[vec_std_mean_SSRT_S1_01_S2_01_test,vec_std_mean_SSRT_S1_01_S2_03_test,vec_std_mean_SSRT_S1_01_S2_05_test,vec_std_mean_SSRT_S1_01_S2_07_test,vec_std_mean_SSRT_S1_01_S2_09_test],
                                  [vec_std_mean_SSRT_S1_03_S2_01_test,vec_std_mean_SSRT_S1_03_S2_03_test,vec_std_mean_SSRT_S1_03_S2_05_test,vec_std_mean_SSRT_S1_03_S2_07_test,vec_std_mean_SSRT_S1_03_S2_09_test],
                                  [vec_std_mean_SSRT_S1_05_S2_01_test,vec_std_mean_SSRT_S1_05_S2_03_test,vec_std_mean_SSRT_S1_05_S2_05_test,vec_std_mean_SSRT_S1_05_S2_07_test,vec_std_mean_SSRT_S1_05_S2_09_test],
                                  [vec_std_mean_SSRT_S1_07_S2_01_test,vec_std_mean_SSRT_S1_07_S2_03_test,vec_std_mean_SSRT_S1_07_S2_05_test,vec_std_mean_SSRT_S1_07_S2_07_test,vec_std_mean_SSRT_S1_07_S2_09_test],
                                  [vec_std_mean_SSRT_S1_09_S2_01_test,vec_std_mean_SSRT_S1_09_S2_03_test,vec_std_mean_SSRT_S1_09_S2_05_test,vec_std_mean_SSRT_S1_09_S2_07_test,vec_std_mean_SSRT_S1_09_S2_09_test]]

D1_marg_vec_mean_mean_SSRT_test=np.mean(vec_mean_mean_SSRT_test,1)
D2_marg_vec_mean_mean_SSRT_test=np.mean(vec_mean_mean_SSRT_test,0)

#right inhibition
#training
vec_mean_right_inhibition_train=  [[vec_mean_right_inhibition_S1_01_S2_01_train,vec_mean_right_inhibition_S1_01_S2_03_train,vec_mean_right_inhibition_S1_01_S2_05_train,vec_mean_right_inhibition_S1_01_S2_07_train,vec_mean_right_inhibition_S1_01_S2_09_train],
                                   [vec_mean_right_inhibition_S1_03_S2_01_train,vec_mean_right_inhibition_S1_03_S2_03_train,vec_mean_right_inhibition_S1_03_S2_05_train,vec_mean_right_inhibition_S1_03_S2_07_train,vec_mean_right_inhibition_S1_03_S2_09_train],
                                   [vec_mean_right_inhibition_S1_05_S2_01_train,vec_mean_right_inhibition_S1_05_S2_03_train,vec_mean_right_inhibition_S1_05_S2_05_train,vec_mean_right_inhibition_S1_05_S2_07_train,vec_mean_right_inhibition_S1_05_S2_09_train],
                                   [vec_mean_right_inhibition_S1_07_S2_01_train,vec_mean_right_inhibition_S1_07_S2_03_train,vec_mean_right_inhibition_S1_07_S2_05_train,vec_mean_right_inhibition_S1_07_S2_07_train,vec_mean_right_inhibition_S1_07_S2_09_train],
                                   [vec_mean_right_inhibition_S1_09_S2_01_train,vec_mean_right_inhibition_S1_09_S2_03_train,vec_mean_right_inhibition_S1_09_S2_05_train,vec_mean_right_inhibition_S1_09_S2_07_train,vec_mean_right_inhibition_S1_09_S2_09_train]]

vec_std_right_inhibition_train=  [[vec_std_right_inhibition_S1_01_S2_01_train,vec_std_right_inhibition_S1_01_S2_03_train,vec_std_right_inhibition_S1_01_S2_05_train,vec_std_right_inhibition_S1_01_S2_07_train,vec_std_right_inhibition_S1_01_S2_09_train],
                                  [vec_std_right_inhibition_S1_03_S2_01_train,vec_std_right_inhibition_S1_03_S2_03_train,vec_std_right_inhibition_S1_03_S2_05_train,vec_std_right_inhibition_S1_03_S2_07_train,vec_std_right_inhibition_S1_03_S2_09_train],
                                  [vec_std_right_inhibition_S1_05_S2_01_train,vec_std_right_inhibition_S1_05_S2_03_train,vec_std_right_inhibition_S1_05_S2_05_train,vec_std_right_inhibition_S1_05_S2_07_train,vec_std_right_inhibition_S1_05_S2_09_train],
                                  [vec_std_right_inhibition_S1_07_S2_01_train,vec_std_right_inhibition_S1_07_S2_03_train,vec_std_right_inhibition_S1_07_S2_05_train,vec_std_right_inhibition_S1_07_S2_07_train,vec_std_right_inhibition_S1_07_S2_09_train],
                                  [vec_std_right_inhibition_S1_09_S2_01_train,vec_std_right_inhibition_S1_09_S2_03_train,vec_std_right_inhibition_S1_09_S2_05_train,vec_std_right_inhibition_S1_09_S2_07_train,vec_std_right_inhibition_S1_09_S2_09_train]]

#test
vec_mean_right_inhibition_test=   [[vec_mean_right_inhibition_S1_01_S2_01_test,vec_mean_right_inhibition_S1_01_S2_03_test,vec_mean_right_inhibition_S1_01_S2_05_test,vec_mean_right_inhibition_S1_01_S2_07_test,vec_mean_right_inhibition_S1_01_S2_09_test],
                                   [vec_mean_right_inhibition_S1_03_S2_01_test,vec_mean_right_inhibition_S1_03_S2_03_test,vec_mean_right_inhibition_S1_03_S2_05_test,vec_mean_right_inhibition_S1_03_S2_07_test,vec_mean_right_inhibition_S1_03_S2_09_test],
                                   [vec_mean_right_inhibition_S1_05_S2_01_test,vec_mean_right_inhibition_S1_05_S2_03_test,vec_mean_right_inhibition_S1_05_S2_05_test,vec_mean_right_inhibition_S1_05_S2_07_test,vec_mean_right_inhibition_S1_05_S2_09_test],
                                   [vec_mean_right_inhibition_S1_07_S2_01_test,vec_mean_right_inhibition_S1_07_S2_03_test,vec_mean_right_inhibition_S1_07_S2_05_test,vec_mean_right_inhibition_S1_07_S2_07_test,vec_mean_right_inhibition_S1_07_S2_09_test],
                                   [vec_mean_right_inhibition_S1_09_S2_01_test,vec_mean_right_inhibition_S1_09_S2_03_test,vec_mean_right_inhibition_S1_09_S2_05_test,vec_mean_right_inhibition_S1_09_S2_07_test,vec_mean_right_inhibition_S1_09_S2_09_test]]

vec_std_right_inhibition_test=   [[vec_std_right_inhibition_S1_01_S2_01_test,vec_std_right_inhibition_S1_01_S2_03_test,vec_std_right_inhibition_S1_01_S2_05_test,vec_std_right_inhibition_S1_01_S2_07_test,vec_std_right_inhibition_S1_01_S2_09_test],
                                  [vec_std_right_inhibition_S1_03_S2_01_test,vec_std_right_inhibition_S1_03_S2_03_test,vec_std_right_inhibition_S1_03_S2_05_test,vec_std_right_inhibition_S1_03_S2_07_test,vec_std_right_inhibition_S1_03_S2_09_test],
                                  [vec_std_right_inhibition_S1_05_S2_01_test,vec_std_right_inhibition_S1_05_S2_03_test,vec_std_right_inhibition_S1_05_S2_05_test,vec_std_right_inhibition_S1_05_S2_07_test,vec_std_right_inhibition_S1_05_S2_09_test],
                                  [vec_std_right_inhibition_S1_07_S2_01_test,vec_std_right_inhibition_S1_07_S2_03_test,vec_std_right_inhibition_S1_07_S2_05_test,vec_std_right_inhibition_S1_07_S2_07_test,vec_std_right_inhibition_S1_07_S2_09_test],
                                  [vec_std_right_inhibition_S1_09_S2_01_test,vec_std_right_inhibition_S1_09_S2_03_test,vec_std_right_inhibition_S1_09_S2_05_test,vec_std_right_inhibition_S1_09_S2_07_test,vec_std_right_inhibition_S1_09_S2_09_test]]

D1_marg_vec_mean_right_inhibition_test=np.mean(vec_mean_right_inhibition_test,1)
D2_marg_vec_mean_right_inhibition_test=np.mean(vec_mean_right_inhibition_test,0)

#global accuracy
#training
vec_mean_accuracy_train=          [[vec_mean_accuracy_S1_01_S2_01_train,vec_mean_accuracy_S1_01_S2_03_train,vec_mean_accuracy_S1_01_S2_05_train,vec_mean_accuracy_S1_01_S2_07_train,vec_mean_accuracy_S1_01_S2_09_train],
                                   [vec_mean_accuracy_S1_03_S2_01_train,vec_mean_accuracy_S1_03_S2_03_train,vec_mean_accuracy_S1_03_S2_05_train,vec_mean_accuracy_S1_03_S2_07_train,vec_mean_accuracy_S1_03_S2_09_train],
                                   [vec_mean_accuracy_S1_05_S2_01_train,vec_mean_accuracy_S1_05_S2_03_train,vec_mean_accuracy_S1_05_S2_05_train,vec_mean_accuracy_S1_05_S2_07_train,vec_mean_accuracy_S1_05_S2_09_train],
                                   [vec_mean_accuracy_S1_07_S2_01_train,vec_mean_accuracy_S1_07_S2_03_train,vec_mean_accuracy_S1_07_S2_05_train,vec_mean_accuracy_S1_07_S2_07_train,vec_mean_accuracy_S1_07_S2_09_train],
                                   [vec_mean_accuracy_S1_09_S2_01_train,vec_mean_accuracy_S1_09_S2_03_train,vec_mean_accuracy_S1_09_S2_05_train,vec_mean_accuracy_S1_09_S2_07_train,vec_mean_accuracy_S1_09_S2_09_train]]

vec_std_accuracy_train=          [[vec_std_accuracy_S1_01_S2_01_train,vec_std_accuracy_S1_01_S2_03_train,vec_std_accuracy_S1_01_S2_05_train,vec_std_accuracy_S1_01_S2_07_train,vec_std_accuracy_S1_01_S2_09_train],
                                  [vec_std_accuracy_S1_03_S2_01_train,vec_std_accuracy_S1_03_S2_03_train,vec_std_accuracy_S1_03_S2_05_train,vec_std_accuracy_S1_03_S2_07_train,vec_std_accuracy_S1_03_S2_09_train],
                                  [vec_std_accuracy_S1_05_S2_01_train,vec_std_accuracy_S1_05_S2_03_train,vec_std_accuracy_S1_05_S2_05_train,vec_std_accuracy_S1_05_S2_07_train,vec_std_accuracy_S1_05_S2_09_train],
                                  [vec_std_accuracy_S1_07_S2_01_train,vec_std_accuracy_S1_07_S2_03_train,vec_std_accuracy_S1_07_S2_05_train,vec_std_accuracy_S1_07_S2_07_train,vec_std_accuracy_S1_07_S2_09_train],
                                  [vec_std_accuracy_S1_09_S2_01_train,vec_std_accuracy_S1_09_S2_03_train,vec_std_accuracy_S1_09_S2_05_train,vec_std_accuracy_S1_09_S2_07_train,vec_std_accuracy_S1_09_S2_09_train]]

#test
vec_mean_accuracy_test=           [[vec_mean_accuracy_S1_01_S2_01_test,vec_mean_accuracy_S1_01_S2_03_test,vec_mean_accuracy_S1_01_S2_05_test,vec_mean_accuracy_S1_01_S2_07_test,vec_mean_accuracy_S1_01_S2_09_test],
                                   [vec_mean_accuracy_S1_03_S2_01_test,vec_mean_accuracy_S1_03_S2_03_test,vec_mean_accuracy_S1_03_S2_05_test,vec_mean_accuracy_S1_03_S2_07_test,vec_mean_accuracy_S1_03_S2_09_test],
                                   [vec_mean_accuracy_S1_05_S2_01_test,vec_mean_accuracy_S1_05_S2_03_test,vec_mean_accuracy_S1_05_S2_05_test,vec_mean_accuracy_S1_05_S2_07_test,vec_mean_accuracy_S1_05_S2_09_test],
                                   [vec_mean_accuracy_S1_07_S2_01_test,vec_mean_accuracy_S1_07_S2_03_test,vec_mean_accuracy_S1_07_S2_05_test,vec_mean_accuracy_S1_07_S2_07_test,vec_mean_accuracy_S1_07_S2_09_test],
                                   [vec_mean_accuracy_S1_09_S2_01_test,vec_mean_accuracy_S1_09_S2_03_test,vec_mean_accuracy_S1_09_S2_05_test,vec_mean_accuracy_S1_09_S2_07_test,vec_mean_accuracy_S1_09_S2_09_test]]


vec_std_accuracy_test=           [[vec_std_accuracy_S1_01_S2_01_test,vec_std_accuracy_S1_01_S2_03_test,vec_std_accuracy_S1_01_S2_05_test,vec_std_accuracy_S1_01_S2_07_test,vec_std_accuracy_S1_01_S2_09_test],
                                  [vec_std_accuracy_S1_03_S2_01_test,vec_std_accuracy_S1_03_S2_03_test,vec_std_accuracy_S1_03_S2_05_test,vec_std_accuracy_S1_03_S2_07_test,vec_std_accuracy_S1_03_S2_09_test],
                                  [vec_std_accuracy_S1_05_S2_01_test,vec_std_accuracy_S1_05_S2_03_test,vec_std_accuracy_S1_05_S2_05_test,vec_std_accuracy_S1_05_S2_07_test,vec_std_accuracy_S1_05_S2_09_test],
                                  [vec_std_accuracy_S1_07_S2_01_test,vec_std_accuracy_S1_07_S2_03_test,vec_std_accuracy_S1_07_S2_05_test,vec_std_accuracy_S1_07_S2_07_test,vec_std_accuracy_S1_07_S2_09_test],
                                  [vec_std_accuracy_S1_09_S2_01_test,vec_std_accuracy_S1_09_S2_03_test,vec_std_accuracy_S1_09_S2_05_test,vec_std_accuracy_S1_09_S2_07_test,vec_std_accuracy_S1_09_S2_09_test]]

D1_marg_vec_mean_accuracy_test=np.mean(vec_mean_accuracy_test,1)
D2_marg_vec_mean_accuracy_test=np.mean(vec_mean_accuracy_test,0)

fig= plt.imshow(vec_mean_mean_reaction_time_Go_training, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('RT Go train [samples]',size=17)
plt.clim(8,35)
plt.show()

fig= plt.imshow(vec_mean_mean_reaction_time_Go_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('RT Go test [samples]',size=17)
plt.clim(8,35)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_reaction_time_Go_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_reaction_time_Go_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel('Dopamine D2', size=17)
plt.ylabel("Marg_D2: RT Go test",size=17)
plt.ylim(8,35)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_reaction_time_Go_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_reaction_time_Go_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel('D1 Dopamine', size=17)
plt.ylabel('Marg_D1: RT Go test',size=17)
plt.ylim(8,35)
plt.show()

fig= plt.imshow(vec_mean_mean_reaction_time_Hold_training, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('RT Hold failure train [samples]',size=17)
plt.clim(8,35)
plt.show()

fig= plt.imshow(vec_mean_mean_reaction_time_Hold_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('RT Hold failure test [samples]',size=17)
plt.clim(8,35)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_reaction_time_Hold_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_reaction_time_Hold_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D2", size=17)
plt.ylabel("Marg_D2: RT Hold failure test",size=17)
plt.ylim(8,35)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_reaction_time_Hold_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_reaction_time_Hold_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: RT Hold filure test",size=17)
plt.ylim(8,35)
plt.show()

fig= plt.imshow(vec_mean_mean_reaction_time_Hold_correct_training, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('RT Hold correct train [samples]',size=17)
plt.clim(8,35)
plt.show()

fig= plt.imshow(vec_mean_mean_reaction_time_Hold_correct_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('RT Hold correct test [samples]',size=17)
plt.clim(8,35)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_reaction_time_Hold_correct_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_reaction_time_Hold_correct_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("D2 Dopamine", size=17)
plt.ylabel("Marg_D2: RT Hold correct test",size=17)
plt.ylim(8,35)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_reaction_time_Hold_correct_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_reaction_time_Hold_correct_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: RT Hold correct test",size=17)
plt.ylim(8,35)
plt.show()

fig= plt.imshow(vec_mean_mean_reaction_time_Hold_total_training, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('RT Hold total train [samples]',size=17)
plt.clim(8,35)
plt.show()

fig= plt.imshow(vec_mean_mean_reaction_time_Hold_total_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('RT Hold total test [samples]',size=17)
plt.clim(8,35)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_reaction_time_Hold_total_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_reaction_time_Hold_total_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D2", size=17)
plt.ylabel("Marg_D2: RT Hold total test",size=17)
plt.ylim(8,35)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_reaction_time_Hold_total_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_reaction_time_Hold_total_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: RT Hold total test",size=17)
plt.ylim(8,35)
plt.show()

fig= plt.imshow(vec_mean_mean_max_PMC_Go_training, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('PMC peak Go train [a.u.]',size=17)
plt.clim(0,0.8)
plt.show()

fig= plt.imshow(vec_mean_mean_max_PMC_Go_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('PMC peak Go test [a.u.]',size=17)
plt.clim(0,0.8)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_max_PMC_Go_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_max_PMC_Go_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D2", size=17)
plt.ylabel("Marg_D2: PMC peak Go test ",size=17)
plt.ylim(0,0.8)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_max_PMC_Go_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_max_PMC_Go_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: PMC peak Go test",size=17)
plt.ylim(0,0.8)
plt.show()

fig= plt.imshow(vec_mean_mean_max_PMC_Hold_training, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('PMC peak Hold failure train [a.u.]',size=17)
plt.clim(0,0.8)
plt.show()

fig= plt.imshow(vec_mean_mean_max_PMC_Hold_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('PMC peak Hold failure test [a.u.]',size=17)
plt.clim(0,0.8)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_max_PMC_Hold_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_max_PMC_Hold_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D2", size=17)
plt.ylabel("Marg_D2: PMC peak Hold failure test ",size=17)
plt.ylim(0,0.8)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_max_PMC_Hold_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_max_PMC_Hold_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: PMC peak Hold failure test ",size=17)
plt.ylim(0,0.8)
plt.show()

fig= plt.imshow(vec_mean_mean_max_PMC_Hold_correct_training, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('PMC peak Hold correct train [a.u.]',size=17)
plt.clim(0,0.8)
plt.show()

fig= plt.imshow(vec_mean_mean_max_PMC_Hold_correct_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('PMC peak Hold correct test [a.u.]',size=17)
plt.clim(0,0.8)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_max_PMC_Hold_correct_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_max_PMC_Hold_correct_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D2", size=17)
plt.ylabel("Marg_D2: PMC peak Hold correct test ",size=17)
plt.ylim(0,0.8)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_max_PMC_Hold_correct_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_max_PMC_Hold_correct_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: PMC peak Hold correct test ",size=17)
plt.ylim(0,0.8)
plt.show()

fig= plt.imshow(vec_mean_mean_max_PMC_Hold_total_training, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('PMC peak Hold total train [a.u.]',size=17)
plt.clim(0,0.8)
plt.show()

fig= plt.imshow(vec_mean_mean_max_PMC_Hold_total_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('PMC peak Hold total test [a.u.]',size=17)
plt.clim(0,0.8)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_max_PMC_Hold_total_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_max_PMC_Hold_total_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D2", size=17)
plt.ylabel("Marg_D2: PMC peak Hold total test ",size=17)
plt.ylim(0,0.8)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_max_PMC_Hold_total_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_max_PMC_Hold_total_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: PMC peak Hold total test ",size=17)
plt.ylim(0,0.8)
plt.show()

fig= plt.imshow(vec_mean_mean_Pmax_Go_training, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('Pmax Go train',size=17)
plt.clim(0,0.6)
plt.show()

fig= plt.imshow(vec_mean_mean_Pmax_Go_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('Pmax Go test',size=17)
plt.clim(0,0.6)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_Pmax_Go_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_Pmax_Go_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D2", size=17)
plt.ylabel("Marg_D2: Pmax Go test ",size=17)
plt.ylim(0,0.6)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_Pmax_Go_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_Pmax_Go_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: Pmax Go test",size=17)
plt.ylim(0,0.6)
plt.show()

fig= plt.imshow(vec_mean_mean_Pmax_Hold_training, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('Pmax Hold failure train',size=17)
plt.clim(0,0.6)
plt.show()

fig= plt.imshow(vec_mean_mean_Pmax_Hold_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('Pmax Hold failure test',size=17)
plt.clim(0,0.6)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_Pmax_Hold_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_Pmax_Hold_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D2", size=17)
plt.ylabel("Marg_D2: Pmax Hold failure test ",size=17)
plt.ylim(0,0.6)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_Pmax_Hold_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_Pmax_Hold_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: Pmax Hold failure test",size=17)
plt.ylim(0,0.6)
plt.show()


fig= plt.imshow(vec_mean_mean_Pmax_Hold_correct_training, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('Pmax Hold correct train',size=17)
plt.clim(0,0.6)
plt.show()

fig= plt.imshow(vec_mean_mean_Pmax_Hold_correct_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('Pmax Hold correct test',size=17)
plt.clim(0,0.6)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_Pmax_Hold_correct_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_Pmax_Hold_correct_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D2", size=17)
plt.ylabel("Marg_D2: Pmax Hold correct test ",size=17)
plt.ylim(0,0.6)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_Pmax_Hold_correct_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_Pmax_Hold_correct_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: Pmax Hold correct test",size=17)
plt.ylim(0,0.6)
plt.show()


fig= plt.imshow(vec_mean_mean_Pmax_Hold_total_training, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('Pmax Hold total train',size=17)
plt.clim(0,0.6)
plt.show()

fig= plt.imshow(vec_mean_mean_Pmax_Hold_total_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('Pmax Hold total test',size=17)
plt.clim(0,0.6)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_Pmax_Hold_total_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_Pmax_Hold_total_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D2", size=17)
plt.ylabel("Marg_D2: Pmax Hold total test ",size=17)
plt.ylim(0,0.6)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_Pmax_Hold_total_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_Pmax_Hold_total_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: Pmax Hold total test",size=17)
plt.ylim(0,0.6)
plt.show()

fig= plt.imshow(vec_mean_mean_SSRT_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('SSRT test [samples]',size=17)
plt.clim(2,25)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_SSRT_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_mean_SSRT_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D2", size=17)
plt.ylabel("Marg_D2: SSRT test",size=17)
plt.ylim(2,25)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_SSRT_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_mean_SSRT_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: SSRT test ",size=17)
plt.ylim(2,25)
plt.show()

fig= plt.imshow(vec_mean_right_inhibition_train, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.clim(0, 100)
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('Right Inhibition train [%]',size=17)
plt.show()

fig= plt.imshow(vec_mean_right_inhibition_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.clim(0, 100)
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('Right Inhibition test [%]',size=17)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_right_inhibition_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_right_inhibition_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D2", size=17)
plt.ylabel("Marg_D2: Right Inhibition test ",size=17)
plt.ylim(0,100)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_right_inhibition_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_right_inhibition_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: Right Inhibition test ",size=17)
plt.ylim(0,100)
plt.show()

fig= plt.imshow(vec_mean_accuracy_train, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.clim(0, 100)
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('Accuracy train [%]',size=17)
plt.show()

fig= plt.imshow(vec_mean_accuracy_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.clim(0, 100)
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('Accuracy test [%]',size=17)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_accuracy_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_mean_accuracy_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D2", size=17)
plt.ylabel("Marg_D2: Accuracy test ",size=17)
plt.ylim(0,100)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_accuracy_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_mean_accuracy_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: Accuracy test",size=17)
plt.ylim(0,100)
plt.show()

fig= plt.imshow(vec_meanG_mean_max_PMC_Pmax_Go_training, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('G: PMC peak & Pmax Go train',size=17)
plt.clim(0,0.8)
plt.show()

fig= plt.imshow(vec_meanG_mean_max_PMC_Pmax_Go_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('G: PMC peak & Pmax Go test',size=17)
plt.clim(0,0.8)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_meanG_mean_max_PMC_Pmax_Go_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_meanG_mean_max_PMC_Pmax_Go_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel('Dopamine D2',size=17)
plt.ylabel("Marg: G: PMC peak & Pmax Go test ",size=17)
plt.ylim(0,0.8)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_meanG_mean_max_PMC_Pmax_Go_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_meanG_mean_max_PMC_Pmax_Go_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("D1 Dopamine", size=17)
plt.ylabel("Marg_D1: G: PMC peak & Pmax Go test",size=17)
plt.ylim(0,0.8)
plt.show()

fig= plt.imshow(vec_meanG_mean_max_PMC_Pmax_Hold_total_training, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('G: PMC peak & Pmax Hold total train',size=17)
plt.clim(0,0.8)
plt.show()

fig= plt.imshow(vec_meanG_mean_max_PMC_Pmax_Hold_total_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('G: PMC peak & Pmax Hold total test',size=17)
plt.clim(0,0.8)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_meanG_mean_max_PMC_Pmax_Hold_total_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_meanG_mean_max_PMC_Pmax_Hold_total_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D2", size=17)
plt.ylabel("Marg_D2: G: PMC peak & Pmax Hold total test ",size=17)
plt.ylim(0,0.8)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_meanG_mean_max_PMC_Pmax_Hold_total_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_meanG_mean_max_PMC_Pmax_Hold_total_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: G: PMC peak & Pmax Hold  total test ",size=17)
plt.ylim(0,0.8)
plt.show()

fig= plt.imshow(vec_meanG_mean_max_PMC_reaction_time_Go_training, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('G: PMC peak & RT Go train',size=17)
plt.clim(0,5)
plt.show()

fig= plt.imshow(vec_meanG_mean_max_PMC_reaction_time_Go_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('G: PMC peak & RT Go test',size=17)
plt.clim(0,5)
plt.show()


plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_meanG_mean_max_PMC_reaction_time_Go_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_meanG_mean_max_PMC_reaction_time_Go_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D2", size=17)
plt.ylabel("Marg_D2: G: PMC peak & RT Go test",size=17)
plt.ylim(0,5)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_meanG_mean_max_PMC_reaction_time_Go_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_meanG_mean_max_PMC_reaction_time_Go_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: G: PMC peak & RT Go test ",size=17)
plt.ylim(0,5)
plt.show()

fig= plt.imshow(vec_meanG_mean_max_PMC_reaction_time_Hold_total_training, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('G: PMC peak & RT Hold total train',size=17)
plt.clim(0,5)
plt.show()

fig= plt.imshow(vec_meanG_mean_max_PMC_reaction_time_Hold_total_test, interpolation = "bilinear", cmap='viridis')
cbar=plt.colorbar()
plt.xticks(range(len(D1)), D1)
plt.yticks(range(len(D2)), D2)
plt.gca().invert_yaxis()
plt.xlabel('Dopamine D2',size=17)
plt.ylabel ('Dopamine D1',size=17)
cbar.set_label('G: PMC peak & RT Hold total test',size=17)
plt.clim(0,5)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_meanG_mean_max_PMC_reaction_time_Hold_total_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D2_marg_vec_meanG_mean_max_PMC_reaction_time_Hold_total_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D2", size=17)
plt.ylabel("Marg_D2: G: PMC peak & RT Hold total test ",size=17)
plt.ylim(0,5)
plt.show()

plt.figure()
plt.errorbar([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_meanG_mean_max_PMC_reaction_time_Hold_total_test, color='black', alpha=0.8)
plt.scatter([0.1,0.3,0.5,0.7,0.9],D1_marg_vec_meanG_mean_max_PMC_reaction_time_Hold_total_test,s=40, color='black', alpha=0.8, marker='o')
plt.xlabel("Dopamine D1", size=17)
plt.ylabel("Marg_D1: G: PMC peak & RT Hold  total test",size=17)
plt.ylim(0,5)
plt.show()












