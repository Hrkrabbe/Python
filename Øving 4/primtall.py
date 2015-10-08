primes=[2]
def main():
    findprimes()
    
#def isprime(a):

def findprimes():
    for i in range(3,50000):
        isprime=True
        for p in primes:
            if(i%p == 0):
                isprime = False
        if(isprime):
            primes.append(i)
            print(i)
           
main()