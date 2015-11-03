__author__ = 'Anders'
__author__ = 'Anders'
def main():
    filename = 'numbers.txt'
    print("Antall linjer:",file_len(filename))
    numberCount(filename)

def file_len(filename):
    with open(filename) as file:
        return sum(1 for line in file)

def numberCount(filename):
    numbers = {}
    with open(filename) as file:
        for line in file:
            rad = line.split()
            for n in rad:
                if(n not in numbers):
                    numbers[n] = 1
                else:
                    numbers[n] += 1

    print(numbers)

main()