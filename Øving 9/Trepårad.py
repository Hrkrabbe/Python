__author__ = 'Anders'
def main():
    board = [[0 for i in range(3)]for j in range(3)]
    won = False
    player = 1
    printBoard(board)
    while(not won):
        board = move(board,player)
        printBoard(board)
        won,winner = checkWinner(board)
        if(won):
            if winner == 0:
                print("Uavgjort!")
            else:
                print("Spiller",player, "vant!")
        if player == 1:
            player = 2
        else:
            player = 1


def printBoard(board):
    symbols = [' ', 'O','X']
    print("   1 2 3")
    #print("---------")
    for l,i in enumerate(board):
        print(l+1,'|', end='')
        for j in i:
            print(symbols[j],"|",end='',sep='')
        print()
    print()

def checkWinner(board):
    for i in range(3):
        product = board[i][0] * board[i][1] * board[i][2]
        if product == 1:
            return True,1
        elif product == 2*3:
            return True,2

    for j in range(3):
        product = board[0][j] * board[1][j] * board[2][j]
        if product == 1:
            return True,1
        elif product == 2*3:
            return True,2

    product = 1
    for k in range(3):
        product*=board[k][k]
    if product == 1:
        return True,1
    elif product == 2*3:
        return True,2

    product = 1
    for k in range(2,-1,-1):
        product*=board[k][k]
    if product == 1:
        return True,1
    elif product == 2*3:
        return True,2

    product = 1
    for i in board:
        for j in i:
            product *=j
    if product != 0:
        return True,0

    return False,0

def move(board,player):
    while(True):
        try:
            inp = input("Spiller " + str(player) + " gjoer et trekk\n")
            cmd = inp.split()
            i,j = int(cmd[0])-1,int(cmd[1])-1
            #sjekk
            if(board[i][j] == 0):
                board[i][j] = player
                return board
            else:
                print("ugyldig trekk")
        except:
            print("Ugyldig input")

    return board
main()
