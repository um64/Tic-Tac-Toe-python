# milestone tic tac toe
#from numpy import array


def pick():
    inp = input("Player 1 select either X or O: ")
    if inp == 'X' or inp == 'O':
        if inp == "X":
            return True
        else:
            return False
    else:
        print("Wrong choice! Try again")
        pick()


def player_input():
    ans = int(input("Enter you choice between 1-9: "))
    if ans in range(1, 10):
        return ans
    else:
        print("Wrong choice, please try again")
        player_input()


def replay():
    i = input("Do you want to play again?(Answer with Y/N):")
    if i == 'Y' or i == 'y':
        return True
    elif i == 'N' or i == 'n':
        return False
    else:
        print("Wrong choice")
        replay()


def display(board):
    print(board[7],(" "),board[8],(" "),board[9])
    print("---------")
    print(board[4],(" "),board[5],(" "),board[6])
    print("---------")
    print(board[1],(" "),board[2],(" "),board[3])


def place_marker(board, marker, position):
    if board[position] == ' ':
        # board.insert(position,marker)
        board[position] = marker
        return True
    else:
        print("This spot is already taken")
        return False


def win_check(board):
    # row
    for i in range(1, 8, 3):
        if (board[i] == board[i + 1] and board[i + 1] == board[i + 2]):
            if board[i] != ' ':
                print("Game over!", board[i], "won the game")
                return True

    # column
    for i in range(1, 4, 1):
        if (board[i] == board[i + 3] and board[i + 3] == board[i + 6]):
            if board[i] != ' ':
                print("Game over!", board[i], "won the game")
                return True

    # diagonal 1
    if (board[1] == board[5] and board[5] == board[9]):
        if board[1] != ' ':
            print("Game over!", board[i], "won the game")
            return True

    # diagonal 2
    if (board[3] == board[5] and board[5] == board[7]):
        if board[3] != ' ':
            print("Game over!", board[i], "won the game")
            return True

    return False


print("Welcomne to tic tac toe")
board1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display(board1)
game = True
while game == True:
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    while win_check(board) == False:
        place_marker(board, 'X', player_input())
        display(board)
        if win_check(board) == True:
            break
        else:
            place_marker(board, 'O', player_input())
            display(board)
            continue

    if replay() == False:
        game = False
        break
    else:
        continue
    continue




















