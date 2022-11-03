#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 23:32:52 2022

@author: mac
"""
import numpy as np
import matplotlib.pyplot as plt

class LIF:
    
    def __init__(self):
        self.vth = -55
        self.vreset = -75
        self.tau_m = 10
        self.gL = 10
        self.vinit = -75
        self.EL = -75
        self.tref = 2
        self.T = 400
        self.dt = 0.1
        self.time = np.arange(0,self.T+self.dt,self.dt)
        
    def set_tref(self,tref):
        self.tref = tref
        
    def dvdt(self,v,I):
        return (-(v-self.EL)+I/self.gL)/self.tau_m
        
    def simulate(self):
        spikes = []
        t_size = len(self.time)
        v = np.zeros(t_size)
        v[0] = self.vinit
        refactor_t = 0
        for t in range(t_size-1):
            if(refactor_t>0):
                v[t] = self.vreset
                refactor_t = refactor_t - 1
            elif(v[t]>= self.vth):
                spikes.append(t*self.dt)
                v[t] = self.vreset
                refactor_t = self.tref / self.dt 
            dv = self.dvdt(v[t],self.I[t])*self.dt
            v[t+1] = v[t]+dv
        
        return v,spikes
    
    def set_current(self,name,amp,freq=0):
        self.freq = freq
        self.amp = amp
        current = {'sin': self.sin_current,
                   'square': self.square_current,
                   'step': self.step_current}
        self.I = current[name](amp,freq)
        
    def square_current(self,amp,freq):
        t_size = len(self.time)
        I = np.array([amp]*t_size)
        I_duration = int(1000/freq)
        const = 0
        for i in range(0,t_size,I_duration):
            I[i:i+I_duration] = const*amp
            if(const == 0):
                const = 1
            else:
                const = 0
        return I
    
    def sin_current(self,amp,freq):
        return amp * np.sin(2 * np.pi * freq * self.time*0.001)
    
    def step_current(self,amp,freq=0):
        t_size = len(self.time)
        return np.array([amp]*t_size)
        
        
    def plot_voltage(self,t_start=0,t_end=100):
        start = int(t_start/self.dt)
        end = int(t_end/self.dt)
        t = self.time[start:end]
        v,spikes = self.simulate()
        v = v[start:end]
        print(f'number of spikes: {len(spikes)}')
        I = self.I[start:end]
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 2))
        axes[0].plot(t,v)
        axes[0].plot(t,[self.vth]*len(t))
        axes[0].set_xlabel('time(ms)')
        axes[0].set_ylabel('v')
        axes[0].set_title('voltage')
        axes[1].plot(t,I)
        axes[1].set_xlabel('time(ms)')
        axes[1].set_ylabel('I')
        axes[1].set_title(f'current = {self.freq}hz,amp = {self.amp}uA')
        plt.show()
        
    def plot_fI_curve(self):
        amps = np.arange(0,1000,10)
        fire_freq = np.zeros(len(amps))
        for i,amp in enumerate(amps):
            self.set_current('step', amp)
            v,spikes = self.simulate()
            if(len(spikes)>1):
                fire_freq[i] = 1000/(spikes[1]-spikes[0])
        plt.figure(figsize=(10, 2))
        plt.plot(amps,fire_freq)
        plt.xlabel('I')
        plt.ylabel('f')
        plt.title('f-I curve')
        plt.show()
    
#1        
model = LIF()
model.set_current('sin',100,10)
model.plot_voltage(0,200)
model.set_current('sin',100,200)
model.plot_voltage(0,200)
model.set_current('sin',100,1000)
model.plot_voltage(0,200)
#3
model.set_current('sin',231,10)
model.plot_voltage(0,200)
model.set_current('sin',250,10)
model.plot_voltage(0,200)
model.set_current('sin',350,10)
model.plot_voltage(0,200) 
model.set_current('sin',231,100)
model.plot_voltage(0,200)
model.set_current('step',200)
model.plot_voltage(0,200) 
model.set_current('step',201)
model.plot_voltage(0,200) 
model.set_current('step',250)
model.plot_voltage(0,200) 
#4
model.set_tref(3)
model.plot_fI_curve()
  
                            
                
            
        
        
        
        
        