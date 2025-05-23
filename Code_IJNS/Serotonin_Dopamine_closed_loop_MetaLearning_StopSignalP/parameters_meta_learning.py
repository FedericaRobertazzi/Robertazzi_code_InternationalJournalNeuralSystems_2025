#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federicarobertazzi
"""
import numpy as np

class parameters():
    def __init__(self):
        self.deltaT=0.1#discretization step
        self.tol=200#tolerance (>= 3tau)
        self.L=100#stimulus duration
        
        #neurons parameters
        #PPC
        self.tau_PPC_Neu=0.5
        self.x0_PPC_Neu=0
        self.s0_PPC_Neu=0.6
        self.slope_PPC_Neu=5
        
        #ACC
        self.Q0=0
        self.alpha =0.9
        self.tau_ACC_Neu=0.6
        self.x0_ACC_Neu=0
        self.s0_ACC_Neu=0.6
        self.slope_ACC_Neu=5
        
        #LPFC
        self.tau_LPFC_Neu=0.5
        self.x0_LPFC_Neu=0
        self.s0_LPFC_Neu=0.6
        self.slope_LPFC_Neu=5
        
        #Striatum 
        self.tau_Striatum_Neu=0.5
        self.x0_Striatum_Neu=0
        self.s0_Striatum_Neu=0.6
        self.slope_Striatum_Neu=5
        
        #SNr
        self.tau_SNr_Neu=0.5
        self.x0_SNr_Neu=0
        self.s0_SNr_Neu=0.6
        self.slope_SNr_Neu=5
        
        #Thalamus 
        self.tau_Thalamus_Neu=0.5
        self.x0_Thalamus_Neu=0
        self.s0_Thalamus_Neu=0.6
        self.slope_Thalamus_Neu=5
        
        #PMC 
        self.tau_PMC_Neu=0.25
        self.x0_PMC_Neu=0
        self.s0_PMC_Neu=0.6
        self.slope_PMC_Neu=5
        
        #synaptic weights
        #from PPC
        self.weight_PPC_to_ACC = +1
        self.weight_PPC_to_LPFC = +1
        self.weight_PPC_to_Striatum = +1
        
        #from ACC 
        self.weight_ACC_to_LPFC = +1
        self.weight_ACC_to_VTA = +1
        
        #from LPFC
        self.weight_LPFC_to_Striatum = +1
        
        #from Striatum
        self.weight_Striatum_to_SNr = -1
        
        #from SNr 
        self.weight_SNr_to_Thalamus = -1
        
        #from Thalamus 
        self.weight_Thalamus_to_PMC = +1
        
        #from PMC 
        self.weight_PMC_to_ACC = +1
        self.weight_PMC_to_Striatum = +1
              
        #reward matrix
        self.r_values_0 = [1,0,0,0]   
        self.r_values_1 = [0,1,0,0]
        self.r_values_2 = [0,0,1,0]
        self.r_values_3 = [0,0,0,1]
        self.matrix=[self.r_values_0,self.r_values_1,self.r_values_2,self.r_values_3]

        #input matrix(categories,stimuli)
        self.nstim =1000
        self.inp_start = [[0 for j in range(self.nstim)] for k in range(4)]
        for ii in range(self.nstim):
            self.inp_start[0][ii] = 200 + ii*self.L + ii*self.tol#200 offset init
            self.inp_start[1][ii] = 200 + ii*self.L + ii*self.tol
            self.inp_start[2][ii] = 200 + ii*self.L + ii*self.tol
            self.inp_start[3][ii] = 200 + ii*self.L + ii*self.tol
       
        self.inp_stop  = [[self.inp_start[i][j] + self.L for j in range(len(self.inp_start[0]))] for i in range(len(self.inp_start))]
        self.niter = self.nstim*self.L + self.nstim*(self.tol)+200
        self.rew_method = 'deterministic'#'random'
        
        self.MetaValue_Thr = -0.25
        self.eta = 0.1
        self.beta0=0.25
        self.prob0=0
        self.size=2
        self.tonic_input_Thal=1
        self.tonic_input_SNr=1
        self.threshold_input = 0.75
        self.salience0 = False

        # self.Qmin=0.2
        # self.Qmax=0.5
        # self.delayMin=0
        # self.delayMax=25
        # self.tauMin=0.25
        # self.tauMax0.45
       
        #Q and delay relation
        # self.a=(self.Qmax-self.Qmin)/self.delayMax
        # self.b=self.Qmin
        self.a=(0.5-0.2)/25
        self.b=0.2
        
        #tau and delay relation
        #self.c=(self.tauMax-self.tauMin)/self.delayMax
        #self.d=self.tauMin
        self.c=(0.45-0.25)/25
        self.d=0.25
      
        #params meta-learning
        self.forget_factor = 0.1
        self.a0_D1_to_beta = [10, 9.5, 0.5]#reference condition
        self.a0_D2_to_s0 = [1.2, 0.67, 0.5]#reference condition
        self.k_VTA_D1 = [3, 0.83] 
        self.k_VTA_D2 =[3, 0.83]
        self.eps=0.001
        self.k_D1_S=[1.5, 0.83]
        self.k_D2_S=[1.5, 0.83]
        self.x0_sero=np.random.uniform(0.2,0.8)#(self.eps,1)
        self.x0_dopaD1=np.random.uniform(0.2,0.8)#(self.eps,1)
        self.x0_dopaD2=np.random.uniform(0.2,0.8)#(self.eps,1)
        self.tau_sero=0.5
        self.tau_dopaD1=0.5
        self.tau_dopaD2=0.5
        self.s0_dopa=1.3 
        self.slope_dopa=3
        self.s0_sero=1.3
        self.slope_sero=3
    
        self.offset=1

# =============================================================================
#         #self.serotonine_D1 =0.5
#         #self.serotonine_D2 =0.5
# =============================================================================
        



