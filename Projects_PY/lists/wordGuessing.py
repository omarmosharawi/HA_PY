import random

name = input("What's your name? ")
print(f'Hi {name}, welcome to the name guessing game')

names = ['OMAR', 'MOHAMED', 'SHARAWI', 'ALI', 'MARIAM', 'ADEL', 'AHMED', 'ABDELRAHMAN', 'ZIAD', 'JANA']
word = random.choice(names)

print("the name is:")

guesses = ''
turns = 13

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The name is:", word)
        break

    guess = input("guess a character:")
    upGuess = guess.upper()
    guesses += upGuess

    if upGuess not in word:
        turns -= 1
        print("Wrong guess")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Lose")