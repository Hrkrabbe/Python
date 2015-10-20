__author__ = 'Anders'
def main():
    filename = 'numbers.txt'
    print("Antall linjer:",file_len(filename))
    numberCount(filename)

def file_len(filename):
    with open(filename) as file:
        return sum(1 for line in file)

def numberCount(filename):
    numbers = [0]*10
    with open(filename) as file:
        for line in file:
            rad = line.split()
            for n in rad:
                numbers[int(n)] += 1

    for i,n in enumerate(numbers):
        if(n != 0):
            print(i, ':', n)

main()