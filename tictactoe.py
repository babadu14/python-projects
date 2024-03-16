board = ['-','-','-',
         '-','-','-',
         '-','-','-']

currentplayer = 'X'
gamerunning = True
winner = None

def printboard(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')

def switchplayer():
    global currentplayer
    if currentplayer == 'X':
        currentplayer = 'O'
    elif currentplayer == 'O':
        currentplayer = 'X'

def user_input(board):
    global currentplayer
    user_input = int(input('Enter a number from 0-8 -> '))
    if user_input >= 0 and user_input <= 8 and board[user_input] == '-':
        board[user_input] = currentplayer
        switchplayer()
        pass

def check_horizont(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True

def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True
    

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner= board[2]
        return True
    
def check_win():
    global gamerunning
    global winner
    if check_diagonal(board) or check_horizont(board) or check_vertical(board):
        printboard(board)
        gamerunning = False
        print('congrats', winner, 'you won ')

def check_tie(board):
    global gamerunning
    if '-' not in board:
        printboard(board)
        gamerunning = False
        print('its a tie')


while gamerunning:
    printboard(board)
    user_input(board)
    check_win()
    check_tie(board)