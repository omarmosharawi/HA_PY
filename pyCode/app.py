# guess number game

num = 5

while True:
    num_guess = input('Enter a number to guess: ')

    if num_guess == '':
        str(num_guess)
        print('please enter a number')
        exit()
    # elif num_guess == 'exit' or 'close':
    #     print('Thanks for using my app powered by Omar Mohamed.')
    #     exit()

    if float(num_guess) >= 0 :
        num_guess = float(num_guess)

        if num_guess == 4 or num_guess == 6 :
            print('you are so close')
        elif num_guess == 5:
            print('you won!')
            exit()
        else:
            print('too far')
    else:
        print('please enter a positive number')
