__author__ = 'Anders'
import random
def main():
    stang = [1,2,3,4]
    print(masseSenter(stang))
    genererStang(15)

def masseSenter(liste):
    M = sum(m for m in liste)
    R = 0
    for i,m in enumerate(liste):
        r = i + 0.5
        R += m*r
    return R/M

def genererStang(lengde):
    stang = [random.randint(1,10) for i in range(lengde)]
    printStang(stang)

def printStang(liste):
    print("Stang:" , liste , "\nMassesenter:",masseSenter(liste))
main()