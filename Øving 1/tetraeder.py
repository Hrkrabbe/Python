import math
def main():
    h = float(input("Angi høyden til tetraederet\n"));
    a = 3/math.sqrt(6) * h
    print ("Areal: {0:.2f} \nVolum: {1:.2f}".format(getSurface(a),getVolume(a)))
    
def getVolume(a):
    v = math.sqrt(2)/12*a**3
    return v
    
def getSurface(a):
    s = math.sqrt(3)*a**2
    return s

main()