__author__ = 'Anders'
def main():
    familie = {}
    while(True):
        inp = input("Legg til et familiemedlem. F.eks 'bestefar' 'suttorm')")
        if inp == '':
            break
        entry = inp.split()
        key = entry[0]
        navn = entry[1]

        if key not in familie:
            familie[key] = [navn]
        else:
            familie[key].append(navn)
    print(familie)
main()