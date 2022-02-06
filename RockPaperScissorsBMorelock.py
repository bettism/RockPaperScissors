# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 22:01:16 2022

@author: betti
"""
#Rock, Paper, Scissors Program
#Bettis Morelock
#1/28/2022

import random

while True:
   
    userAction = input('Make a choice. Rock, paper, or scissors?')
    possibleActions = ['rock', 'paper', 'scissors']
    computerAction = random.choice(possibleActions)
    
    print('\nYou chose {}. Computer chose {}.\n' .format(userAction, computerAction))
    
    if userAction == computerAction:
        print("Both players selected {}. It's a tie.".format(userAction))
    elif userAction == "rock":
        if computerAction == 'scissors':
            print('Rock smashes scissors! You win!')
        else:
            print('Paper covers rock! You lose.')
    elif userAction == 'paper':
        if computerAction == 'rock':
            print('Paper covers rock! You win.')
        else:
            print('Scissors cuts paper! You lose.')
    elif userAction == 'scissors':
        if computerAction == 'paper':
            print('Scissors cuts paper! You win!')
        else:
            print('Rock smashes scissors! You lose.')
            
    playAgain = input('Play again? (y/n):')
    if playAgain.lower() != 'y':
        break
