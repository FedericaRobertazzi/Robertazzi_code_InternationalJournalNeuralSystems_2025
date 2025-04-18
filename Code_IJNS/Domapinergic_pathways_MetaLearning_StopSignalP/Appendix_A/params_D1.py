#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federicarobertazzi
"""
import matplotlib.pyplot as plt
import numpy as np
from mechanisms_meta_learning import rel_D1_beta 
import sympy as sp

#seacrhing parameters in the etaD1,low efficacy condition

a0_D1_to_beta = [10, 9.5, 0.5]#reference condition
#a0_D1_to_beta = [11.42, 1.81, 0.5]#etaD1,low condition

#ka_rate=1.2/1.05 #D2 decrease--->D1 increase 
#kb_rate=0.67/3.5 #D2 increase--->D1 decrese 
#kc_rate=0.5/0.5 #same 

D1=np.linspace(0.1,1,100)
h=(1-0.1)/100 #dopamine range/100

beta0=[]

for i in D1:
    beta0.append(rel_D1_beta(a0_D1_to_beta,i))

plt.figure()
plt.plot(D1,beta0)
plt.xlabel('D1',size=17)
plt.ylabel('beta0',size=17)
plt.grid()
plt.show()

#sigmoid min and max value in [D2]=0 e [D2]=1, respectively 
beta0_min=rel_D1_beta(a0_D1_to_beta,0.1)
beta0_max=rel_D1_beta(a0_D1_to_beta,1) 

index=(beta0_max-beta0_min)/(1-0.1) #raw index 

print('min beta0 :', beta0_min)
print('max beta0 :', beta0_max)
print('index:', index)

#first order derivative (symbolic)
def rel_D1_beta_symbolic(D1):
    return a0_D1_to_beta[0]/(1+sp.exp(-(a0_D1_to_beta[1]*(D1 - a0_D1_to_beta[2]))))

D1=sp.symbols('D1')
fun_D1=rel_D1_beta_symbolic(D1)
D1_prime=fun_D1.diff(D1)
D1_n=np.linspace(0.1,1,100)

#first order derivative (numeric)
def rel_D1_beta_numeric(D1):
     return 0.82191104429646*np.exp(-9.5*D1)/(0.00865169520312063 + np.exp(-9.5*D1))**2 

#def rel_D1_beta_numeric(D1):
     #return 8.36196167345642*np.exp(-1.81*D1)/(0.404541885103019 + np.exp(-1.81*D1))**2
   
D1_prime_n=[]

for i in D1_n:
    D1_prime_n.append(rel_D1_beta_numeric(i))
    
D1_prime_n=np.array(D1_prime_n)

plt.figure()
plt.plot(D1_n,D1_prime_n)
plt.xlabel('D1',size=17)
plt.ylabel('beta0',size=17)

def annot_max(D1_n,D1_prime_n, ax=None):
    xmax = D1_n[np.argmax(D1_prime_n)]
    ymax = D1_prime_n.max()
    text= "D1={:.3f}, s0={:.3f}".format(xmax, ymax)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmax, ymax), xytext=(0.94,0.96), **kw)
annot_max(D1_n,D1_prime_n)
plt.show()
