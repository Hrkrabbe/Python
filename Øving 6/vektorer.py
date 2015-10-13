__author__ = 'Anders'
def main():
    vec1 = vectorIn()
    #vec2 = mulitplyScalar(2,vec1)
    vec2 = vectorIn()
    dot = multiplyDot(vec1,vec2)

    printvector("vec1",vec1)
    printvector("vec2",vec2)
    print("Dotprodukt: ",dot)

def vectorIn():
    inp = input("Skriv inn en vektor: ")
    vec = inp.split(",", inp.count(",") +1)
    for i,val in enumerate(vec):
        vec[i] = float(val)
    return vec

def printvector(name,vec):
    print("{0} = [{1:.2f},{2:.2f},{3:.2f}]".format(name, vec[0],vec[1],vec[2]))

def mulitplyScalar(scalar, vec):
    for i,n in enumerate(vec):
        vec[i] = n*scalar
    return vec

def multiplyDot(vec1,vec2):
    sum = 0
    for i in range(len(vec1)):
        sum+= vec1[i]*vec2[i]
    return sum

main()