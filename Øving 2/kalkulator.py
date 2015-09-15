def main():
    print("Type a number, followed by an operator, followed by another number.\nValid operators are: '+,-,*,/'. Example:'5*5'. \n'q' to quit")
    run = True;
    while(run):
        str = input("")
        
        try:
            if("q" in str):
                run = False
                break
                
            elif("*" in str):
                i = str.index("*")
                x = float(str[:i])
                y = float(str[(i+1):])
                print(multiply(x,y))
            
            elif("/" in str):
                i = str.index("/")
                x = float(str[:i])
                y = float(str[(i+1):])
                print(divide(x,y))
                
            elif("+" in str):
                i = str.index("+")
                x = float(str[:i])
                y = float(str[(i+1):])
                print(add(x,y))
                
            elif("-" in str):
                i = str.index("-")
                x = float(str[:i])
                y = float(str[(i+1):])
                print(subtract(x,y))
            
            else:
                print("Invalid syntax")
        except ValueError:
            print("Invalid syntax")
        except ZeroDivisionError:
            print("I'm sorry, Dave. I'm afraid I can't do that")
    
def add(x,y):
    return x+y
    
def multiply(x,y):
    return x*y
    
def divide(x,y):
    return x/y
    
def subtract(x,y):
    return x-y
    
main();