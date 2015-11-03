#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

from matplotlib.pyplot import figure,title,xlabel,ylabel,plot,legend,hold,show, savefig, grid, ylim
import math

def main():
    v1,v2,v3 = 0.4,6.253,7
    
    pendel1 = Pendel(1,0,v1,4.02)
    pendel2 = Pendel(1,0,v2,10.75)
    pendel3 = Pendel(1,0,v3,2.7)
    
    pendel1.plotAngle("andersnt_FIGA")
    pendel2.plotAngle("andersnt_FIGB")
    pendel3.plotAngle("andersnt_FIGC")
    pendel2.plotEnergy("andersnt_FIGD")
    

class Pendel:
    def __init__(self,L,theta0,v0,TwoT):
        self.L = L
        self.theta0 = theta0
        self.v0 = v0
        self.g = 9.81
        self.delta_t = 0.0001
        self.TwoT = TwoT
        
        
    def thetaDegrees(self):
        thetas = []
        t = []
        v = self.v0
        theta = self.theta0
        thetas.append(theta)
        t.append(0)

        while(t[-1] <= self.TwoT):
            delta_theta = (v/self.L)*self.delta_t
            theta += delta_theta
            delta_v = -self.g*math.sin(theta) * self.delta_t
            v += delta_v
            thetas.append(math.degrees(theta))
            t.append(t[-1]+self.delta_t)
        return thetas,t
        
    def energy(self):
        e = []
        t = []
        v = self.v0
        theta = self.theta0
        t.append(0)
        e.append((1/2)*v**2 + self.g*self.L*(1 - math.cos(theta)))

        while(t[-1] <= self.TwoT):
            delta_theta = (v/self.L)*self.delta_t
            theta += delta_theta
            delta_v = -self.g*math.sin(theta) * self.delta_t
            v += delta_v
            e.append((1/2)*(v)**2 + self.g*self.L*(1 - math.cos(theta)))
            t.append(t[-1]+self.delta_t)
        return e,t
        
    def plotAngle(self,fName):
        thetaList,t = self.thetaDegrees()
        figure(fName)
        title(r'$v_0=$ ' + str(self.v0))
        xlabel(r'$t(s)$')
        ylabel(r'$\theta(grader)$')
        #hold(True)
        plot(t,thetaList)
        grid()
        show()
        savefig(fName+'.png')
        
    def plotEnergy(self,fName):
        e,t = self.energy()
        figure(fName)
        title(r'$v_0=$ ' + str(self.v0))
        xlabel(r'$t(s)$')
        ylabel(r'$e/m (m^2/s^2)$')
        ylim(15,25)
        #hold(True)
        plot(t,e)
        grid()
        show()
        savefig(fName+'.png')
main()