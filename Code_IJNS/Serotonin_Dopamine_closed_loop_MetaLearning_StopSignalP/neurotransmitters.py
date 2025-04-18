#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@author: federicarobertazzi
"""
import numpy as np

#dopamine neurotransmitter D1, D2
class dopamine:
    def __init__(self, x0, tau_dopa, k_VTA_D, s0_dopa, slope_dopa):
        self.x= x0
        self.tau_dopa=tau_dopa
        self.k_VTA_D=k_VTA_D
        self.memory = [] 
        self.s0_dopa=s0_dopa
        self.slope_dopa=slope_dopa
        self.memory.append(x0)
    def update(self,inp,deltaT,func):
        ext_temp=0
        coupling_temp=func(inp, self.k_VTA_D)
        imp_tot=ext_temp+coupling_temp
        coupling_nonlin=1./(1+np.exp(-self.slope_dopa*(imp_tot-self.s0_dopa)))
        self.x = self.x + deltaT*((-self.x + np.random.normal(coupling_nonlin,0))/self.tau_dopa)
        self.memory.append(self.x)
        
#serotonin neurotrasmitter
class serotonin:
    def __init__(self, x0, tau_sero, k_D1_S,k_D2_S, s0_sero, slope_sero):
        self.x= x0
        self.tau_sero=tau_sero
        self.k_D1_S=k_D1_S
        self.k_D2_S=k_D2_S
        self.memory = []  
        self.s0_sero=s0_sero
        self.slope_sero=slope_sero
        self.memory.append(x0)
    def update(self,inp1,inp2, deltaT,func):
        ext_temp=0
        coupling_temp=func (inp1, self.k_D1_S)+func (inp2, self.k_D2_S)
        imp_tot=ext_temp+coupling_temp
        coupling_nonlin=1./(1+np.exp(-self.slope_sero*(imp_tot-self.s0_sero)))
        self.x = self.x + deltaT*((-self.x + np.random.normal(coupling_nonlin,0))/self.tau_sero)
        self.memory.append(self.x)
                              
                        

   
               
