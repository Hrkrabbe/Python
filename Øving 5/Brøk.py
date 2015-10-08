def main():
    a = int(input("Teller:"))
    b= int(input("Nevner:"))
    res=reduce_fraction(a,b)
    print("Forkortet brøk: {0}/{1}".format(res[0],res[1]))
    
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