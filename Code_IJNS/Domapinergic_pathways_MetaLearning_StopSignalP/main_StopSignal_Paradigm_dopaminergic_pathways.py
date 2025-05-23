#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""    
@author: federicarobertazzi
"""
import numpy as np
#import matplotlib.pyplot as plt

from neurons import PPC,ACC_Q,ACC,LPFC,Striatum,SNr,Thalamus,PMC
from synapses import synapse,synaptic_plasticity
from action_probability import action_probability
from parameters_meta_learning import parameters
from utility import visual_input,check_salience,check_pcc,motor_output,compute_reward,stationary_stochastic_reward,reset_Q,reset_beta
from utility import get_activity,prevent_Qstack,get_QAct,get_QPrev,random_distr,action_vec_to_mat,update_metavalue,hold_react,get_new_tau
from mechanisms_meta_learning import rel_D1_beta,serotonin_to_dopamine,compute_TD_meta_learning,compute_forgetting
from parameters_and_metrics_computation import compute_net_parameters,compute_SSRT,compute_right_inhibition,compute_global_accuracy

params = parameters()

#neurons 
#PPC layer
PPC_Neu0 = PPC(params.tau_PPC_Neu,params.x0_PPC_Neu,params.s0_PPC_Neu,params.slope_PPC_Neu)
PPC_Neu1 = PPC(params.tau_PPC_Neu,params.x0_PPC_Neu,params.s0_PPC_Neu,params.slope_PPC_Neu)
PPC_Neu2 = PPC(params.tau_PPC_Neu,params.x0_PPC_Neu,params.s0_PPC_Neu,params.slope_PPC_Neu)
PPC_Neu3 = PPC(params.tau_PPC_Neu,params.x0_PPC_Neu,params.s0_PPC_Neu,params.slope_PPC_Neu)
PPC_Neu =[[PPC_Neu0, PPC_Neu1], [PPC_Neu2, PPC_Neu3]]

#ACC action values
ACC_Q0 = ACC_Q(params.alpha,params.Q0)
ACC_Q1 = ACC_Q(params.alpha,params.Q0)
ACC_Q2 = ACC_Q(params.alpha,params.Q0)
ACC_Q3 = ACC_Q(params.alpha,params.Q0)
ACC_Q =[[ACC_Q0, ACC_Q1], [ACC_Q2, ACC_Q3]]

#ACC layer 
ACC_Neu0 = ACC(params.tau_ACC_Neu,params.x0_ACC_Neu,params.s0_ACC_Neu,params.slope_ACC_Neu)  
ACC_Neu1 = ACC(params.tau_ACC_Neu,params.x0_ACC_Neu,params.s0_ACC_Neu,params.slope_ACC_Neu)
ACC_Neu2 = ACC(params.tau_ACC_Neu,params.x0_ACC_Neu,params.s0_ACC_Neu,params.slope_ACC_Neu)
ACC_Neu3 = ACC(params.tau_ACC_Neu,params.x0_ACC_Neu,params.s0_ACC_Neu,params.slope_ACC_Neu)
ACC_Neu =[[ACC_Neu0, ACC_Neu1], [ACC_Neu2, ACC_Neu3]]

#LPFC layer 
LPFC_Neu0 = LPFC(params.tau_LPFC_Neu,params.x0_LPFC_Neu,params.s0_LPFC_Neu,params.slope_LPFC_Neu,params.prob0)
LPFC_Neu1 = LPFC(params.tau_LPFC_Neu,params.x0_LPFC_Neu,params.s0_LPFC_Neu,params.slope_LPFC_Neu,params.prob0)
LPFC_Neu2 = LPFC(params.tau_LPFC_Neu,params.x0_LPFC_Neu,params.s0_LPFC_Neu,params.slope_LPFC_Neu,params.prob0)
LPFC_Neu3 = LPFC(params.tau_LPFC_Neu,params.x0_LPFC_Neu,params.s0_LPFC_Neu,params.slope_LPFC_Neu,params.prob0)
LPFC_Neu =[[LPFC_Neu0, LPFC_Neu1], [LPFC_Neu2, LPFC_Neu3]]

#Striatum layer 
Striatum_Neu0 = Striatum(params.tau_Striatum_Neu,params.x0_Striatum_Neu,params.s0_Striatum_Neu,params.slope_Striatum_Neu)
Striatum_Neu1 = Striatum(params.tau_Striatum_Neu,params.x0_Striatum_Neu,params.s0_Striatum_Neu,params.slope_Striatum_Neu)
Striatum_Neu2 = Striatum(params.tau_Striatum_Neu,params.x0_Striatum_Neu,params.s0_Striatum_Neu,params.slope_Striatum_Neu)
Striatum_Neu3 = Striatum(params.tau_Striatum_Neu,params.x0_Striatum_Neu,params.s0_Striatum_Neu,params.slope_Striatum_Neu)
Striatum_Neu =[[Striatum_Neu0, Striatum_Neu1], [Striatum_Neu2, Striatum_Neu3]]

#SNr layer 
SNr_Neu0 = SNr(params.tau_SNr_Neu,params.x0_SNr_Neu,params.s0_SNr_Neu,params.slope_SNr_Neu)
SNr_Neu1 = SNr(params.tau_SNr_Neu,params.x0_SNr_Neu,params.s0_SNr_Neu,params.slope_SNr_Neu)
SNr_Neu2 = SNr(params.tau_SNr_Neu,params.x0_SNr_Neu,params.s0_SNr_Neu,params.slope_SNr_Neu)
SNr_Neu3 = SNr(params.tau_SNr_Neu,params.x0_SNr_Neu,params.s0_SNr_Neu,params.slope_SNr_Neu)
SNr_Neu =[[SNr_Neu0, SNr_Neu1], [SNr_Neu2, SNr_Neu3]]
 
#Thalamus layer 
Thalamus_Neu0 = Thalamus(params.tau_Thalamus_Neu,params.x0_Thalamus_Neu,params.s0_Thalamus_Neu,params.slope_Thalamus_Neu)
Thalamus_Neu1 = Thalamus(params.tau_Thalamus_Neu,params.x0_Thalamus_Neu,params.s0_Thalamus_Neu,params.slope_Thalamus_Neu)
Thalamus_Neu2 = Thalamus(params.tau_Thalamus_Neu,params.x0_Thalamus_Neu,params.s0_Thalamus_Neu,params.slope_Thalamus_Neu)
Thalamus_Neu3 = Thalamus(params.tau_Thalamus_Neu,params.x0_Thalamus_Neu,params.s0_Thalamus_Neu,params.slope_Thalamus_Neu)
Thalamus_Neu =[[Thalamus_Neu0, Thalamus_Neu1], [Thalamus_Neu2, Thalamus_Neu3]]

#PMC layer
PMC_Neu0 = PMC(params.tau_PMC_Neu,params.x0_PMC_Neu,params.s0_PMC_Neu,params.slope_PMC_Neu)
PMC_Neu1 = PMC(params.tau_PMC_Neu,params.x0_PMC_Neu,params.s0_PMC_Neu,params.slope_PMC_Neu)
PMC_Neu2 = PMC(params.tau_PMC_Neu,params.x0_PMC_Neu,params.s0_PMC_Neu,params.slope_PMC_Neu)
PMC_Neu3 = PMC(params.tau_PMC_Neu,params.x0_PMC_Neu,params.s0_PMC_Neu,params.slope_PMC_Neu)
PMC_Neu =[[PMC_Neu0, PMC_Neu1], [PMC_Neu2, PMC_Neu3]]

# beta init
beta = []
beta.append(np.random.uniform(0,5))

#tau init
tau_vec=[]
tau_vec.append(params.tau_PMC_Neu)

# action probability
P0 = action_probability(params.beta0,params.prob0,[0,0])
P1 = action_probability(params.beta0,params.prob0,[0,1])
P2 = action_probability(params.beta0,params.prob0,[1,0])
P3 = action_probability(params.beta0,params.prob0,[1,1])
P = [[P0,P1],[P2,P3]]

#synapses 
#from PPC
PPC_to_ACC = synapse(params.weight_PPC_to_ACC)
PPC_to_LPFC = synapse(params.weight_PPC_to_LPFC)
PPC_to_Striatum = synapse(params.weight_PPC_to_Striatum)

#from ACC 
ACC_to_LPFC = synapse(params.weight_ACC_to_LPFC)
#ACC_to_VTA = synapse(params.weight_ACC_to_VTA)

#from LPFC
#plasticity
LPFC_to_Striatum_0 = synaptic_plasticity(params.weight_LPFC_to_Striatum,params.Q0)
LPFC_to_Striatum_1 = synaptic_plasticity(params.weight_LPFC_to_Striatum,params.Q0)
LPFC_to_Striatum_2 = synaptic_plasticity(params.weight_LPFC_to_Striatum,params.Q0)
LPFC_to_Striatum_3 = synaptic_plasticity(params.weight_LPFC_to_Striatum,params.Q0)
LPFC_to_Striatum=[[ LPFC_to_Striatum_0,LPFC_to_Striatum_1],[LPFC_to_Striatum_2, LPFC_to_Striatum_3]]

#from Striatum
Striatum_to_SNr = synapse(params.weight_Striatum_to_SNr)

#from SNr 
SNr_to_Thalamus = synapse(params.weight_SNr_to_Thalamus)

#from Thalamus 
Thalamus_to_PMC = synapse(params.weight_Thalamus_to_PMC)

#from PMC 
PMC_to_ACC = synapse(params.weight_PMC_to_ACC)
PMC_to_Striatum = synapse(params.weight_PMC_to_Striatum)

# visual input
inp = visual_input(params.niter,params.inp_start,params.inp_stop)

#salience input 
sal = check_salience(inp,params.salience0)

firing_PPC = np.zeros((params.size, params.size, params.niter))
firing_ACC = np.zeros((params.size, params.size, params.niter))
firing_LPFC = np.zeros((params.size, params.size, params.niter))
firing_Striatum = np.zeros((params.size, params.size, params.niter))
firing_SNr = np.zeros((params.size, params.size, params.niter))
firing_Thalamus = np.zeros((params.size, params.size, params.niter))
firing_PMC = np.zeros((params.size, params.size, params.niter))

PPC_to_ACC_matrix = np.zeros((params.size,params.niter))
PPC_to_LPFC_matrix = np.zeros((params.size,params.niter))
PPC_to_Striatum_matrix = np.zeros((params.size,params.niter))
ACC_to_LPFC_matrix = np.zeros((params.size,params.niter))
LPFC_to_Striatum_matrix = np.zeros((params.size,params.niter))
Striatum_to_SNr_matrix = np.zeros((params.size,params.niter))
SNr_to_Thalamus_matrix = np.zeros((params.size,params.niter))
Thalamus_to_PMC_matrix = np.zeros((params.size,params.niter))
PMC_to_ACC_matrix = np.zeros((params.size,params.niter))
PMC_to_Striatum_matrix = np.zeros((params.size,params.niter))

#parameters init
Pmax =[]
action_vec =[]
reward_vec = []
flag_updateTD = []
TD_memory = []
delta_rew = []
time_hold = []
time_crucial_trial = []
count_problem=[]
trial_type_vec = []

MetaValue_Direction = [0,0]
MetaValue_Hold = [0,0]
action=0
reward = 0
cont_salient = 0
TD = 0
count_ppc = 0
l=np.random.randint(0,2)
#trial type (Go 50% or StopSignal 50%)
trial_type_set = [0,1]
prob_trial_type = [0.5,0.5]
trial_type = 1 #init

#reward
r_values_Go = params.matrix[l]
r_values_Stop_Signal = [0,0,1,0]
print('r values Go',r_values_Go)
print('r values StopSignal',r_values_Stop_Signal)

n_problems = 0
n_success = 0

n_trials_block = 10
n_trials_block_counter = 0

count_ppc = 0
flag_hold = False
done_crucial = 0

entropy_vec=[]#entropy init

# parameters ML init
Sero_D1 = []
Sero_D1.append(params.serotonin_D1)
Sero_D2 = []
Sero_D2.append(params.serotonin_D2)
DopaD1 = []
D1, D2 = serotonin_to_dopamine(params.serotonin_D1,params.serotonin_D2, params.k_VTA_D1, params.k_SNc_D2)
DopaD1.append(D1)
DopaD2 = []
DopaD2.append(D2)

Stop_Signal_failure_type=[]#StopSignal failure trials : omol or eter 

print('Sero D1:', Sero_D1)
print('Sero D2:', Sero_D2)
print('D1:', DopaD1)
print('D2:', DopaD2)

matrix_P_vec=np.empty((3,1))
beta_new=[] #auxiliary beta (updated when entropy_vec is updated), beta and beta_new have the same trend

count_step_delay=0
vector_delay=np.array(range(0,31,10))#delay [10,20,30]
print('vector delay:', vector_delay)
delay_type=[]
print('delay type:',delay_type)

for n in range(params.niter-1): 
    count_step_delay=count_step_delay+1
    if count_ppc != 4:
        trial_type = 1
    if count_ppc==5:
       done_crucial = 0
       flag_hold = False
       count_ppc = 0
       beta = reset_beta(beta)
       ACC_Q = reset_Q(ACC_Q)
       l=np.random.randint(0,2)
       if params.rew_method == 'deterministic':
          r_values = params.matrix[l]
       elif params.rew_method == 'random':
            #this function is equal to deterministic case if there are 1 and 0, 
            #change this values for custom probability
            r_values = stationary_stochastic_reward(params.matrix[l],params.matrix)        
    if count_ppc == 4 and done_crucial == 0: # target detection 
           done_crucial = 1
           print('START CRUCIAL TRIAL ########################################')
           print('ppc 4 yes')
           trial_type = random_distr(trial_type_set, prob_trial_type)
           trial_type_vec.append(trial_type)          
           if trial_type == 0:
                flag_hold = True
                r_values = r_values_Stop_Signal 
    D1,D2 = serotonin_to_dopamine(Sero_D1[-1],Sero_D2[-1],params.k_VTA_D1, params.k_SNc_D2)
    DopaD1.append(D1)
    DopaD2.append(D2)
    
    # compute input
    for i in range(len(PPC_Neu)):
        for j in range(len(PPC_Neu[0])):
            #PPC connections 
             PPC_to_ACC.connect(PPC_Neu[i][j])
             PPC_to_ACC_matrix[i][j]=PPC_to_ACC.inp*ACC_Q[i][j].Q
             
             PPC_to_LPFC.connect(PPC_Neu[i][j])
             PPC_to_LPFC_matrix[i][j]=PPC_to_LPFC.inp
             
             PPC_to_Striatum.connect(PPC_Neu[i][j])
             PPC_to_Striatum_matrix[i][j]=PPC_to_Striatum.inp
             
             #ACC connections
             ACC_to_LPFC.connect(ACC_Neu[i][j])
             ACC_to_LPFC_matrix[i][j]=ACC_to_LPFC.inp
             
             #ACC_to_VTA.connect(ACC_Neu[i][j])
             #ACC_to_VTA_matrix[i][j]=ACC_to_VTA.inp
           
             #LPFC connections
             LPFC_to_Striatum[i][j].update(P[i][j])             
             LPFC_to_Striatum[i][j].connect(LPFC_Neu[i][j])
             LPFC_to_Striatum_matrix[i][j]=LPFC_to_Striatum[i][j].inp
             
             if i == 1 and j == 1:
                LPFC_to_Striatum_matrix[i][j]=LPFC_to_Striatum[i][j].inp*5
             
             #Striatum connections 
             Striatum_to_SNr.connect(Striatum_Neu[i][j])
             Striatum_to_SNr_matrix[i][j]= Striatum_to_SNr.inp
             
             #SNr connections 
             SNr_to_Thalamus.connect(SNr_Neu[i][j])
             SNr_to_Thalamus_matrix[i][j]= SNr_to_Thalamus.inp
             
             #Thalamus connections
             Thalamus_to_PMC.connect(Thalamus_Neu[i][j])
             Thalamus_to_PMC_matrix[i][j] = Thalamus_to_PMC.inp 
          
             #PMC connections 
             PMC_to_ACC.connect(PMC_Neu[i][j])
             PMC_to_ACC_matrix[i][j]= PMC_to_ACC.inp
             
             PMC_to_Striatum.connect(PMC_Neu[i][j])
             PMC_to_Striatum_matrix[i][j]= PMC_to_Striatum.inp
             
    for i in range(len(P)):
        for j in range(len(P[0])):
             P[i][j].set_values(beta[-1],ACC_Q)
             P[i][j].probab()
    if sal[n]  == 1:
        cont_salient = cont_salient + 1     
        if (cont_salient%2) != 0:
            print('ACC INP LEFT:',PPC_to_ACC_matrix[0][0])
            print('ACC INP RIGHT:',PPC_to_ACC_matrix[0][1])
            print('ACC INP HOLD:',PPC_to_ACC_matrix[1][0])
            if count_ppc!=4:
                time_crucial_trial.append(0)
            else:
                time_crucial_trial.append(1)
            print('check ppc 2:',count_ppc)                    
            QAct = get_QAct(ACC_Q)
            var=np.random.randint(0,len(vector_delay))
            delay=vector_delay[var]
            print('delay:',delay)
            if flag_hold:
                delay_type.append(delay)
            else: 
                delay_type.append(-1)                 
            if flag_hold and count_step_delay >= round(params.deltaT*delay):
                count_step_delay=0         
                ACC_Q, beta = hold_react(MetaValue_Direction,MetaValue_Hold,beta,ACC_Q, params.MetaValue_Thr,delay,params.a,params.b)
                new_tau=get_new_tau(delay,params.c,params.d)
                tau_vec.append(new_tau)
                PMC_Neu[1][0].set_tau(new_tau)
                for i in range(len(P)):
                    for j in range(len(P[0])):
                        P[i][j].set_values(beta[-1],ACC_Q)
                        P[i][j].probab()       
                print('hold react yes')
                print('beta {} and 1P test {}, 2P test {} and 3P test HOLD {}:'.format(beta[-1], P[0][0].probability, P[0][1].probability, P[1][0].probability))
                time_hold.append(1)
            else:
                time_hold.append(0)
                PMC_Neu[1][0].set_tau(params.tau_PMC_Neu)
                tau_vec.append(params.tau_PMC_Neu)
            if cont_salient < 4:
               QPrev = QAct
            else:
               QPrev = get_QPrev(ACC_Q)
            print('Beta {} and 1Q test {}, 2Q test {} and 3Q test {}:'.format(beta[-1], ACC_Q[0][0].Q, ACC_Q[0][1].Q, ACC_Q[1][0].Q))               
            print('1P test {}, 2P test {} and 3P test {}:'.format(P[0][0].probability, P[0][1].probability, P[1][0].probability))
            print('trial type:',trial_type)
            if trial_type == 1:   
               r_values = stationary_stochastic_reward(params.matrix[l],params.matrix)      
               print('r value impo:',r_values)
            else:
                r_values = r_values_Stop_Signal
        elif (cont_salient%2) == 0:          
             curr_PMC = get_activity(PMC_Neu)
             print('1PMC test {}, 2PMC test {} and 3PMC test {}:'.format(curr_PMC[0][0], curr_PMC[0][1], curr_PMC[1][0]))
             Pmax.append(motor_output(curr_PMC)[0])
             action = (motor_output(curr_PMC)[1]) 
             print('action: ',action)
             
             ###########################ENTROPY###########################
             P_vec=np.array([P[0][0].probability,P[0][1].probability, P[1][0].probability])         
             entropy_vec.append(-sum(np.multiply(P_vec, np.log2(P_vec)))/np.log2(3))
             beta_new.append(beta[-1])
             matrix_P_vec= np.column_stack((matrix_P_vec, P_vec))
             ##############################################################
             
             if action == 3:
                 action = 2
             action_conv_i, action_conv_j = action_vec_to_mat(action)
             action_vec.append(action)
             print('r values:',r_values)  
             reward = compute_reward(action,r_values)    
             reward_vec.append(reward)
             
             if reward==0 and trial_type==0:
                 if l==action:
                    Stop_Signal_failure_type.append(1) #omol
                 else:
                     Stop_Signal_failure_type.append(0) #eter
                     
             print('flag hold: ',flag_hold)
             MetaValue_Direction,MetaValue_Hold,delta_rew_out = update_metavalue(MetaValue_Direction,MetaValue_Hold,reward_vec,params.eta,flag_hold)
             delta_rew.append(delta_rew_out)
             flag_hold = False
             count_ppc = check_pcc(reward,count_ppc)
             if count_ppc == 4:
                 n_problems = n_problems + 1    
             print('action i', action_conv_i)
             print('action j', action_conv_j)
             print('QAct',QAct[action_conv_i][ action_conv_j])
             print('QPrev',QPrev[action_conv_i][action_conv_j])
             print('Sero D1',Sero_D1[-1])
             print('Sero D2',Sero_D2[-1])
             print('Dopa',DopaD1[-1])
             print('count ppc: ', count_ppc) 
             [TD,flagSalient] = compute_TD_meta_learning(reward, QAct[action_conv_i][action_conv_j], QPrev[action_conv_i][action_conv_j], Sero_D1[-1], DopaD1[-1] )   
             print('delta reward:',delta_rew_out)             
             print('end trial')
             TD_memory.append(TD)
             
             # compute beta from D1 
             beta.append(rel_D1_beta(params.a0_D1_to_beta,DopaD1[-1]*TD))
             # be sure that useless neuron is always 0
             ACC_Q[1][1].Q = 0
             ACC_Q[action_conv_i][action_conv_j].update(TD,1)  
             ACC_Q = compute_forgetting(ACC_Q,[action_conv_i, action_conv_j], params.forget_factor)
             print('1Q test {}, 2Q test {} and 3Q test {}:'.format(ACC_Q[0][0].Q, ACC_Q[0][1].Q, ACC_Q[1][0].Q))
 
    for i in range(len(PPC_Neu)):
        for j in range(len(PPC_Neu[0])):
            if i == 0 and  j ==0:    
                if l == 0:
                    PPC_Neu[i][j].update(params.deltaT,inp[0][n])
                else:
                    PPC_Neu[i][j].update(params.deltaT,0)                        
            elif i == 0 and j ==1:
                if l == 1:
                    PPC_Neu[i][j].update(params.deltaT,inp[1][n])
                else:
                    PPC_Neu[i][j].update(params.deltaT,0)                     
            elif i == 1 and j ==0 and flag_hold == True:    
                 PPC_Neu[i][j].update(params.deltaT,inp[2][n])
            elif i == 1 and j ==1:    
                 PPC_Neu[i][j].update(params.deltaT,inp[3][n])           
            else:
                PPC_Neu[i][j].update(params.deltaT,0)  
                
            PPC_Neu[i][j].sigmoid() 
            l_PPC=PPC_Neu[i][j].out
            firing_PPC[i][j][n+1]=l_PPC

            ACC_Neu[i][j].update(params.deltaT,PPC_to_ACC_matrix[i][j]) #+PMC_to_ACC_matrix[i][j])
            ACC_Neu[i][j].store()
            l_ACC=ACC_Neu[i][j].out
            firing_ACC[i][j][n]=l_ACC
            
            LPFC_Neu[i][j].update(params.deltaT, ACC_to_LPFC_matrix[i][j]) #+PPC_to_LPFC_matrix[i][j])
            LPFC_Neu[i][j].sigmoid()
            l_LPFC=LPFC_Neu[i][j].out
            firing_LPFC[i][j][n+1]=l_LPFC
            
            Striatum_Neu[i][j].update_s0(DopaD2[-1], params.a0_D2_to_s0)
            Striatum_Neu[i][j].update(params.deltaT, LPFC_to_Striatum_matrix[i][j]) #+ PMC_to_Striatum_matrix[i][j])# PPC_to_Striatum_matrix[i][j])
            Striatum_Neu[i][j].sigmoid()
            l_Striatum=Striatum_Neu[i][j].out
            firing_Striatum[i][j][n+1]=l_Striatum
            
            SNr_Neu[i][j].update(params.deltaT,Striatum_to_SNr_matrix[i][j]+ params.tonic_input_SNr)
            SNr_Neu[i][j].sigmoid()
            l_SNr=SNr_Neu[i][j].out
            firing_SNr[i][j][n+1]=l_SNr
            
            Thalamus_Neu[i][j].update(params.deltaT,SNr_to_Thalamus_matrix[i][j]+params.tonic_input_Thal)
            Thalamus_Neu[i][j].sigmoid()
            l_Thalamus=Thalamus_Neu[i][j].out
            firing_Thalamus[i][j][n+1]=l_Thalamus
        
            PMC_Neu[i][j].update(params.deltaT,Thalamus_to_PMC_matrix[i][j]) 
            PMC_Neu[i][j].sigmoid()
            l_PMC=PMC_Neu[i][j].out
            firing_PMC[i][j][n+1]=l_PMC
            
    ACC_Q = prevent_Qstack(ACC_Q)

print('##############################################')
print(' Simulation settings:')
print(' level of serotonin D1:', np.mean(Sero_D1))
print(' level of serotonin D2:', np.mean(Sero_D2))
print(' level of D1:', np.mean(DopaD1))
print(' level of D2:', np.mean(DopaD2))
print('##############################################')

print('##############################################')
print(' Check variables: ')
print(' len reward: ',len(reward_vec))
print(' len time hold: ',len(time_hold))
print(' len stimuli: ',len(params.inp_start[0]))
print(' len delta rew: ',len(delta_rew))
print(' len meta value hold ',len(MetaValue_Hold))
print(' len meta value direction ',len(MetaValue_Direction))
print(' len action ',len(action_vec))
print('##############################################')

#time to reach threshold
MetaValue_Hold = np.array(MetaValue_Hold)
try:
    time_tothr = np.argwhere(MetaValue_Hold <= params.MetaValue_Thr).min()
    print('trials needed to learn hold meta-value:',time_tothr)
    time_toend=params.nstim-time_tothr
    print('trials from learn hold meta-value and the end:',time_toend)
except:
    print('Metavalue of holds always greater than -0.25')

when_hold= np.argwhere(np.array(time_hold) == 1)

when_hold_training = when_hold[when_hold <= time_tothr]
when_hold_test = when_hold[when_hold > time_tothr]

firing_PMC_training=np.zeros((2,2,params.inp_start[0][time_tothr]))
firing_PMC_test=np.zeros((2,2,params.niter-params.inp_start[0][time_tothr]))

for i in range(2):
    for j in range(2):
        firing_PMC_training[i,j,:]=firing_PMC[i,j,0:params.inp_start[0][time_tothr]]
        firing_PMC_test[i,j,:]=firing_PMC[i,j,(params.inp_start[0][time_tothr]):]
        
count_inp_start=time_tothr  
print('count inp start:',count_inp_start)

delay_type_training1=delay_type[0:(count_inp_start)]
delay_type_training=np.array(delay_type_training1)
print('delay type training:',delay_type_training)
print('delay type training size:', np.shape(delay_type_training))

time_crucial_trial_training1=time_crucial_trial[0:(count_inp_start)]
time_crucial_trial_training=list(map(bool,time_crucial_trial_training1))
print('time crucial trial training:', time_crucial_trial_training)
print('time crucial trial training size:', np.shape(time_crucial_trial_training))

reward_vec_training1=reward_vec[0:(count_inp_start)]
reward_vec_training=np.array(reward_vec_training1)
print('reward vec training:',reward_vec_training)
print('reward vec training size:', np.shape(reward_vec_training))

action_vec_training1=action_vec[0:(count_inp_start)]
action_vec_training=np.array(action_vec_training1)
print('action vec training:',action_vec_training)
print('action vec training size:', np.shape(action_vec_training))

inp_start_training1=params.inp_start[1][0:(count_inp_start)]
inp_start_training=np.array(inp_start_training1)
print('inp start training:',inp_start_training)
print('inp start training size:', np.shape(inp_start_training))

Pmax_training1=Pmax[0:(count_inp_start)]
Pmax_training=np.array(Pmax_training1)

summa=np.sum(time_crucial_trial_training)
print('summa:',summa)

trial_type_training1=trial_type_vec[0:(summa)]
trial_type_training=np.array(trial_type_training1)
print('trial type training:',trial_type_training)
print('trial type training size:', np.shape(trial_type_training))

print('####################################################################')
print('time tothtr:',time_tothr)
#print('firing PMC training:',firing_PMC_training )
print('firing PMC training size:',np.shape(firing_PMC_training))
#print('firing PMC test:',firing_PMC_test)
print('firing PMC test size:',np.shape(firing_PMC_test))
print('####################################################################')

delay_type_test1=delay_type[(count_inp_start):]
delay_type_test=np.array(delay_type_test1)
print('delay type test:',delay_type_test)
print('delay type test size:', np.shape(delay_type_test))

time_crucial_trial_test1=time_crucial_trial[(count_inp_start):]
time_crucial_trial_test=list(map(bool,time_crucial_trial_test1))
print('time crucial trial test:', time_crucial_trial_test)
print('time crucial trial test size:', np.shape(time_crucial_trial_test))

reward_vec_test1=reward_vec[(count_inp_start):]
reward_vec_test=np.array(reward_vec_test1)
print('reward vec test:',reward_vec_test)
print('reward vec test size:', np.shape(reward_vec_test))

action_vec_test1=action_vec[(count_inp_start):]
action_vec_test=np.array(action_vec_test1)
print('action vec test:',action_vec_test)
print('action vec test size:', np.shape(action_vec_test))

inp_start_test1=params.inp_start[1][(count_inp_start):]
inp_start_test=np.array(inp_start_test1)
print('inp start test:',inp_start_test)
print('inp start test size:', np.shape(inp_start_test))

Pmax_test1=Pmax[(count_inp_start):]
Pmax_test=np.array(Pmax_test1)

trial_type_test1=trial_type_vec[(summa):]
trial_type_test=np.array(trial_type_test1)
print('trial type test:',trial_type_test)
print('trial type test size:', np.shape(trial_type_test))
 
n_Go_training,n_Stop_Signal_training,n_Stop_Signal_correct_training, react_time_Go_training_1,react_time_Stop_Signal_total_training_1, react_time_Stop_Signal_training_1,react_time_Stop_Signal_correct_training_1, max_PMC_Go_training,max_PMC_Stop_Signal_total_training, max_PMC_Stop_Signal_training,max_PMC_Stop_Signal_correct_training,Pmax_Go_training,Pmax_Stop_Signal_total_training, Pmax_Stop_Signal_training, Pmax_Stop_Signal_correct_training =compute_net_parameters(firing_PMC,inp_start_training,trial_type_training,action_vec_training,time_crucial_trial_training,delay_type_training,Pmax_training,reward_vec_training)

Stop_Signal_failure_type_training=np.array(Stop_Signal_failure_type[0:(n_Stop_Signal_training)])
Stop_Signal_failure_type_test=np.array(Stop_Signal_failure_type[(n_Stop_Signal_training):])

freq_1_Stop_Signal_failure_type_training=np.mean(Stop_Signal_failure_type_training)*100
freq_0_Stop_Signal_failure_type_training=100-freq_1_Stop_Signal_failure_type_training

freq_1_Stop_Signal_failure_type_test=np.mean(Stop_Signal_failure_type_test)*100
freq_0_Stop_Signal_failure_type_test=100-freq_1_Stop_Signal_failure_type_test

num_1_Stop_Signal_failure_type_training=sum(Stop_Signal_failure_type_training)
num_0_Stop_Signal_failure_type_training=len(Stop_Signal_failure_type_training)-num_1_Stop_Signal_failure_type_training

num_1_Stop_Signal_failure_type_test=sum(Stop_Signal_failure_type_test)
num_0_Stop_Signal_failure_type_test=len(Stop_Signal_failure_type_test)-num_1_Stop_Signal_failure_type_test

mean_react_time_Go_training_1=np.mean(react_time_Go_training_1)
std_react_time_Go_training_1=np.std(react_time_Go_training_1)

mean_react_time_Stop_Signal_total_training_1=np.mean(react_time_Stop_Signal_total_training_1)
std_react_time_Stop_Signal_total_training_1=np.std(react_time_Stop_Signal_total_training_1)

mean_react_time_Stop_Signal_training_1=np.mean(react_time_Stop_Signal_training_1)
std_react_time_Stop_Signal_training_1=np.std(react_time_Stop_Signal_training_1)

mean_react_time_Stop_Signal_training_1_eter=np.mean(react_time_Stop_Signal_training_1[Stop_Signal_failure_type_training==0])
std_react_time_Stop_Signal_training_1_eter=np.std(react_time_Stop_Signal_training_1[Stop_Signal_failure_type_training==0])

mean_react_time_Stop_Signal_training_1_omol=np.mean(react_time_Stop_Signal_training_1[Stop_Signal_failure_type_training==1])
std_react_time_Stop_Signal_training_1_omol=np.std(react_time_Stop_Signal_training_1[Stop_Signal_failure_type_training==1])

mean_react_time_Stop_Signal_correct_training_1=np.mean(react_time_Stop_Signal_correct_training_1)
std_react_time_Stop_Signal_correct_training_1=np.std(react_time_Stop_Signal_correct_training_1)

mean_max_PMC_Go_training=np.mean(max_PMC_Go_training)
std_max_PMC_Go_training=np.std(max_PMC_Go_training)

mean_max_PMC_Stop_Signal_total_training=np.mean(max_PMC_Stop_Signal_total_training)
std_max_PMC_Stop_Signal_total_training=np.std(max_PMC_Stop_Signal_total_training)

mean_max_PMC_Stop_Signal_training=np.mean(max_PMC_Stop_Signal_training)
std_max_PMC_Stop_Signal_training=np.std(max_PMC_Stop_Signal_training)

mean_max_PMC_Stop_Signal_training_eter=np.mean(max_PMC_Stop_Signal_training[Stop_Signal_failure_type_training==0])
std_max_PMC_Stop_Signal_training_eter=np.std(max_PMC_Stop_Signal_training[Stop_Signal_failure_type_training==0])

mean_max_PMC_Stop_Signal_training_omol=np.mean(max_PMC_Stop_Signal_training[Stop_Signal_failure_type_training==1])
std_max_PMC_Stop_Signal_training_omol=np.std(max_PMC_Stop_Signal_training[Stop_Signal_failure_type_training==1])

mean_max_PMC_Stop_Signal_correct_training=np.mean(max_PMC_Stop_Signal_correct_training)
std_max_PMC_Stop_Signal_correct_training=np.std(max_PMC_Stop_Signal_correct_training)

mean_Pmax_Go_training=np.mean(Pmax_Go_training)
std_Pmax_Go_training=np.std(Pmax_Go_training)

mean_Pmax_Stop_Signal_total_training=np.mean(Pmax_Stop_Signal_total_training)
std_Pmax_Stop_Signal_total_training=np.std(Pmax_Stop_Signal_total_training)

mean_Pmax_Stop_Signal_training=np.mean(Pmax_Stop_Signal_training)
std_Pmax_Stop_Signal_training=np.std(Pmax_Stop_Signal_training)

mean_Pmax_Stop_Signal_training_eter=np.mean(Pmax_Stop_Signal_training[Stop_Signal_failure_type_training==0])
std_Pmax_Stop_Signal_training_eter=np.std(Pmax_Stop_Signal_training[Stop_Signal_failure_type_training==0])

mean_Pmax_Stop_Signal_training_omol=np.mean(Pmax_Stop_Signal_training[Stop_Signal_failure_type_training==1])
std_Pmax_Stop_Signal_training_omol=np.std(Pmax_Stop_Signal_training[Stop_Signal_failure_type_training==1])

mean_Pmax_Stop_Signal_correct_training=np.mean(Pmax_Stop_Signal_correct_training)
std_Pmax_Stop_Signal_correct_training=np.std(Pmax_Stop_Signal_correct_training)

right_inhibition_training=compute_right_inhibition(reward_vec_training,trial_type_training,time_crucial_trial_training)

accuracy_training=compute_global_accuracy(reward_vec_training,time_crucial_trial_training)

n_Go_test,n_Stop_Signal_test,n_Stop_Signal_correct_test,react_time_Go_test_1,react_time_Stop_Signal_total_test_1,react_time_Stop_Signal_test_1,react_time_Stop_Signal_correct_test_1,max_PMC_Go_test,max_PMC_Stop_Signal_total_test, max_PMC_Stop_Signal_test,max_PMC_Stop_Signal_correct_test,Pmax_Go_test,Pmax_Stop_Signal_total_test, Pmax_Stop_Signal_test, Pmax_Stop_Signal_correct_test=compute_net_parameters(firing_PMC,inp_start_test,trial_type_test, action_vec_test,time_crucial_trial_test,delay_type_test,Pmax_test,reward_vec_test)

mean_react_time_Go_test_1=np.mean(react_time_Go_test_1)
std_react_time_Go_test_1=np.std(react_time_Go_test_1)

mean_react_time_Stop_Signal_total_test_1=np.mean(react_time_Stop_Signal_total_test_1)
std_react_time_Stop_Signal_total_test_1=np.std(react_time_Stop_Signal_total_test_1)

mean_react_time_Stop_Signal_test_1=np.mean(react_time_Stop_Signal_test_1)
std_react_time_Stop_Signal_test_1=np.std(react_time_Stop_Signal_test_1)

mean_react_time_Stop_Signal_test_1_eter=np.mean(react_time_Stop_Signal_test_1[Stop_Signal_failure_type_test==0])
std_react_time_Stop_Signal_test_1_eter=np.std(react_time_Stop_Signal_test_1[Stop_Signal_failure_type_test==0])

mean_react_time_Stop_Signal_test_1_omol=np.mean(react_time_Stop_Signal_test_1[Stop_Signal_failure_type_test==1])
std_react_time_Stop_Signal_test_1_omol=np.std(react_time_Stop_Signal_test_1[Stop_Signal_failure_type_test==1])

mean_react_time_Stop_Signal_correct_test_1=np.mean(react_time_Stop_Signal_correct_test_1)
std_react_time_Stop_Signal_correct_test_1=np.std(react_time_Stop_Signal_correct_test_1)

mean_max_PMC_Go_test=np.mean(max_PMC_Go_test)
std_max_PMC_Go_test=np.std(max_PMC_Go_test)

mean_max_PMC_Stop_Signal_total_test=np.mean(max_PMC_Stop_Signal_total_test)
std_max_PMC_Stop_Signal_total_test=np.std(max_PMC_Stop_Signal_total_test)

mean_max_PMC_Stop_Signal_test=np.mean(max_PMC_Stop_Signal_test)
std_max_PMC_Stop_Signal_test=np.std(max_PMC_Stop_Signal_test)

mean_max_PMC_Stop_Signal_test_eter=np.mean(max_PMC_Stop_Signal_test[Stop_Signal_failure_type_test==0])
std_max_PMC_Stop_Signal_test_eter=np.std(max_PMC_Stop_Signal_test[Stop_Signal_failure_type_test==0])

mean_max_PMC_Stop_Signal_test_omol=np.mean(max_PMC_Stop_Signal_test[Stop_Signal_failure_type_test==1])
std_max_PMC_Stop_Signal_test_omol=np.std(max_PMC_Stop_Signal_test[Stop_Signal_failure_type_test==1])

mean_max_PMC_Stop_Signal_correct_test=np.mean(max_PMC_Stop_Signal_correct_test)
std_max_PMC_Stop_Signal_correct_test=np.std(max_PMC_Stop_Signal_correct_test)

mean_Pmax_Go_test=np.mean(Pmax_Go_test)
std_Pmax_Go_test=np.std(Pmax_Go_test)

mean_Pmax_Stop_Signal_total_test=np.mean(Pmax_Stop_Signal_total_test)
std_Pmax_Stop_Signal_total_test=np.std(Pmax_Stop_Signal_total_test)

mean_Pmax_Stop_Signal_test=np.mean(Pmax_Stop_Signal_test)
std_Pmax_Stop_Signal_test=np.std(Pmax_Stop_Signal_test)

mean_Pmax_Stop_Signal_test_eter=np.mean(Pmax_Stop_Signal_test[Stop_Signal_failure_type_test==0])
std_Pmax_Stop_Signal_test_eter=np.std(Pmax_Stop_Signal_test[Stop_Signal_failure_type_test==0])

mean_Pmax_Stop_Signal_test_omol=np.mean(Pmax_Stop_Signal_test[Stop_Signal_failure_type_test==1])
std_Pmax_Stop_Signal_test_omol=np.std(Pmax_Stop_Signal_test[Stop_Signal_failure_type_test==1])

mean_Pmax_Stop_Signal_correct_test=np.mean(Pmax_Stop_Signal_correct_test)
std_Pmax_Stop_Signal_correct_test=np.std(Pmax_Stop_Signal_correct_test)

right_inhibition_test=compute_right_inhibition(reward_vec_test,trial_type_test, time_crucial_trial_test)

accuracy_test=compute_global_accuracy(reward_vec_test,time_crucial_trial_test)

SSRT_test,delay_type_Stop_Signal_test=compute_SSRT(react_time_Go_test_1,delay_type_test,trial_type_test,time_crucial_trial_test,right_inhibition_test)

mean_delay_type_Stop_Signal_test= np.mean(delay_type_Stop_Signal_test)
std_delay_type_Stop_Signal_test= np.std(delay_type_Stop_Signal_test)

print('##############################################')
print(' Model output during training phase:')

print('mean reaction time Go Trials training 1 :', mean_react_time_Go_training_1)
print('std reaction time Go Trials training 1 :', std_react_time_Go_training_1)

print('mean reaction time StopSignal total Trials training 1:',mean_react_time_Stop_Signal_total_training_1 )
print('std reaction time StopSignal total Trials training 1:',std_react_time_Stop_Signal_total_training_1 )

print('mean reaction time StopSignal Trials training 1 :',mean_react_time_Stop_Signal_training_1 )
print('std reaction time StopSignal Trials training 1 :',std_react_time_Stop_Signal_training_1 )

print('mean reaction time StopSignal Trials correct training 1 :',mean_react_time_Stop_Signal_correct_training_1 )
print('std reaction time StopSignal Trials correct training 1 :',std_react_time_Stop_Signal_correct_training_1 )

print('mean max PMC Go training:',mean_max_PMC_Go_training)
print('std max PMC Go training:',std_max_PMC_Go_training)

print('mean max PMC StopSignal total training:',mean_max_PMC_Stop_Signal_total_training)
print('std max PMC StopSignal total training:',std_max_PMC_Stop_Signal_total_training)

print('mean max PMC StopSignal training:',mean_max_PMC_Stop_Signal_training)
print('std max PMC StopSignal training:',std_max_PMC_Stop_Signal_training)

print('mean max PMC StopSignal correct training:',mean_max_PMC_Stop_Signal_correct_training)
print('std max PMC StopSignal correct training:',std_max_PMC_Stop_Signal_correct_training)

print('mean Pmax Go training:',mean_Pmax_Go_training)
print('std Pmax Go training:',std_Pmax_Go_training)

print('mean Pmax StopSignal total training:',mean_Pmax_Stop_Signal_total_training)
print('std Pmax StopSignal total training:',std_Pmax_Stop_Signal_total_training)

print('mean Pmax StopSignal training:',mean_Pmax_Stop_Signal_training)
print('std Pmax StopSignal training:',std_Pmax_Stop_Signal_training)

print('mean Pmax StopSignal correct training:',mean_Pmax_Stop_Signal_correct_training)
print('std Pmax StopSignal correct training:',std_Pmax_Stop_Signal_correct_training)

print('% right inibiton trials before and after meta_value_hold thr training:',right_inhibition_training)

print('global accuracy before and after meta_value_hold thr training:',accuracy_training)
print('##############################################')

print('##############################################')
print(' Model output during test phase:')

print('mean reaction time Go Trials test 1 :', mean_react_time_Go_test_1)
print('std reaction time Go Trials test 1 :', std_react_time_Go_test_1)

print('mean reaction time StopSignal total Trials test 1:',mean_react_time_Stop_Signal_total_test_1 )
print('std reaction time StopSignal total Trials test 1:',std_react_time_Stop_Signal_total_test_1 )

print('mean reaction time StopSignal Trials test 1 :',mean_react_time_Stop_Signal_test_1 )
print('std reaction time StopSignal Trials test 1 :',std_react_time_Stop_Signal_test_1 )

print('mean reaction time StopSignal Trials correct test: 1 ',mean_react_time_Stop_Signal_correct_test_1 )
print('std reaction time StopSignal Trials correct test 1 :',std_react_time_Stop_Signal_correct_test_1 )

print('mean max PMC Go test:',mean_max_PMC_Go_test)
print('std max PMC Go test:',std_max_PMC_Go_test)

print('mean max PMC StopSignal total test:',mean_max_PMC_Stop_Signal_total_test)
print('std max PMC StopSignal total test:',std_max_PMC_Stop_Signal_total_test)

print('mean max PMC StopSignal test:',mean_max_PMC_Stop_Signal_test)
print('std max PMC StopSignal test:',std_max_PMC_Stop_Signal_test)

print('mean max PMC StopSignal test correct :',mean_max_PMC_Stop_Signal_correct_test)
print('std max PMC StopSignal test correct :',std_max_PMC_Stop_Signal_correct_test)

print('mean Pmax Go test:',mean_Pmax_Go_test)
print('std Pmax Go test:',std_Pmax_Go_test)

print('mean Pmax StopSignal total test:',mean_Pmax_Stop_Signal_total_test)
print('std Pmax StopSignal total test:',std_Pmax_Stop_Signal_total_test)

print('mean Pmax StopSignal test:',mean_Pmax_Stop_Signal_test)
print('std Pmax StopSignal test:',std_Pmax_Stop_Signal_test)

print('mean Pmax StopSignal correct  test:',mean_Pmax_Stop_Signal_correct_test)
print('std Pmax StopSignal correct test:',std_Pmax_Stop_Signal_correct_test)

print('stop signal reaction time test:', SSRT_test)

print('% right inibiton trials before and after meta_value_hold thr test:',right_inhibition_test)

print('global accuracy before and after meta_value_hold thr test:',accuracy_test)
print('##############################################')

print('freq omol StopSignal failure type training :', freq_1_Stop_Signal_failure_type_training )
print('freq eter StopSignal failure type training :',freq_0_Stop_Signal_failure_type_training )

print('num omol StopSignal failure type training:', num_1_Stop_Signal_failure_type_training)
print('num eter StopSignal failure type training:', num_0_Stop_Signal_failure_type_training)

print('freq omol StopSignal failure type test:',freq_1_Stop_Signal_failure_type_test )
print('freq eter StopSignal failure type test:',freq_0_Stop_Signal_failure_type_test )

print('num omol StopSignal failure type test:',num_1_Stop_Signal_failure_type_test )
print('num eter StopSignal failure type test', num_0_Stop_Signal_failure_type_test)
print('##############################################')

print('mean react time StopSignal training 1 eter:', mean_react_time_Stop_Signal_training_1_eter)
print('std react time StopSignal training 1 eter', std_react_time_Stop_Signal_training_1_eter)

print('mean react time StopSignal training 1 omol:', mean_react_time_Stop_Signal_training_1_omol)
print('std react time StopSignal training 1 omol', std_react_time_Stop_Signal_training_1_omol)

print('mean max PMC StopSignal training eter:',mean_max_PMC_Stop_Signal_training_eter )
print('std max PMC StopSignal training eter',std_max_PMC_Stop_Signal_training_eter )

print('mean max PMC StopSignal training omol:',mean_max_PMC_Stop_Signal_training_omol )
print('std max PMC StopSignal training omol',std_max_PMC_Stop_Signal_training_omol )

print('mean Pmax StopSignal training eter:',mean_Pmax_Stop_Signal_training_eter)
print('std Pmax StopSignal training eter:',std_Pmax_Stop_Signal_training_eter)

print('mean Pmax StopSignal training omol:',mean_Pmax_Stop_Signal_training_omol)
print('std Pmax StopSignal training omol:',std_Pmax_Stop_Signal_training_omol)

print('mean react time StopSignal test 1 eter:', mean_react_time_Stop_Signal_test_1_eter )
print('std react time StopSignal test 1 eter:', std_react_time_Stop_Signal_test_1_eter)

print('mean react time StopSignal test 1 omol:', mean_react_time_Stop_Signal_test_1_omol )
print('std react time StopSignal test 1 omol:', std_react_time_Stop_Signal_test_1_omol)

print('mean max PMC StopSignal test eter:',mean_max_PMC_Stop_Signal_test_eter )
print('std max PMC StopSignal test eter:', std_max_PMC_Stop_Signal_test_eter)

print('mean max PMC StopSignal test omol:',mean_max_PMC_Stop_Signal_test_omol )
print('std max PMC StopSignal test omol:', std_max_PMC_Stop_Signal_test_omol)

print('mean Pmax StopSignal test eter:',mean_Pmax_Stop_Signal_test_eter )
print('std Pmax StopSignal test eter:',std_Pmax_Stop_Signal_test_eter )

print('mean Pmax StopSignal test omol:',mean_Pmax_Stop_Signal_test_omol )
print('std Pmax StopSignal test omol:',std_Pmax_Stop_Signal_test_omol)

print('##############################################')

num_problems_training=np.sum(time_crucial_trial_training1)
num_problems_test=np.sum(time_crucial_trial_test1)

#training
num_problems_training_Go=0
num_problems_training_Stop_Signal=0
for i in range(num_problems_training):
    if trial_type_training[i]==1:
        num_problems_training_Stop_Signal=num_problems_training_Stop_Signal+1
    else:
        num_problems_training_Go=num_problems_training_Go+1
        
#test
num_problems_test_Go=0
num_problems_test_Stop_Signal=0
for i in range(num_problems_test):
    if trial_type_test[i]==1:
        num_problems_test_Stop_Signal=num_problems_test_Stop_Signal+1
    else:
        num_problems_test_Go=num_problems_test_Go+1

num_trials_between_two_problems_training=(len(time_crucial_trial_training1)-4*num_problems_training)/num_problems_training
num_trials_between_two_problems_test=(len(time_crucial_trial_test1)-4*num_problems_test)/num_problems_test

print('num problems training:',num_problems_training)
print('num problems training Go:',num_problems_training_Go)
print('num problems training StopSignal:',num_problems_training_Stop_Signal)
print('num trials between two problems training:',num_trials_between_two_problems_training)

print('num problems test:',num_problems_test)
print('num problems test Go:',num_problems_test_Go)
print('num problems test StopSignal:',num_problems_test_Stop_Signal)
print('num trials between two problems test:',num_trials_between_two_problems_test)

print('###############################')

print('trials needed to learn hold meta-value:',time_tothr)
print('trials from learn hold meta-value and the end:',time_toend)
print(' meta-value hold at time_tothr: ',MetaValue_Hold[time_tothr])
print(' meta-value hold at time_to the end: ',MetaValue_Hold[time_toend])
print(' meta-value slope:', MetaValue_Hold[time_tothr]/time_tothr)

ACC_Q_hold_train=ACC_Q[1][0].memory[1:(count_inp_start+1)]
ACC_Q_hold_test=ACC_Q[1][0].memory[(count_inp_start+1):]

print('###############################')

print('Qvalue max train mean:',max(ACC_Q_hold_train))
print('Qvalue max train median:',np.median(ACC_Q_hold_train))

print('Qvalue max test mean: ',max(ACC_Q_hold_test))
print('Qvalue max test median: ',np.median(ACC_Q_hold_test))

print('###############################')

print('min TD:', min(TD_memory))
print('max TD:', max(TD_memory))

print('min S0:', min(Striatum_Neu0.s0_memory))
print('max S0:', max(Striatum_Neu0.s0_memory))

reward_vec_crucial_test=reward_vec_test[np.where(time_crucial_trial_test)]

react_time_Stop_Signal_total_test_delay = []
react_time_Stop_Signal_failure_test_delay = []
react_time_Stop_Signal_correct_test_delay = []

delay_type_crucial=delay_type_test[np.where(time_crucial_trial_test)]

delay_type_Stop_Signal_failure_test=delay_type_crucial[np.logical_and((trial_type_test==0), (reward_vec_crucial_test==0))] 
delay_type_Stop_Signal_correct_test=delay_type_crucial[np.logical_and((trial_type_test==0), (reward_vec_crucial_test==1))]

for ii in range(len(vector_delay)):
    react_time_Stop_Signal_total_test_delay.append(np.mean(react_time_Stop_Signal_total_test_1[np.where(delay_type_Stop_Signal_test == vector_delay[ii])]))
    react_time_Stop_Signal_failure_test_delay.append(np.mean(react_time_Stop_Signal_test_1[np.where(delay_type_Stop_Signal_failure_test == vector_delay[ii])]))
    react_time_Stop_Signal_correct_test_delay.append(np.mean(react_time_Stop_Signal_correct_test_1[np.where(delay_type_Stop_Signal_correct_test == vector_delay[ii])]))

reward_vec_test_crucial  = reward_vec_test[np.where(time_crucial_trial_test)]
reward_vec_test_crucial_Stop_Signal = reward_vec_test_crucial[np.where(trial_type_test==0)]
RI_Stop_Signal_delay = []
for ii in range(len(vector_delay)):
    RI_Stop_Signal_delay.append(np.mean(reward_vec_test_crucial_Stop_Signal[np.where(delay_type_Stop_Signal_test == vector_delay[ii])]))

print('##############################################')
print('right inhibition StopSignal delay test',RI_Stop_Signal_delay)
print('##############################################')

print('##############################################')
print('react time StopSignal total test delay ',react_time_Stop_Signal_total_test_delay)
print('react time StopSignal failure test delay ',react_time_Stop_Signal_failure_test_delay)
print('react time StopSignal correct test delay',react_time_Stop_Signal_correct_test_delay)

entropy_vec_training1=entropy_vec[0:(count_inp_start)]
entropy_vec_training=np.array(entropy_vec_training1)
print('entropy vec training:', entropy_vec_training)
print('entropy vec training size:',np.shape(entropy_vec_training))

entropy_vec_test1=entropy_vec[(count_inp_start):]
entropy_vec_test=np.array(entropy_vec_test1)
print('entropy vec test:', entropy_vec_test)
print('entropy vec test size:',np.shape(entropy_vec_test))

entropy_vec_crucial=entropy_vec_test[np.where(time_crucial_trial_test)]

entropy_vec_Go_test= entropy_vec_crucial[np.where(trial_type_test)] 
entropy_vec_Stop_Signal_failure_test=entropy_vec_crucial[np.logical_and((trial_type_test==0), (reward_vec_crucial_test==0))] 
entropy_vec_Stop_Signal_correct_test=entropy_vec_crucial[np.logical_and((trial_type_test==0), (reward_vec_crucial_test==1))]

mean_entropy_vec_Go_test=np.mean(entropy_vec_Go_test)
std_entropy_vec_Go_test=np.std(entropy_vec_Go_test)

mean_entropy_vec_Stop_Signal_failure_test=np.mean(entropy_vec_Stop_Signal_failure_test)
std_entropy_vec_Stop_Signal_failure_test=np.std(entropy_vec_Stop_Signal_failure_test)

mean_entropy_vec_Stop_Signal_correct_test=np.mean(entropy_vec_Stop_Signal_correct_test)
std_entropy_vec_Stop_Signal_correct_test=np.std(entropy_vec_Stop_Signal_correct_test)

print('###############################')

print('mean entropy Go test:',mean_entropy_vec_Go_test)
print('std entropy Go test:', std_entropy_vec_Go_test)

print('mean entropy StopSignal failure test:',mean_entropy_vec_Stop_Signal_failure_test)
print('std entropy StopSignal failure test',std_entropy_vec_Stop_Signal_failure_test)

print('mean entropy StopSignal correct test:',mean_entropy_vec_Stop_Signal_correct_test)
print('std entropy StopSignal correct test:',std_entropy_vec_Stop_Signal_correct_test)

print('###############################')

inp_start_crucial=inp_start_test[np.where(time_crucial_trial_test)]

inp_start_Go_test=inp_start_crucial[np.where(trial_type_test)]
inp_start_Stop_Signal_failure_test=inp_start_crucial[np.logical_and((trial_type_test==0), (reward_vec_crucial_test==0))] 
inp_start_Stop_Signal_correct_test=inp_start_crucial[np.logical_and((trial_type_test==0), (reward_vec_crucial_test==1))]

beta_new_test1=beta_new[(count_inp_start):]
beta_new_test=np.array(beta_new_test1)

beta_new_crucial=beta_new_test[np.where(time_crucial_trial_test)]

beta_new_Go_test=beta_new_crucial[np.where(trial_type_test)]
beta_new_Stop_Signal_failure_test=beta_new_crucial[np.logical_and((trial_type_test==0), (reward_vec_crucial_test==0))] 
beta_new_Stop_Signal_correct_test=beta_new_crucial[np.logical_and((trial_type_test==0), (reward_vec_crucial_test==1))]

#np.savetxt('entropy_vec_test_open_loop40.txt',entropy_vec_test)
#np.savetxt('beta_new_open_loop40.txt',beta_new_test)























