# age calculator

while True:
    name = str(input('\nEnter your name: '))
    if name == 'stop': break

    age = int(input('Enter your birthday year: '))

    current_year = 2024
    current_age = current_year - age

    print('Hello', name+',', 'your age is', current_age)
