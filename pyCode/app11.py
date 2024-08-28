# this app using exceptions to handle errors

class toOldErrors(Exception):
    def __str__(self):
        return "Sorry, you can't sign in because you are too old"

class toYoungErrors(Exception):
    def __str__(self):
        return "Sorry, you can't sign in because you are too young"

age = int(input("Enter your age: "))
if age < 18 : raise toYoungErrors()
if age > 70 : raise toOldErrors()



# another way with using a specific error message for each exception
class toOldErrors2(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class toYoungErrors2(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

age = int(input("Enter your age: "))
if age < 18 : raise toYoungErrors2(f'Your age: {age} is too young')
if age > 70 : raise toOldErrors2(f'Your age: {age} is too old')



# another way with using try -except blocks and raising the appropriate exception
try:
    age = int(input("Enter your age: "))
    if age < 18 : raise ValueError("You are too young")
    elif age > 70 : raise ValueError("You are too old")
    else: print('Congratulations! You have signed in successfully')
except ValueError as e:
    print(e)
