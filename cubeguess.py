import random
while(True):
    i = random.randrange(1,100)
    cube = i**3
    print ("What is the cuberoot of {0:,d}".format(cube))
    user_i = int(input())
    if (i==user_i):
        print("Correct!")
    elif(user_i == 0):
        break
    else:
        print("Incorrect! The correct answer is ",i)