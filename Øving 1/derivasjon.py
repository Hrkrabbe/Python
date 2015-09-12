import math

def main():
    #h = 10**-3
    #x = math.pi
    
    x = float(input("Skriv inn ett flyttall"))
    h = float(input("Skriv inn ett flyttall til"))
    
    f1 = math.sin(x)
    f2 = math.sin(x + h)
    
    df = (f2 - f1) / h
    print("{0:.2f}".format(df))
    
main()
    
    