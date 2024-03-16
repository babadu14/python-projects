import random 

rps = ['rock', 'paper', 'scissors']
gamerunning = True
player_score = 0
computer_score = 0
winning_score = 3


def get_user_choice(rps):
    choice = input('choose either rock, paper or scissors: ').lower()
    while choice not in rps:
        choice = input('INVALID CHOICE, please choose one of rock, paper or scissors: ').lower()
    return choice


def get_computer_choice(rps):
    computer_choice = random.choice(rps)
    return computer_choice


def winner(user_choice, computer_choice):
    global player_score
    global computer_score
    if user_choice == 'rock' and computer_choice == 'scissors':
        print(f'you chose {user_choice}, computer chose {computer_choice}')
        player_score += 1
        print(f' you have: {player_score} points computer has: {computer_score} points')
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print(f'you chose {user_choice}, computer chose {computer_choice}')
        player_score += 1
        print(f' you have: {player_score} points computer has: {computer_score} points')
    elif user_choice == 'paper' and computer_choice == 'rock':
        print(f'you chose {user_choice}, computer chose {computer_choice}')
        player_score += 1
        print(f' you have: {player_score} points computer has: {computer_score} points')
    elif computer_choice == 'rock' and user_choice == 'scissors':
        print(f'you chose {user_choice}, computer chose {computer_choice}')
        computer_score += 1
        print(f' you have: {player_score} points computer has: {computer_score} points')
    elif computer_choice == 'scissors' and user_choice == 'paper':
        print(f'you chose {user_choice}, computer chose {computer_choice}')
        computer_score += 1
        print(f' you have: {player_score} points computer has: {computer_score} points')

    elif computer_choice == 'paper' and user_choice == 'rock':
        print(f'you chose {user_choice}, computer chose {computer_choice}')
        computer_score += 1
        print(f' you have: {player_score} points computer has: {computer_score} points')


def check_tie(user_choice, computer_choice):
    global player_score
    global computer_score
    if user_choice == computer_choice:
        print(f'you chose {user_choice}, computer chose {computer_choice}')
        print('its a tie')
        print(f' you have: {player_score} points computer has: {computer_score} points')

def game_winner():
    global gamerunning
    global winning_score
    if player_score == winning_score:
        print('GAME OVER\n congrats you won')
        gamerunning = False
    elif computer_score == winning_score:
        print('GAME OVER\n computer won')
        gamerunning = False


def play_again():
    global gamerunning
    global player_score
    global computer_score 
    if player_score == winning_score or computer_score == winning_score:
        play_again_input = input('Do you want to play again? ')
        if play_again_input == 'yes':
            player_score = 0
            computer_score = 0
            gamerunning = True
        else:
            gamerunning = False

while gamerunning:
    user_choice = get_user_choice(rps)
    computer_choice = get_computer_choice(rps)
    winner(user_choice, computer_choice)
    check_tie(user_choice, computer_choice)
    game_winner()
    play_again()

