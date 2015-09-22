debug = True
def main():
    x = 6
    y = 7
    mult(x,y)
    
def mult(x,y):
    if(debug):
        print("Tallene som multipliseres er" , x, "og",y,)
    print(x*y)
    
main()