# simple app for storing birthdays and check by name

BD = {'omar': 'Jul 27, 2003', 'mariam': 'Oct 15, 2007', 'adel': 'Jun 15, 2009'}

while True:
    name = input('Enter a name: ')
    if name == '':
        print('You are clicked Enter button to exit...')
        break

    if name in BD:
        print(f'{BD[name]} is the birthday of {name}')
    else:
        print('name not exist')
        newBD = input('What is their birthday? ')
        BD[name] = newBD
        print('added!')