def main():
    tol = 1/1000
    res = multiply(tol)
    print("Produkt: {0}\nIterasjoner: {1}\nToleranse: {2}".format(res[0],res[1],tol))
    
def multiply(tol):
    product = 1
    i = 1
    while(True):
        productold = product
        n = 1 + 1/i**2
        product *= n
        i+=1
        if((product - productold) < tol):
            break
    return product,i
main()