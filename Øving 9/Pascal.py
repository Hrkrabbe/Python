__author__ = 'Anders'
def main():
    trekant = pascalsTrekant(7)
    for i,line in enumerate(trekant):
        print('  ' * int((len(trekant) -i+1)) , line)

    print()
    printPolynom(3)

def pascalsTrekant(n):
    trekant = []
    trekant.append([1])

    for i in range(1,n):
        trekant.append([])
        for j in range(i+1):
            if j == 0:
                trekant[i].append(1)
            elif j == i:
                trekant[i].append(1)
            else:
                trekant[i].append(trekant[i-1][j-1]+trekant[i-1][j])
    return trekant

def printPolynom(n):
    co = pascalsTrekant(n+1)[n]
    for i,num in enumerate(co):
        print("{2}X^{0}Y^{1}".format((n - i),i,num),end=' ')

main()




