def std_info(name, age, level):
    print(f"Name: {name}, Age: {age}, Level: {level}")
    return

std_info("John", 16, "Junior")
std_info(age=20, name="Mike", level="Senior")
std_info(name="Emily", **{"age": 18, "level": "Master"})
std_info('Lucas', *[22], 'Pro')
std_info('Omar', age=20, level='Advanced')
# std_info('Mohamed', age=19, 'Junior') # this an error because we can't pass a string as keyword argument
# std_info('Ahmed', None, age=19) # this an error because the function expects a string but got None instead of a string
# std_info('Ali', age=15, 'Intermediate') # This will also be treated as positional arguments and will give an error



# default parameter value
def std_info(name, age, level=None): # this error to make std_info(name, level=None, age) because we should to put a default parameters at the end
    print(f"Name: {name}, Age: {age}, Level: {level}")
    return

std_info("John", 16) # level will be None by default if you don't put the argument in the function call.
std_info("John", 16, "Junior") # level is Junior and it will not throw any errors because put the argument in the function call



# *args method # used to send any number of arguments that are not predefined (like list or dictionary)
def sum_args(*args): # can change the args name to any name as you like
    total = 0
    for num in args:
        total += num
    return print(f'The sum is: {total}')

sum_args(1,5,6,8,7,2,11)



# **kwargs method  # used to send named arguments which are not predefined and their names are known beforehand
def weather(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

weather(city="London", temperature=34, wind="Strong")



# program take 2 arguments and make power operation between them
def program1(number, power):
    result = 0
    result = number ** power
    return print(f"Your operation: {number}^{power} = {result}")

# get the user input as a string
user_input = input(f'Enter 2 numbers to make an operation (make a space between them): ')
# split the string by spaces and convert each value to an integer
user_input = [int(x) for x in user_input.split()]
# unpack the list into two variables
number, power = *user_input,
# call the function with the two arguments
program1(number, power)



# program take information from student and print it
def stdInfo(name, age, grade, phone=None):
    if phone == '':
        return print(f"\nName: {name}\nAge: {age}\nGrade: {grade}")
    else:
        return print(f"\nName: {name}\nAge: {age}\nGrade: {grade}\nPhone Number: {phone}")

name = input('Enter your name: ')
age = int(input('Enter your age: '))
grade = float(input('Enter your grade: '))
phone = input('Enter your phone: ')

stdInfo(name, age, grade, phone)
