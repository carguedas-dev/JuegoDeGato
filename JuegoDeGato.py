def DisplayBoard(board):
    for i in range(3):
        print("+-------" * 3 + "+")
        print(("|" + " " * 7) * 4)
        print(("|" + " " * 2), board[i][0], " " * 2 + "|" + " " * 2, board[i][1], " " * 2 + "|" + " " * 2, board[i][2], " " * 2 + "|")
        print(("|" + " " * 7) * 4)

    print("+-------" * 3 + "+")
def EnterMove(board):

    Move = int(input("Enter your move: "))
    while not 0 < Move <= 10:
        print("Number not within 1-10 range.")
        Move = int(input("Please retype:"))

    Rollback = 0
    while Rollback == 0:
        counter = 0
        for i in board:
            if Move in i:
                continue
            else:
                counter += 1
        if counter == 3:
            print("The value you've entered is either taken or not valid. Please try again!")
            Move = int(input("Enter your move: "))
            Rollback = 0
        else:
            Rollback = 1

    for i in range(0, len(board)):
        counter = 0
        for a in board[i]:
            if a == Move:
                board[i][counter] = "O"
                break
            else:
                counter += 1
def VictoryFor(board, sign):

    global usedspaces
    if (board[0][0] == board[0][1] == board[0][2] == sign) or (board[1][0] == board[1][1] == board[1][2] == sign) or (board[2][0] == board[2][1] == board[2][2] == sign) or \
            (board[0][0] == board[1][0] == board[2][0] == sign) or (board[0][1] == board[1][1] == board[2][1] == sign) or (board[0][2] == board[1][2] == board[2][2] == sign) or \
                (board[0][0] == board[1][1] == board[2][2] == sign) or (board[0][2] == board[1][1] == board[2][0] == sign):
        return True
    else:
        usedspaces = 0
        for i in range(len(board)):
            for a in board[i]:
                if a not in [1,2,3,4,5,6,7,8,9]:
                    usedspaces += 1
                else:
                    continue
        if usedspaces == 9:
            return usedspaces
        else:
            pass
def DrawMove(board):
    from random import randrange

    computer = randrange(1,10)

    Rollback = 0
    while Rollback == 0:
        counter = 0
        for i in board:
            if computer in i:
                continue
            else:
                counter += 1
        if counter == 3:
            computer = randrange(1,10)
            Rollback = 0
        else:
            Rollback = 1

    for i in range(0, len(board)):
        counter = 0
        for a in board[i]:
            if a == computer:
                board[i][counter] = "X"
                break
            else:
                counter += 1
board = [[1,2,3],[4,5,6],[7,8,9]]
GameWon = False

print("Welcome to TicTacToe, the computer will make the first move. Then you'll be prompted to enter your move:")
DrawMove(board)
DisplayBoard(board)
while GameWon==False:
    for i in range(2,99999):
        if i == 2:
            EnterMove(board)
            DisplayBoard(board)
        else:
            if i%2 != 0:
                DrawMove(board)
                GameWon = VictoryFor(board, "X")
                if GameWon == True:
                    print('Congratulations! "X" Wins!')
                    DisplayBoard(board)
                    break
                elif GameWon == 9:
                    print("Sorry! It seems we have a tie! Better luck next time!")
                    DisplayBoard(board)
                    GameWon = True
                    break
                else:
                    continue
            else:
                DisplayBoard(board)
                EnterMove(board)
                GameWon = VictoryFor(board, "O")
                if GameWon == True:
                    print('Congratulations! "O" Wins!')
                    DisplayBoard(board)
                    break
                elif GameWon == 9:
                    print("Sorry! It seems we have a tie! Better luck next time!")
                    DisplayBoard(board)
                    GameWon = True
                    break
                else:
                    DisplayBoard(board)
                    continue





