__author__ = 'Anders'
from Pendel import Pendel
from matplotlib.pyplot import rc,figure,title,xlabel,ylabel,plot,legend,hold,show
import math

def main():
    pendel1 = Pendel(1,0,-0.2)
    pendel2 = Pendel(1,0,8)
    t = 1
    print(pendel1.theta(t,100))
    print(pendel2.theta(t,100))

    theta1 = t*2
    figure('Theta')
    title('Vinkel')
    hold(True)
    plot(t,theta1,label="Theta")
    xlabel("x")
    ylabel("y")
    show()
    input()
main()