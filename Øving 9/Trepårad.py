__author__ = 'Anders'
def main():
    board = [[0 for i in range(3)]for j in range(3)]
    printBoard(board)

def printBoard(board):
    print("   1 2 3")
    #print("---------")
    for l,i in enumerate(board):
        print(l+1,'|', end='')
        for j in i:
            print(j,"|",end='',sep='')
        print()

def checkWinner(board):
    for i in board:
        product = board[i][0] * board[i][1] * board[i][2]
    if product == 1:
        return True,0
    elif product == 2*3:
        return True,1

    for j in range(3):
        product = board[0][j] * board[1][j] * board[2][j]
    if product == 1:
        return True,0
    elif product == 2*3:
        return True,1

    product = 1
    for k in range(3):
        product*=board[k][k]
    if product == 1:
        return True,0
    elif product == 2*3:
        return True,1

main()
