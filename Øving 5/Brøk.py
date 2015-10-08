def main():
    a = int(input("Teller:"))
    b= int(input("Nevner:"))
    print("Forkortet brøk: {0}/{1}".format(reduce_fraction(a,b)[0],reduce_fraction(a,b)[1]))
    
def gcd(a,b):
    while(b!=0):
        oldb = b
        b = a%b
        a = oldb
    return a
    
def reduce_fraction(a,b):
    cd = gcd(a,b)
    return int(a/cd),int(b/cd)
    
main()