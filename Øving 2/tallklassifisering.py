def main():
    n = -4
    
    if(wholeNumber(n)):
        print("Dette er et heltall")
    else:
        print("Dette er ikke et heltall")
        
    if(evenNumber(n)):
        print("Dette er et partall")
    else:
        print("Dette er ikke et partall")
        
    if(positiveNumber(n)):
        print("Dette er et positivt tall")
    else:
        print("Dette er ikke et positivt tall")

def wholeNumber(n):
    return isinstance(n,int)
    
def evenNumber(n):
    return not(n % 2)
    
def positiveNumber(n):
    return (n>0)

main()