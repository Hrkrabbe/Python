def main():
    a=int(input("a= "))
    b=int(input("b= "))
    c=int(input("c= "))
    d = int((b**2-4*a*c))
    
    if(d==0):
        print("Ligningen {0}x*x + {1}x + {2} = 0 har én reell dobbeltrot.".format(a,b,c))
    elif(d<0):
        print("Ligningen {0}x*x + {1}x + {2} = 0 har to imaginære løsninger.".format(a,b,c))
    else:
        print("Ligningen {0}x*x + {1}x + {2} = 0 har to reelle løsninger.".format(a,b,c))
    
main()