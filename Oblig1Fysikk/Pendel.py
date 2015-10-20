__author__ = 'Anders' #Copyright bithces
import math

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


