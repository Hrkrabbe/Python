__author__ = 'Anders'
import random
def main():
    numbers = []
    for n in range(1,35):
        numbers.append(n)
    myGuess = [4,8,15,16,23,32]

    winningNumbers = drawNumbers(numbers,10)
    mainHits = compList(winningNumbers[:len(winningNumbers)-3],myGuess)
    extraHits = compList(winningNumbers[len(winningNumbers)-3:],myGuess)
    prize=calculatePrize(winningNumbers,3,myGuess)

    print("Vinnertall: ",winningNumbers)
    print("Antall rette: ", mainHits, "+", extraHits)
    print("Premie: ",prize)

def drawNumbers(numbers,n):
    drawnNumbers = []
    for x in range(n):
        i = random.randint(0,len(numbers)-1-x)
        drawnNumbers.append(numbers.pop(i))
    return drawnNumbers

def compList(list1, list2):
    hits = 0
    for n in list1:
        if n in list2:
            hits += 1
    return hits

def calculatePrize(winningNumbers,noExtra, guess):
    mainHits = compList(winningNumbers[:len(winningNumbers)-noExtra],guess)
    extraHits = compList(winningNumbers[len(winningNumbers)-noExtra:],guess)
    if(mainHits>=4):
        if(mainHits == 7):
            return 2749455
        elif(mainHits == 6 and extraHits >= 1):
            return 102110
        elif(mainHits == 6):
            return 3385
        elif(mainHits == 5):
            return 95
        elif(extraHits >= 1):
            return 45
    return 0

main()