__author__ = 'Anders'
import timeit
import random
def main():
    listelengde = 200
    liste = [random.randint(0,listelengde) for i in range(listelengde)]
    liste1 = bubbleSort(liste[:])
    liste2 = selectionSort(liste[:])

    print("Usortert liste: ")
    print(liste)
    print()

    print("Liste sortert med bubblesort:")
    print(liste1)
    t = timeit.Timer(lambda: bubbleSort(liste[:]))
    print("Tid:",t.timeit(number=1))
    print()

    print("Liste sortert med selectionsort:")
    print(liste2)
    t = timeit.Timer(lambda: selectionSort(liste[:]))
    print("Tid:",t.timeit(number=1))

def bubbleSort(liste):
    sorted = False
    while(not sorted):
        sorted = True
        for i in range(len(liste)-1):
            if (liste[i] > liste[i+1]):
                liste[i], liste[i+1] = liste[i+1], liste[i]
                sorted = False
    return liste

def selectionSort(liste):
    for j in range(len(liste)):
        iMin = j
        for i in range(j, len(liste)):
            if(liste[i] < liste[iMin]):
                iMin = i
        if(iMin != j):
            liste[j], liste[iMin] = liste[iMin], liste[j]
    return liste

main()