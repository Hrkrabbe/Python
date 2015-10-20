#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

from numpy import log,linspace
from matplotlib.pyplot import rc,figure,title,xlabel,ylabel,plot,legend,hold,show
import math

def main():
    v1,v2,v3 = 0.4,6.25,7
    
    pendel1 = Pendel(1,0,v1)
    pendel2 = Pendel(1,0,v2)
    pendel3 = Pendel(1,0,v3)
    
    tf =6
    N = 10000
    t = linspace(0,tf,N)
    
    plotAngle(pendel1,t,tf,N,"Pendel 1")
    plotAngle(pendel2,t,tf,N,"Pendel 2")
    plotAngle(pendel3,t,tf,N,"Pendel 3")
    
    show()
    
def plotAngle(pendel,t,tf,N,fName):
    thetaList = pendel.thetaListDegrees(tf,N)
    figure(fName)
    title('v0= ' + str(pendel.v0))
    hold(True)
    plot(t,thetaList)
    show()

class Pendel:
    def __init__(self,L,theta0,v0):
        self.L = L
        self.theta0 = theta0
        self.v0 = v0
        self.g = 9.81

    def theta(self,t,N):
        delta_t = t/N
        v = self.v0
        theta = self.theta0

        for n in range(N):
            delta_v = -self.g*math.sin(theta) * delta_t
            delta_theta = (v/self.L)*delta_t
            v += delta_v
            theta += delta_theta
        return theta
        
    def thetaListDegrees(self,t,N):
        thetas = []
        delta_t = t/N
        v = self.v0
        theta = self.theta0

        for n in range(N):
            delta_v = -self.g*math.sin(theta) * delta_t
            delta_theta = (v/self.L)*delta_t
            v += delta_v
            theta += delta_theta
            thetas.append(math.degrees(theta))
        return thetas
main()