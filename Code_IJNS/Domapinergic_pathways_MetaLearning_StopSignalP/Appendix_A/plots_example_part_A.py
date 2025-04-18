#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federicarobertazzi
"""
# toplot = [0, 1]
# for i in toplot:
#     for j in toplot:   
#         plt.figure()         
#         plt.plot(firing_PPC[i][j],label="PPC")
#         plt.plot(firing_ACC[i][j],label="ACC")
#         plt.plot(firing_LPFC[i][j],label="LPFC")
#         plt.plot(firing_Striatum[i][j],label="Striatum")
#         plt.plot(firing_SNr[i][j],label="SNr")
#         plt.plot(firing_Thalamus[i][j],label="Thalamus")
#         plt.plot(firing_PMC[i][j],label="PMC")
#         plt.legend(loc = 'best')
#         plt.ylim(0,2.5)
#         plt.xlabel("Time(s)", size=15)
#         plt.ylabel("Firing Rate(Hz))",size=15)
#         plt.title("Firing Rate " + str(i) + "" + str(j),size=15)
#         plt.show()

# plt.figure()         
# #toplot = [0, 1]
# #for i in toplot:
# #    for j in toplot:   
# #        plt.plot(firing_PMC[i][j],label="PMC_" + str(i) + "" + str(j))
# #        plt.plot(firing_PMC[i][j],label="PMC")
# plt.plot(firing_PMC[0][0],label="Left")
# plt.plot(firing_PMC[0][1],label="Right")
# plt.plot(firing_PMC[1][0],label="Hold")
# plt.ylim(0,1)
# plt.xlim(0,60000)
# plt.xlabel("Time [samples]", size=17)
# plt.ylabel("PMC Firing Rate [a.u.]",size=17)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.02),
#           fancybox=True, shadow=True, ncol=5)
# plt.show()    

# plt.figure()         
# #toplot = [0, 1]
# #for i in toplot:
# #    for j in toplot:   
# #        plt.plot(firing_PMC[i][j],label="PMC_" + str(i) + "" + str(j))
# #        plt.plot(firing_PMC[i][j],label="PMC")
# plt.plot(firing_PMC[0][0],label="Left")
# plt.plot(firing_PMC[0][1],label="Right")
# plt.plot(firing_PMC[1][0],label="Hold")
# plt.ylim(0,1)
# plt.xlim(0,20000)
# plt.xlabel("Time [samples]", size=17)
# plt.ylabel("PMC Firing Rate [a.u.]",size=17)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.02),
#           fancybox=True, shadow=True, ncol=5)
# plt.show()    

# plt.figure()         
# #toplot = [0, 1]
# #for i in toplot:
# #    for j in toplot:   
# #        plt.plot(firing_PMC[i][j],label="PMC_" + str(i) + "" + str(j))
# #        plt.plot(firing_PMC[i][j],label="PMC")
# plt.plot(firing_PMC[0][0],label="Left")
# plt.plot(firing_PMC[0][1],label="Right")
# plt.plot(firing_PMC[1][0],label="Hold")
# plt.ylim(0,1)
# plt.xlim(20000,40000)
# plt.xlabel("Time [samples]", size=17)
# plt.ylabel("PMC Firing Rate [a.u.]",size=17)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.02),
#           fancybox=True, shadow=True, ncol=5)
# plt.show()    

# plt.figure()         
# # toplot = [0, 1]
# # for i in toplot:
# #    for j in toplot:   
# #        plt.plot(firing_PMC[i][j],label="PMC_" + str(i) + "" + str(j))
# #        plt.plot(firing_PMC[i][j],label="PMC")
# plt.plot(firing_PMC[0][0],label="Left")
# plt.plot(firing_PMC[0][1],label="Right")
# plt.plot(firing_PMC[1][0],label="Hold")
# plt.ylim(0,1)
# plt.xlim(40000,60000)
# plt.xlabel("Time [samples]", size=17)
# plt.ylabel("PMC Firing Rate [a.u.]",size=17)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.02),
#           fancybox=True, shadow=True, ncol=5)
# plt.show()  

# plt.figure()         
# # toplot = [0, 1]
# # for i in toplot:
# #     for j in toplot:   
# #         plt.plot(ACC_Q[i][j].memory,label="action value_"+ str(i) + "" + str(j))
# plt.plot(ACC_Q[0][0].memory,label="Left")
# plt.plot(ACC_Q[0][1].memory,label="Right")
# plt.plot(ACC_Q[1][0].memory,label="Hold")
# plt.xlim(0,400)
# plt.ylim(-0.5, 3)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.02),
#           fancybox=True, shadow=True, ncol=5)
# plt.xlabel("Stimuli", size=17)
# plt.ylabel("Q [a.u.]",size=17)
# plt.show()

# plt.figure()         
# # toplot = [0, 1]
# # for i in toplot:
# #     for j in toplot:   
# #         plt.plot(ACC_Q[i][j].memory,label="action value_"+ str(i) + "" + str(j))
# plt.plot(ACC_Q[0][0].memory,label="Left")
# plt.plot(ACC_Q[0][1].memory,label="Right")
# plt.plot(ACC_Q[1][0].memory,label="Hold")
# plt.xlim(0,133)
# plt.ylim(-0.5, 3)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.02),
#           fancybox=True, shadow=True, ncol=5)
# plt.xlabel("Stimuli", size=17)
# plt.ylabel("Q [a.u.]",size=17)
# plt.show()

# plt.figure()         
# # toplot = [0, 1]
# # for i in toplot:
# #     for j in toplot:   
# #         plt.plot(ACC_Q[i][j].memory,label="action value_"+ str(i) + "" + str(j))
# plt.plot(ACC_Q[0][0].memory,label="Left")
# plt.plot(ACC_Q[0][1].memory,label="Right")
# plt.plot(ACC_Q[1][0].memory,label="Hold")
# plt.xlim(133,266)
# plt.ylim(-0.5, 3)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.02),
#           fancybox=True, shadow=True, ncol=5)
# plt.xlabel("Stimuli", size=17)
# plt.ylabel("Q [a.u.]",size=17)
# plt.show()

# plt.figure()         
# # toplot = [0, 1]
# # for i in toplot:
# #     for j in toplot:   
# #         plt.plot(ACC_Q[i][j].memory,label="action value_"+ str(i) + "" + str(j))
# plt.plot(ACC_Q[0][0].memory,label="Left")
# plt.plot(ACC_Q[0][1].memory,label="Right")
# plt.plot(ACC_Q[1][0].memory,label="Hold")
# plt.xlim(266,400)
# plt.ylim(-0.5, 3)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.02),
#           fancybox=True, shadow=True, ncol=5)
# plt.xlabel("Stimuli", size=17)
# plt.ylabel("Q [a.u.]",size=17)
# plt.show()

# plt.figure()         
# plt.scatter(list(range(len(reward_vec))),reward_vec)
# plt.ylim(0,1)
# plt.xlim(0,400)
# plt.xlabel("Stimuli", size=15)
# plt.ylabel("r",size=15)
# plt.show()                  

# plt.figure()         
# plt.plot(beta,'black',label="beta")
# plt.xlabel("Stimuli", size=17)
# plt.ylabel(r"$\beta$ [a.u.] ",size=17)
# plt.xlim(0,400)
# plt.ylim(0,10)
# plt.show()

# plt.figure()         
# plt.plot(beta,'black',label="beta")
# plt.xlabel("Stimuli", size=17)
# plt.ylabel(r"$\beta$ [a.u.] ",size=17)
# plt.xlim(0,133)
# plt.ylim(0,10)
# plt.show()
 
# plt.figure()         
# plt.plot(beta,'black',label="beta")
# plt.xlabel("Stimuli", size=17)
# plt.ylabel(r"$\beta$ [a.u.] ",size=17)
# plt.xlim(133,266)
# plt.ylim(0,10)
# plt.show() 
        
# plt.figure()         
# plt.plot(beta,'black',label="beta")
# plt.xlabel("Stimuli", size=17)
# plt.ylabel(r"$\beta$ [a.u.] ",size=17)
# plt.xlim(266,400)
# plt.ylim(0,10)
# plt.show()

# plt.figure()   
# plt.scatter(list(range(len(TD_memory))),TD_memory,label="TD", color='black')
# plt.xlim(0,400)
# plt.ylim(-1,1)
# plt.xlabel("Stimuli", size=17)
# plt.ylabel(r"$\delta$ [a.u.] ",size=17)
# plt.show()
  
# plt.figure()   
# plt.scatter(list(range(len(TD_memory))),TD_memory,label="TD",color='black')
# plt.xlim(0,133)
# plt.ylim(-1,1)
# plt.xlabel("Stimuli", size=17)
# plt.ylabel(r"$\delta$ [a.u.] ",size=17)
# plt.show()     
 
# plt.figure() 
# plt.scatter(list(range(len(TD_memory))),TD_memory,label="TD", color='black')
# plt.xlim(133,266)
# plt.ylim(-1,1)
# plt.xlabel("Stimuli", size=17)
# plt.ylabel(r"$\delta$ [a.u.] ",size=17)
# plt.show()     

# plt.figure() 
# plt.scatter(list(range(len(TD_memory))),TD_memory,label="TD", color='black')
# plt.xlim(266,400)
# plt.ylim(-1,1)
# plt.xlabel("Stimuli", size=17)
# plt.ylabel(r"$\delta$ [a.u.] ",size=17)
# plt.show() 

# plt.figure()         
# plt.plot(Pmax,label="Pmax",color='black')
# plt.ylim(0,1)
# plt.xlim(0,400)
# plt.xlabel("Stimuli", size=17)
# plt.ylabel("Pmax",size=17)
# plt.show()

# plt.figure()    
# plt.plot(MetaValue_Hold,'blue', label="Meta-Value Hold")
# plt.plot(MetaValue_Direction,'teal',label="Meta-Value Direction")
# plt.xlim(0,400)
# plt.axhline(y=-0.25,xmin=0, xmax=400, linestyle ="dotted", color ='red', label='Trheshold')
# plt.xlabel('Stimuli',size = 17)
# plt.ylabel('Meta-value [a.u.]',size = 17)
# plt.legend(loc='upper center', bbox_to_anchor=(0.78, 0.5),
#           fancybox=True, shadow=True, ncol=1)
# plt.show()

# plt.figure()         
# plt.plot(action_vec,'black', alpha=0.8, label="Action")
# plt.plot(reward_vec,'salmon',label='Reward')
# plt.plot(time_hold,'darkred',label='Hold Signal Time')
# plt.plot(delta_rew,'darkorchid',label='Delta Reward')
# plt.xlim(0,400)
# plt.ylim(-1,3)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.02),
#           ncol=2, fancybox=True, shadow=True)
# plt.xlabel('Stimuli',size = 17)
# plt.ylabel('Event [a.u.]',size = 17)
# plt.show()

# plt.figure()         
# plt.plot(action_vec,'black', alpha=0.8, label="Action")
# plt.plot(reward_vec,'salmon',label='Reward')
# plt.plot(time_hold,'darkred',label='Hold Signal Time')
# plt.plot(delta_rew,'darkorchid',label='Delta Reward')
# plt.xlim(0,133)
# plt.ylim(-1,3)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.02),
#           ncol=2, fancybox=True, shadow=True)
# plt.xlabel('Stimuli',size = 17)
# plt.ylabel('Event [a.u.]',size = 17)
# plt.show()

# plt.figure()         
# plt.plot(action_vec,'black', alpha=0.8, label="Action")
# plt.plot(reward_vec,'salmon',label='Reward')
# plt.plot(time_hold,'darkred',label='Hold Signal Time')
# plt.plot(delta_rew,'darkorchid',label='Delta Reward')
# plt.xlim(133,266)
# plt.ylim(-1,3)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.02),
#           ncol=2, fancybox=True, shadow=True)
# plt.xlabel('Stimuli',size = 17)
# plt.ylabel('Event [a.u.]',size = 17)
# plt.show()

# plt.figure()         
# plt.plot(action_vec,'black', alpha=0.8, label="Action")
# plt.plot(reward_vec,'salmon',label='Reward')
# plt.plot(time_hold,'darkred',label='Hold Signal Time')
# plt.plot(delta_rew,'darkorchid',label='Delta Reward')
# plt.xlim(266,400)
# plt.ylim(-1,3)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.02),
#           ncol=2, fancybox=True, shadow=True)
# plt.xlabel('Stimuli',size = 17)
# plt.ylabel('Event [a.u.]',size = 17)
# plt.show()

# plt.figure()
# plt.stem(trial_type_vec,label='trial type')
# plt.xlabel('Stimuli',size = 17)
# plt.legend(loc = 'best')
# plt.show()

# plt.figure()
# plt.plot(delay_type,label='delay type')
# plt.xlabel('Stimuli',size = 17)
# plt.xlim(0,400)
# plt.legend(loc = 'best')
# plt.show()

# plt.figure()
# plt.plot(time_crucial_trial,label='time crucial trial')
# plt.xlabel('Stimuli',size = 17)
# plt.xlim(0,400)
# plt.legend(loc = 'best')
# plt.show()  

# j=-1
# summa_time_crucial_and_trial_type=np.zeros_like(time_crucial_trial)
# for i in range(len(time_crucial_trial)):
#     if (time_crucial_trial[i]==1):
#         j=j+1
#         print(j)
#         if (trial_type_vec[j]==1):
#             summa_time_crucial_and_trial_type[i]=1            
#         else:
#             summa_time_crucial_and_trial_type [i]=-1
        
# plt.figure()    
# plt.plot(summa_time_crucial_and_trial_type,label="summa time crucial and trial type")
# plt.legend(loc = 'best')
# plt.xlabel('Stimuli',size = 17)
# plt.xlim(0,400)
# plt.show()

# plt.figure()
# for i in range (3):
#    plt.plot(matrix_P_vec[i,:])
# plt.xlabel('stimuli', size=17)
# plt.ylabel('matrix P vec ', size=17)
# plt.xlim(0,1000)
# plt.show()
# plt.figure()
# plt.plot(entropy_vec, c='black')
# plt.xlabel('stimuli', size=17)
# plt.ylabel('entropy', size=17)
# plt.xlim(0,1000)
# plt.show()
# plt.figure()
# plt.plot(beta_new, c='black')
# plt.xlabel('stimuli', size=17)
# plt.ylabel('beta new', size=17)
# plt.xlim(0,1000)
# plt.show()
# plt.figure()
# plt.plot(beta, c='black')
# plt.xlabel('stimuli', size=17)
# plt.ylabel('beta origin ', size=17)
# plt.xlim(0,1000)
# plt.show()

# plt.figure()
# plt.plot(inp_start_test, entropy_vec_test)
# plt.xlabel('inp start test', size=17)
# plt.ylabel('entropy test', size=17)
# plt.show()

# plt.figure()
# plt.plot(inp_start_Go_test, entropy_vec_Go_test, label= 'Go test')
# plt.plot(inp_start_Stop_Signal_failure_test, entropy_vec_Stop_Signal_failure_test,label='StopSignal failire test')
# plt.plot(inp_start_Stop_Signal_correct_test, entropy_vec_Stop_Signal_correct_test, label='StopSignal correct test')
# plt.plot()
# plt.xlabel('insp start', size=17)
# plt.ylabel('entropy test', size=17)
# plt.legend()
# plt.show()

# plt.figure()
# plt.scatter(beta_new_test, entropy_vec_test, c= 'black')
# plt.xlabel('beta new test', size=17)
# plt.ylabel('entropy test', size=17)
# plt.show()

# plt.figure()
# plt.scatter(beta_new_Go_test, entropy_vec_Go_test,color='blue', label='Go_test')
# plt.scatter(beta_new_Stop_Signal_failure_test, entropy_vec_Stop_Signal_failure_test,color='red', label='StopSignal failure test')
# plt.scatter(beta_new_Stop_Signal_correct_test, entropy_vec_Stop_Signal_correct_test,color='purple',  label='StopSignal correct test')
# plt.xlabel('beta new test', size=17)
# plt.ylabel('entropy test', size=17)
# plt.legend()
# plt.ylim(0,1)
# plt.xlim(0,10)
# plt.show()
