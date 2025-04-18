#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federicarobertazzi
"""

import numpy as np
import matplotlib.pyplot as plt


#from mechanisms_meta_learning import serotonin_to_dopamine_upreg,dopamine_to_serotonin_upreg
#from mechanisms_meta_learning import serotonin_to_dopamine_downreg,dopamine_to_serotonin_upreg,choose_func
#from mechanisms_meta_learning import serotonin_to_dopamine_downreg,dopamine_to_serotonin_downreg,choose_func
from mechanisms_meta_learning import serotonin_to_dopamine_upreg,dopamine_to_serotonin_downreg

serotonin=np.linspace(0.1,1,100)
D=np.linspace(0.1,1,100)

#nei parametri di quelle negative tenere conto dell offset a 1 ed includerlo direttamente nel parametri
#offset=1 
#-k0log (x+k1)=k0newlog(x+k1new)

k_VTA_D0=np.linspace (0.01,4,50)#np.linspace (1,8,20)

k_VTA_D1=np.linspace (0.01,1,100) #np.linspace (0.5,3,20) 

X, Y = np.meshgrid(k_VTA_D0, k_VTA_D1)
print(np.size(X,0))
out=np.zeros((np.size(X,0), np.size(X,1), len(serotonin)))

vec=np.ones((np.size(X,0), np.size(X,1)))

for i in range(np.size(X,0)):
    for j in range(np.size(X,1)):
        for k in range(len(serotonin)):
            out[i,j,k]=serotonin_to_dopamine_upreg(serotonin[k],[X[i,j], Y[i,j]])
     
        temp= np.squeeze(out[i,j,:])

        if (max(temp)<0.98 or min(temp)>0.02 or all(x<0.001 or x>0.99 for x in temp) or sum(temp)==0 or np.isnan(temp).any()):
            vec[i,j]=0

fig,ax=plt.subplots(1,1)
cp = ax.contourf(X, Y, vec,1)
fig.colorbar(cp) 
ax.set_title('region of existence')
ax.set_xlabel('k_VTA_D0')
ax.set_ylabel('k_VTA_D1')
plt.show()    
    
    
        