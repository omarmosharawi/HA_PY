import random

l = ['OMAR', 'MOHAMED', 'SHARAWI', 'ALI', 'MARIAM', 'ADEL', 'AHMED', 'ABDELRAHMAN', 'ZIAD', 'JANA']
word = random.choice(l)
health = 5

name = input("What's your name? ")
print(f'Hi {name}, welcome to the name guessing game')
print("- Here's a list to help you guess: ")
print('\t', l)
print(f'- You have {health} attempts to solve')

while True:
    guess = input('\nEnter the guess name: ')
    upL = guess.upper()

    if upL == word:
        print(f'You won the correct name is {word}')
        break
    else:
        health -= 1
        print(f'Wrong guess, try again... | Remaining attempts = {health}')
        if health == 0:
            print(f'The attempts are over, the guess name is {word}')
            break