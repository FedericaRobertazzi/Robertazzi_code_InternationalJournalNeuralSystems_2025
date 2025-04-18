#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federicarobertazzi
"""
import matplotlib.pyplot as plt
import numpy as np
from mechanisms_meta_learning import D2_Striatum
import sympy as sp

#seacrhing parameters in the etaD2,high efficacy condition

#a0_D2_to_s0 =[1.2, 0.67, 0.5]#reference condition
a0_D2_to_s0 = [1.05,3.5,0.5]#etaD2,high condition 

D2=np.linspace(0.1,1,100)
h=(1-0.1)/100 #dopamine range/100

s0=[]

for i in D2:
    s0.append(D2_Striatum(a0_D2_to_s0,i))

plt.figure()
plt.plot(D2,s0)
plt.xlabel('D2',size=17)
plt.ylabel('s0',size=17)
plt.grid()
plt.show()

#sigmoid min and max value in [D2]=0 e [D2]=1, respectively 
s0_min=D2_Striatum(a0_D2_to_s0,0.1)
s0_max=D2_Striatum(a0_D2_to_s0,1) 

index=(s0_max-s0_min)/(1-0.1) #raw index 

print('min s0 :', s0_min)
print('max s0 :', s0_max)
print('index:', index)

#first order derivative (symbolic)
def D2_Striatum_symbolic(D2):
    return a0_D2_to_s0[0]/(1+sp.exp(-(a0_D2_to_s0[1]*(D2 - a0_D2_to_s0[2]))))

D2=sp.symbols('D2')
fun_D2=D2_Striatum_symbolic(D2)
D2_prime=fun_D2.diff(D2)
D2_n=np.linspace(0.1,1,100)

#first order derivative (numeric)
def D2_Striatum_numeric(D2):
    return 0.638619242180386*np.exp(-3.5*D2)/(0.173773943450445 + np.exp(-3.5*D2))**2    #etaD2, large condition

#def D2_Striatum_numeric(D2):    
    #return 0.575131821427458*np.exp(-0.67*D2)/(0.71533808635256 + np.exp(-0.67*D2))**2  #reference condition
   
D2_prime_n=[]

for i in D2_n:
    D2_prime_n.append(D2_Striatum_numeric(i))
    
D2_prime_n=np.array(D2_prime_n)

plt.figure()
plt.plot(D2_n,D2_prime_n)
plt.xlabel('D2',size=17)
plt.ylabel('s0',size=17)

def annot_max(D2_n,D2_prime_n, ax=None):
    xmax = D2_n[np.argmax(D2_prime_n)]
    ymax = D2_prime_n.max()
    text= "D2={:.3f}, s0={:.3f}".format(xmax, ymax)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmax, ymax), xytext=(0.94,0.96), **kw)
annot_max(D2_n,D2_prime_n)
plt.show()