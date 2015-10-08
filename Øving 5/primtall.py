import math
primes=[]
def main():
    loadPrimes()            #Oppretter liste med alle primtallene i filen primtall.txt
    print(isPrime(19997))   #Sjekker om det gitte tallet er et primtall
    #findPrimes(1000)       #Finner alle primtall opptil argumentet og lagrer i primtall.txt
    
def isPrime(a):
    for p in primes:
        if(p >= round(math.sqrt(a) + 0.5)):
            return True
        if(a%p == 0 and a!=p):
            print("Divisible by" , p)
            return False

    for i in range(primes[len(primes)-1], round(math.sqrt(a) + 0.5)):
        if(a%i == 0):
            print("Divisible by" , i)
            return False
    return True

def findPrimes(end):
    index = len(primes) -1
    for i in range(primes[index],end):
        isprime=True
        for p in primes:
            if(p >= round(math.sqrt(i) + 0.5)):
                break
            if(i%p == 0):
                isprime = False
        if(isprime):
            primes.append(i)
            print(i)
    savePrimes(index)

def loadPrimes():
    import os
    if(os.stat("primtall.txt").st_size == 0):
            primes.append(2)
            savePrimes(-1)
            return
    with open("primtall.txt") as f:
        for line in f:
            primes.append(int(line.strip()))

def savePrimes(index):
    with open("primtall.txt","a") as f:
        for i in range(index+1,len(primes)):
            f.write("{0}\n".format(primes[i]))
    print("Successfully saved to file")

main()