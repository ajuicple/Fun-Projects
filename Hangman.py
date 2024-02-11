#Github Username:
#Python Project: Hangman
#Description: Uses random and time to pick a secret word for you to guess.

import random
import time

#list of random words to be used in the game.
words = [
    'inspiration','fashion','person','decorative','goal','officer',
         'electronics','Separate','conversation', 'appeal', 'green',
         'dictate', 'experienced', 'crew', 'couple', 'continuation',
         'large', 'perforate', 'leave', 'campaign', 'stroll', 'murder',
         'decay', 'clay', 'option', 'classify', 'conscience', 'try',
         'transmission', 'draw', 'school','throne'
    ]

#Asking for player name. 
name = input('Hello, what is your name? ')
print('Hello {}, Time to play Hangman!'.format(name))
print('Start Guessing...')
time.sleep(0.5)

#picks random word from words
word = random.choice(words)
guesses = ''
turns = 6 #player has 6 turns

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end='')
        else:
            print('_', end='')
            failed += 1
    if failed == 0:
        print(' You Won!')
        break
    guess = input(' Guess a Character...')
    guesses += guess
    if guess not in word:
        turns -= 1
        print('Wrong :(')
        print('You have {} more guesses.'.format(turns))
        if turns == 0:
            print('You Lose :(')
            print(word)
