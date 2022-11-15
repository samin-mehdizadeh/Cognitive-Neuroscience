#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pylab 
import scipy.integrate as integrate
from sympy import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt
    
def step(amp,t):
    return amp

def impulse(amp,t):
    if(t>=0 and t<=0.4):
        return amp
    else:
        return 0


class MorrisLecar:
    
    def __init__(self,current,amp):
        self.gl = 8
        self.El = -80
        self.gNa = 20
        self.Ena = 60
        self.gk = 10
        self.Ek = -90
        self.v12n = -25
        self.v12m = -20
        self.kn = 5
        self.km = 15
        self.Cm = 1
        self.current_func = current
        self.amp = amp
        
    def change_current(self,amp,current=step):
        self.current_func = current
        self.amp = amp
        
    def m_inf(self,v):
        return 1/(1+np.exp((self.v12m-v)/self.km))
                  
    def n_inf(self,v):
        return 1/(1+np.exp((self.v12n-v)/self.kn))
    
    def tau(self,v):
        return 1

    
    def dvdt(self,v,n,t):
        return (self.current_func(self.amp,t)-self.gl*(v-self.El)-self.gk*n*(v-self.Ek)-self.gNa*self.m_inf(v)*(v-self.Ena))/self.Cm
    
    def dndt(self,v,n):
        return (1/self.tau(v))*(self.n_inf(v)-n)
    
    def plot_voltage(self):
        v0 =-66
        n0 = 0
        t = np.arange(0.0, 100, 0.1)

        init_state = [v0, n0]  
        ans = odeint(lambda state,t: self.derivs(state,t), init_state,t)
        v = ans[:,0] 
        
        pylab.figure(figsize = (5,3))
        pylab.plot(t, v)
        pylab.xlabel('time(ms)')
        pylab.ylabel('v')
        pylab.title('voltage')
        pylab.show()   
  
    def derivs(self,state,t):
        v,n = state
        dvdt = self.dvdt(v,n,t)
        dndt = self.dndt(v,n)
        return dvdt,dndt

    
    def draw_system(self):
        v0 =-66
        n0 = 0
        t = np.arange(0, 100, 0.1)

        init_state = [v0, n0]  
        ans = odeint(lambda state,t: self.derivs(state,t), init_state,t)
        v = ans[:,0]  
        n = ans[:,1]  

        plt.figure(figsize=(6,6))
        plt.plot(v, n,'->')
        plt.xlabel('V')
        plt.ylabel('n')
        plt.title('phase plane')
        
        vmax = v.max()
        vmin =  v.min()
        nmax = n.max()
        nmin = n.min()
        V, N = np.meshgrid(np.linspace(vmin,vmax, num=15), np.linspace(nmin,nmax, num=15))
        dV = self.dvdt(V, N,t)
        dN = self.dndt(V, N)
        color_array = np.sqrt(((dV+2)/2)**2 + ((dN+2)/2)**2)
        plt.quiver(V, N, dV, dN,color=(1,1,1,1), alpha=0.8)
        plt.streamplot(V, N, dV, dN,color=(0,0,0,.2))
        
        fig, ax = plt.subplots(figsize=(6,4))
        
        ax.set_title('nullclines')
        
        V, N = np.meshgrid(np.linspace(-80,20, num=25), np.linspace(-0.5,1.25, num=25))
        dV = self.dvdt(V, N,t)
        dN = self.dndt(V, N)
        ax.streamplot(V, N, dV, dN,color=(0,0,0,.2))
        
        V, N = np.meshgrid(np.linspace(-80,20, num=100), np.linspace(-0.5,1.25, num=100))
        dV = self.dvdt(V, N,t)
        dN = self.dndt(V, N)
        NC1 = ax.contour(V, N, dV, levels=[0], linewidths=1, colors='red')
        ax.clabel(NC1, inline=1, fontsize=10)

        NC2 = ax.contour(V, N, dN, levels=[0], linewidths=1, colors='green')
        ax.clabel(NC2, inline=1, fontsize=10)

        lines = [ NC1.collections[0], NC2.collections[0]]
        labels = ['V-nullcline','n-nullcline']

        plt.legend(lines, labels)
        plt.show()
             
#1       
print("input current = 0")        
model = MorrisLecar(step,0)
model.draw_system()
#2
print("minimum amplitude for current leading the system to spike")
model.change_current(4.52)
model.plot_voltage()
print("below threshold(Ib=3)")
model.change_current(3)
model.plot_voltage()
print("above threshold(Ia=20)")
model.change_current(20)
model.plot_voltage()
#3
print("below threshold(Ib=3)")
model.change_current(3)
model.draw_system()
print("above threshold(Ia=20)")
model.change_current(20)
model.draw_system()
#4
model.change_current(27.1,impulse)
model.plot_voltage()
print("below threshold(Ib=15)")
model.change_current(15,impulse)
model.plot_voltage()
print("above threshold(Ia=35)")
model.change_current(35,impulse)
model.plot_voltage()