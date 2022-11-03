#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 13:36:53 2022

@author: mac
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class HodgkinHuxley:
    
    def __init__(self):
        self.v0 = -65
        self.n0 = 0.3
        self.h0 = 0.6
        self.m0 = 0.05
        self.ENa = 55
        self.EK = -77
        self.EL = -65
        self.gNa = 40
        self.gL = 0.3
        self.gK = 35
        self.C = 1
        
    def alpha_n(self,v):
        return 0.02*(v-25)/(1 - np.exp(-(v-25) / 9))

    def beta_n(self,v):
        return -0.002*(v-25)/(1 - np.exp((v-25) / 9))
    
    def alpha_m(self,v):
        return 0.182*(v+35)/(1 - np.exp(-(v+35) / 9))

    def beta_m(self,v):
        return -0.124*(v+35)/(1 - np.exp((v+35) / 9))

    def alpha_h(self,v):
        return 0.25*np.exp(-(v+90)/12)

    def beta_h(self,v):
        return 0.25*(np.exp((v+62) / 6))/(np.exp((v+90) / 12))
    
    def I_K(self,v,n):
        return self.gK * n**4 * (v - self.EK)
    
    def I_Na(self,v,m,h):
        return self.gNa * m**3 * h * (v - self.ENa)

    def I_L(self,v):
        return self.gL * (v - self.EL)
    
    def set_current(self,name,amp,start,end):
        current = {'step': self.step_current,
                   'custom': self.custom_current}
        self.I = current[name]
        self.amp = amp
        self.start = start
        self.end = end
        
    def step_current(self,t):
        if(t>=self.start and t<=self.end):
            return self.amp
        else:
            return 0
        
    def custom_current(self,t):
        if(t>=self.start and t<=self.end):
            return self.amp
        
        elif(t>=15 and t<=35):
            return 40
        else:
            return 0
        
    def set_capacitance(self,capacitance):
        self.C = capacitance
        
    
    def compute_derivatives(self,init_state, t):

        v, m, h, n = init_state

        dvdt = (self.I(t) - self.I_Na(v, m, h) - self.I_K(v, n) - self.I_L(v)) / self.C
        dndt = self.alpha_n(v)*(1-n) - self.beta_n(v)*n
        dmdt = self.alpha_m(v)*(1-m) - self.beta_m(v)*m
        dhdt = self.alpha_h(v)*(1-h) - self.beta_h(v)*h

        return dvdt, dmdt, dhdt, dndt
    
    def plot_voltage(self,start=0,end=100):
        t = np.arange(start,end, 0.01)
        init_state = [self.v0, self.m0,self.h0,self.n0]  
        ans = odeint(lambda state,t: self.compute_derivatives(state,t), init_state,t)
        v = ans[:,0]
        vecI = np.vectorize(self.I)
        I = vecI(t)
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 2))
        axes[0].plot(t,v)
        axes[0].set_xlabel('time(ms)')
        axes[0].set_ylabel('v(mv)')
        axes[0].set_title('voltage')
        axes[1].plot(t,I)
        axes[1].set_xlabel('time(ms)')
        axes[1].set_ylabel('amplitude')
        axes[1].set_title(f'current = {self.amp}')
        plt.show()
        
    def plot_current(self):
        t = np.arange(0,100, 0.01)
        vecI = np.vectorize(self.I)
        I = vecI(t)
        plt.figure(figsize=(10, 2))
        plt.plot(t,I)
        plt.xlabel('t(ms)')
        plt.ylabel('amplitude')
        plt.title(f'current = {self.amp}')
        plt.show()
        
    def plot_mnh(self):
        t = np.arange(0,100, 0.01)
        init_state = [self.v0, self.m0,self.h0,self.n0]  
        ans = odeint(lambda state,t: self.compute_derivatives(state,t), init_state,t)
        m,h,n = ans[:,1],ans[:,2],ans[:,3]
        plt.figure(figsize=(10, 2))
        plt.plot(t,m,label = 'm')
        plt.plot(t,n,label = 'n')
        plt.plot(t,h,label = 'h')
        plt.xlabel('t(ms)')
        plt.ylabel('gating value')
        plt.title('gating plot')
        plt.legend()
        plt.show()
        
    def plot_channel_current(self):
        t = np.arange(0,100, 0.01)
        init_state = [self.v0, self.m0,self.h0,self.n0] 
        ans = odeint(lambda state,t: self.compute_derivatives(state,t), init_state,t)
        v,m,h,n = ans[:,0],ans[:,1],ans[:,2],ans[:,3]
        ina = self.I_Na(v, m, h)
        ik = self.I_K(v, n)
        plt.figure(figsize=(10, 2))
        plt.plot(t,ina,label = 'I_Na')
        plt.plot(t,ik,label = 'I_K')
        plt.xlabel('t(ms)')
        plt.ylabel('channels current')
        plt.title('current plot')
        plt.legend()
        plt.show()
        
        
        
#1
model = HodgkinHuxley()
model.set_current('step',20,0,0.2)
model.plot_voltage()
print("minimum amplitude for excitation")
model.set_current('step',58.1,0,0.2)
model.plot_voltage()
print("5 different width for excitation")  
model.set_current('step',23.2,0,0.5)
model.plot_voltage()

model.set_current('step',11.6,0,1)
model.plot_voltage()

model.set_current('step',2,0,5)
model.plot_voltage()

model.set_current('step',0.9,0,10)
model.plot_voltage()

model.set_current('step',0.4,0,20)
model.plot_voltage()
#2
model.set_current('step',50,0,12)
model.plot_mnh()
model.plot_current()
#3
model.plot_channel_current()
#4
print("C=1")
model.plot_voltage(end = 60)
print("C=3")
model.set_capacitance(3)
model.plot_voltage(end = 60)
print("C=10")
model.set_capacitance(10)
model.plot_voltage(end = 60)
#5
model.set_capacitance(1)
model.set_current('custom',20,0,0.2)
model.plot_voltage()