__author__ = 'Anders'
import math
def main():
    F = integralSinX(0,math.pi,100)
    print(F)
    F = integralSinXTrapes(0,math.pi,100)
    print(F)
    F = integralSinXSimpsons(0,math.pi,100)
    print(F)

    F = integral(0,math.pi,100,math.sin)
    print(F)

    F = integral(0,1,100,f)
    print(F)

def sinX(x):
    return math.sin(x)

def exp(x):
    return math.exp(x)

def f(x):
    y = x**2
    return y

def integral(a,b,N,func):
    sum = 0
    h = (b-a)/N
    for i in range(N+1):
        sum += func(i*h+h/2+a)*h
    return sum

def integralSinX(a,b,N):
    sum = 0
    h = (b-a)/N
    for i in range(N+1):
        sum += math.sin(i*h+h/2+a)*h
    return sum

def integralSinXTrapes(a,b,N):
    sum = 0
    h = (b-a)/N
    for i in range(1,N+1):
        sum += (h/2)*(math.sin(h*i+a) + math.sin(h*(i-1)+a))
    return sum

def integralSinXSimpsons(a,b,N):
    sum = 0
    h = (b-a)/N
    for i in range(N+1):
        if(i==0 or i==N):
            sum+= (h/3)*math.sin(h*i+a)
        elif(i%2==0):
            sum+= 2*(h/3)*math.sin(h*i+a)
        else:
            sum+= 4*(h/3)*math.sin(h*i+a)
    return sum

main()