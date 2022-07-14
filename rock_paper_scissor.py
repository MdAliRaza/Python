""" Rock Paper Scissor Game Code """

import random 
choices = ['rock', 'paper', 'scissor']
computer = random.choice(choices)
player = None


def game():
    global player
    while player not in choices:
        player = input('choose yours.. ').lower()

        if player == computer:
            print('Player : ', player)
            print('Computer : ', computer)
            print('Tie')
        elif player == 'rock':
            if computer == 'paper':
                print('Player : ', player)
                print('Computer : ', computer)
                print('Computer wins')
            elif computer == 'scissors':
                print('Player : ', player)
                print('Computer : ', computer)
                print('Player Wins')
        elif player == 'scissors':
            if computer == 'rock':
                print('Player : ', player)
                print('Computer : ', computer)
                print('Computer Wins')
            elif computer == 'paper':
                print('Player : ', player)
                print('Computer : ', computer)
                print('Player Wins')
        elif player == 'paper':
            if computer == 'rock':
                print('Player : ', player)
                print('Computer : ', computer)
                print('Player Wins')
            elif computer == 'scissors':
                print('Player : ', player)
                print('Computer : ', computer)
                print('Computer Wins')


for i in range(3):
    game()
