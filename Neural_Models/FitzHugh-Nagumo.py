#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 03:25:05 2022

@author: mac
"""
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

class BVP:

    
    def compute_derivatives(self,init_state, t):
        v,w = init_state
        dvdt = self.dvdt(v,w,t)
        dwdt = self.dwdt(v,w)
        return dvdt, dwdt
    
    def dvdt(self,v,w,t):
        return  v - v**3/3 - w +self.I(t)
    
    def dwdt(self,v,w):
        return 0.08*(v+0.7-0.8*w)
    
    
    def step_current(self,t):
        return self.amp
    
    def impulse_current(self,t):
        if(t<10):
            return self.amp
        else:
            return 0
    
    def set_current(self,amp,name='step'):
        current = {'step': self.step_current,
                   'impulse': self.impulse_current}
        self.amp = amp
        self.I = np.vectorize(current[name])
    
    def plot_nullcline(self):
        t = np.arange(0, 100, 0.1)
        fig, ax = plt.subplots(figsize=(6,4))
        
        ax.set_title(f'nullclines I={self.amp}')
        ax.set_xlabel('v')
        ax.set_ylabel('w')
        
        t = np.linspace(0, 100,30)
        V, W = np.meshgrid(np.linspace(-2.5,2.5, num=30), np.linspace(-2.5,2.5, num=30))
        dV = self.dvdt(V, W,t)
        dW = self.dwdt(V, W)
        ax.streamplot(V, W, dV, dW,color=(0,0,0,.2))
        
        
        t = np.linspace(0, 100,100)
        V, W = np.meshgrid(np.linspace(-2.5,2.5, num=100), np.linspace(-2.5,2.5, num=100))
        dV = self.dvdt(V, W,t)
        dW = self.dwdt(V, W)
        NC1 = ax.contour(V, W, dV, levels=[0], linewidths=1, colors='red')
        ax.clabel(NC1, inline=1, fontsize=10)

        NC2 = ax.contour(V, W, dW, levels=[0], linewidths=1, colors='green')
        ax.clabel(NC2, inline=1, fontsize=10)

        lines = [ NC1.collections[0], NC2.collections[0]]
        labels = ['V-nullcline','n-nullcline']
        plt.legend(lines, labels)
        plt.show()
        
    def plot_trajectory(self,v0,w0):
        t = np.linspace(0,100, num=100)
        ans = odeint(lambda state,t: self.compute_derivatives(state,t), [v0,w0],t)
        v = ans[:,0]  
        w = ans[:,1]  

        fig, ax = plt.subplots(figsize=(6,4))
        V, W = np.meshgrid(np.linspace(-2.5,2.5, num=100), np.linspace(-2.5,2.5, num=100))
        dV = self.dvdt(V, W,t)
        dW = self.dwdt(V, W)
        ax.streamplot(V, W, dV, dW,color=(0,0,0,.2))
        ax.plot(v, w,'->')
        ax.set_xlabel('v')
        ax.set_ylabel('w')
        ax.set_title(f'trajectory plot,I={self.amp}')
        
        NC1 = ax.contour(V, W, dV, levels=[0], linewidths=1, colors='red')
        ax.clabel(NC1, inline=1, fontsize=10)

        NC2 = ax.contour(V, W, dW, levels=[0], linewidths=1, colors='green')
        ax.clabel(NC2, inline=1, fontsize=10)

        lines = [ NC1.collections[0], NC2.collections[0]]
        labels = ['V-nullcline','n-nullcline']
        plt.legend(lines, labels)
        
    def plot_volatege(self,v0,w0):
        t = np.arange(0, 100, 0.1)
        init_state = [v0, w0]  
        ans = odeint(lambda state,t: self.compute_derivatives(state,t), init_state,t)
        v = ans[:,0]  
        w = ans[:,1]  

        plt.figure(figsize=(6,6))
        plt.plot(t, v,'->')
        plt.xlabel('V')
        plt.ylabel('t')
        plt.title('voltage')
        
#1       
model = BVP()
model.set_current(0)
model.plot_nullcline()
model.set_current(1.5)
model.plot_nullcline()  
#2
model.set_current(0)
model.plot_trajectory(-1.5,0) 
model.set_current(1.5)
model.plot_trajectory(-1.5,0) 
model.set_current(0)
model.plot_trajectory(-2,-1)
model.set_current(1.5)
model.plot_trajectory(-2,-1)
model.set_current(0)
model.plot_trajectory(-2,2)
model.set_current(1.5)
model.plot_trajectory(-2,2)

