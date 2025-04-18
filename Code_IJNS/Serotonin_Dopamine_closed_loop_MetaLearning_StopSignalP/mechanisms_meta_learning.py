#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federica robertazzi
"""
import math as m

def rel_D1_beta(a0_D1_to_beta,D1_TD): 
    return a0_D1_to_beta[0]/(1+m.exp(-(a0_D1_to_beta[1]*(D1_TD - a0_D1_to_beta[2]))))

def D2_Striatum(a0_D2_to_s0,D2):
    return a0_D2_to_s0[0]/(1+m.exp(-(a0_D2_to_s0[1]*(D2 - a0_D2_to_s0[2]))))

#serotonin upregulates dopamine 
def serotonin_to_dopamine_upreg (serotonin, k_VTA_D): 
    if ((serotonin + k_VTA_D[1])>0):
        D = k_VTA_D[0]*m.log(serotonin + k_VTA_D[1],m.e)
        #if (D<=0):
           # D=0
        #elif (D>=1):
           # D=1
    else: 
        #D=m.nan
        D=k_VTA_D[0]*m.log(0 + k_VTA_D[1],m.e)
    return D

#serotonin downregulates dopamine
def serotonin_to_dopamine_downreg (serotonin, k_VTA_D): 
    if ((serotonin + k_VTA_D[1])>0):
        D = -k_VTA_D[0]*m.log(serotonin + k_VTA_D[1],m.e)+1
        #if (D<=0):
           # D=0
       # elif (D>=1):
          #  D=1
    else: 
        #D=m.nan
        D=-k_VTA_D[0]*m.log(0 + k_VTA_D[1],m.e)+1
    return D

#dopamine upregulates serotonin
def dopamine_to_serotonin_upreg (D,k_S): 
    if ((D + k_S[1])>0):
        S = k_S[0]*m.log(D+ k_S[1],m.e)
        #if (S<=0):
          #  S=0
        #elif (S>=1):
          #  S=1
    else:
        #S=m.nan
        S=k_S[0]*m.log(0+ k_S[1],m.e)
    return S

#dopamine downregulates serotonin
def dopamine_to_serotonin_downreg (D,k_S):
    if ((D + k_S[1])>0):
        S = -k_S[0]*m.log(D+ k_S[1],m.e)+1
        #if (S<=0):
            #S=0
       # elif (S>=1):
          #  S=1
    else: 
        #S=m.nan
        S=-k_S[0]*m.log(0+ k_S[1],m.e)+1
    return S

def choose_func(argument):
    switcher = {
        1: "FUNC1: serotonin to dopamine upreg; FUNC2: dopamine to serotonin upreg",
        2: "FUNC1: serotonin to dopamine downreg; FUNC2: dopamine to serotonin upreg",
        3: "FUNC1: serotonin to dopamine downreg FUNC2: dopamine to serotonin downreg",
        4: "FUNC1: serotonin to dopamine upreg; FUNC2: dopamine to serotonin downreg",
        }
    func = switcher.get(argument)
    return(func)

def compute_TD_meta_learning(reward,Q_now,Q_prev, serotonin,D1): 
    salientEvent = 1.0;
    tderror = (reward + serotonin* Q_now - Q_prev)*D1
    print('reward, sero, Q_prev:',[reward, serotonin*Q_now, Q_prev])  
    return tderror, salientEvent   

def compute_forgetting(Q_now, action_sel_conv,forget_factor):
    for i in range(len(Q_now)):
        for j in range(len(Q_now[0])):
            if(i != action_sel_conv[0]) or (j != action_sel_conv[1]):
                 if i == 1 and j == 0:
                    Q_now[i][j].Q = Q_now[i][j].Q*(1-0.01)
                    Q_now[i][j].memory.append(Q_now[i][j].Q)
                 else:                     
                    Q_now[i][j].Q = Q_now[i][j].Q*(1-forget_factor)
                    Q_now[i][j].memory.append(Q_now[i][j].Q)
    return Q_now
        
    
    
    
    
    
    













    
    
    
    
    
    
    
    