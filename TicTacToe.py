import random
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm\n\n')


def OpenScreen():
    print('***********************')
    print("Welcome to Tic Tac Toe!")
    print('***********************')
    print("Below you can see the game board's arrangement")
    print('1' + '|' + '2' + '|' + '3')

    print('4' + '|' + '5' + '|' + '6')

    print('7' + '|' + '8' + '|' + '9')


def DisplayBoard(b):
    print(b[1] + '|' + b[2] + '|' + b[3])

    print(b[4] + '|' + b[5] + '|' + b[6])

    print(b[7] + '|' + b[8] + '|' + b[9])


def PlayerSelection():
    print("Now, please choose 'X' or 'O' (make sure you've entered a valid choice)")

    select = input("Select 'X' or 'O': ")

    while select != 'X' and select != 'O':
        select = input("Select only 'x' or 'o': ")
    print("You are - ", select)
    computer = 'O' if select == 'X' else 'X'

    return select, computer


def PlayerMove(board, playerSymbol):
    flag = 1
    print("Please select a position on the board:")
    while flag:
        try:
            position = int(input(""))
            while board[position] != ' ':
                position = int(input("please choose an available position: "))
            flag = 0
        except IndexError:
            print("INDEX ERROR: index is out of range, enter a valid position")
        except ValueError:
            print("VALUE ERROR: enter only numbers (1-9)")


    board[position] = playerSymbol
    return board


def CheckRow(board, player, computer):
    temp = []
    for index in range(1, 8, 3):
        temp = board[index:index + 3]
        if temp.count(player) == 3:
            print("Congratulations! You win!")
            return 'end'
        elif temp.count(computer) == 3:
            print("Sorry, You lose...")
            return 'end'


def CheckColumn(board, player, computer):
    for index in range(1, 4):
        if board[index] == player and board[index + 3] == player and board[index + 6] == player:
            print("Congratulations! You win!")
            return 'end'
        if board[index] == computer and board[index + 3] == computer and board[index + 6] == computer:
            print("Sorry, You lose...")
            return 'end'


def CheckDiagonal(board, player, computer):
    if board[5] == player and board[1] == player and board[9] == player:
        print("Congratulations! You win!")
        return 'end'
    elif board[5] == player and board[3] == player and board[7] == player:
        print("Congratulations! You win!")
        return 'end'
    if board[5] == computer and board[1] == computer and board[9] == computer:
        print("Sorry, You lose...")
        return 'end'
    if board[5] == computer and board[3] == computer and board[7] == computer:
        print("Sorry, You lose...")
        return 'end'


def CheckForWinner(b, p, c):
    if CheckRow(b, p, c) == 'end':
        return 'end'
    elif CheckColumn(b, p, c) == 'end':
        return 'end'
    elif CheckDiagonal(b, p, c) == 'end':
        return 'end'
    elif ' ' not in b:
        print("It's a tie")
        return 'end'
    else:
        return 'continue'


def ComputerMove(b, p, c):
    Strategy(b, p, c)
    return b


def RollTheDice():
    print("Let's roll the dice...")
    print(".....")
    time.sleep(2)
    start = random.randint(0, 1)
    print("You start") if start == 0 else print("Computer starts")

    return start


def RunGame(board, start, player, computer):
    if start == 0:
        b = PlayerMove(board, player)
        DisplayBoard(b)
        print("\n")
        while True:
            ComputerMove(b, player, computer)
            DisplayBoard(b)
            if CheckForWinner(b, player, computer) == 'end':
                break
            print("\n")
            PlayerMove(b, player)
            if CheckForWinner(b, player, computer) == 'end':
                break
            DisplayBoard(b)
            print("\n")
    else:
        b = ComputerMove(board, player, computer)
        time.sleep(1)
        DisplayBoard(b)
        while True:
            PlayerMove(b, player)
            DisplayBoard(b)
            if CheckForWinner(b, player, computer) == 'end':
                break
            print("\n")
            ComputerMove(b, player, computer)
            DisplayBoard(b)
            if CheckForWinner(b, player, computer) == 'end':
                break
            print("\n")


def WinningRowCheck(board, computer):
    ROW_LENGTH, fill = 3, -1
    for j in range(1, ROW_LENGTH * (ROW_LENGTH - 1) + 2, ROW_LENGTH):
        temp = board[j:ROW_LENGTH + j]
        if temp.count(computer) == ROW_LENGTH - 1 and ' ' in temp:
            fill = temp.index(' ')
            board[fill + j] = computer
            return 1
    return 0


def WinningColumnCheck(board, computer):
    COLUMN_LENGTH, d = 3, {}
    for i in range(1, COLUMN_LENGTH + 1):
        for j in range(1, COLUMN_LENGTH * COLUMN_LENGTH + 1, COLUMN_LENGTH):
            d[j + i - 1] = board[j + i - 1]
        if sum(v == computer for v in d.values()) == COLUMN_LENGTH - 1 and sum(v == ' ' for v in d.values()) == 1:
            keys = list(d.keys())
            values = list(d.values())
            position = values.index(' ')
            board[keys[position]] = computer
            return 1
        d = {}
    return 0


def WinningDiagonalCheck(board, computer):
    DIAGONAL_LENGTH, d = 3, {}
    for i in range(1, DIAGONAL_LENGTH * DIAGONAL_LENGTH + 1, DIAGONAL_LENGTH + 1):
        d[i] = board[i]
    if sum(v == computer for v in d.values()) == DIAGONAL_LENGTH - 1 and sum(v == ' ' for v in d.values()) == 1:
        keys = list(d.keys())
        values = list(d.values())
        position = values.index(' ')
        board[keys[position]] = computer
        return 1
    d = {}
    for i in range(DIAGONAL_LENGTH, DIAGONAL_LENGTH * DIAGONAL_LENGTH - 1, DIAGONAL_LENGTH - 1):
        d[i] = board[i]
    if sum(v == computer for v in d.values()) == DIAGONAL_LENGTH - 1 and sum(v == ' ' for v in d.values()) == 1:
        keys = list(d.keys())
        values = list(d.values())
        position = values.index(' ')
        board[keys[position]] = computer
        return 1
    return 0


def WinningStrategy(board, computer):
    if WinningRowCheck(board, computer) == 0:
        if WinningColumnCheck(board, computer) == 0:
            if WinningDiagonalCheck(board, computer) == 0:
                return 0
    return 1


def AvoidLosingStrategy(board, player, computer):
    if board[5] != ' ' and computer not in board:
        r = random.randrange(1, 10, 2)
        while r == 5:
            r = random.randrange(1, 10, 2)
        if board[r] == ' ':
            board[r] = computer
            return board

    if board[1] == ' ' and player == board[2] and player == board[3] or board[1] == ' ' and player == board[4] and player == board[7] or board[1] == ' ' and player == board[5] and player == board[9]:
        board[1] = computer
        return board
    if board[3] == ' ' and player == board[2] and player == board[1] or board[3] == ' ' and player == board[6] and player == board[9] or board[3] == ' ' and player == board[5] and player == board[7]:
        board[3] = computer
        return board
    if board[7] == ' ' and player == board[8] and player == board[9] or board[7] == ' ' and player == board[4] and player == board[1] or board[7] == ' ' and player == board[5] and player == board[3]:
        board[7] = computer
        return board
    if board[9] == ' ' and player == board[6] and player == board[3] or board[9] == ' ' and player == board[8] and player == board[7] or board[9] == ' ' and player == board[5] and player == board[1]:
        board[9] = computer
        return board
    if board[2] == ' ' and player == board[1] and player == board[3] or board[2] == ' ' and player == board[5] and player == board[8]:
        board[2] = computer
        return board
    if board[4] == ' ' and player == board[5] and player == board[6] or board[4] == ' ' and player == board[1] and player == board[7]:
        board[4] = computer
        return board
    if board[6] == ' ' and player == board[3] and player == board[9] or board[6] == ' ' and player == board[5] and player == board[4]:
        board[6] = computer
        return board
    if board[8] == ' ' and player == board[5] and player == board[2] or board[8] == ' ' and player == board[7] and player == board[9]:
        board[8] = computer
        return board
    if board[5] == ' ' and player == board[1] and player == board[9] or board[5] == ' ' and player == board[3] and player == board[7]:
        board[5] = computer
        return board
    if board[5] == ' ' and player == board[2] and player == board[8] or board[5] == ' ' and player == board[4] and player == board[6]:
        board[5] = computer
        return board
    return 0


def Strategy(board, player, computer):
    b = WinningStrategy(board, computer)
    if b == 0:
        b = AvoidLosingStrategy(board, player, computer)
        if b == 0:
            if board[5] == ' ':
                board[5] = computer
                return board
            else:
                r = random.randint(1, 9)
                while board[r] != ' ':
                    r = random.randint(1, 9)
                board[r] = computer
                return board
    return b


def CreateBoard():
    board = ['@', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    return board


OpenScreen()
p, c = PlayerSelection()
start = RollTheDice()
b = CreateBoard()
RunGame(b, start, p, c)