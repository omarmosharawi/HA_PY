x = 100

def print_number(y):
    z = x + y
    return print(f'{x} + {y} = {z}')

print_number(200)



def print_number2():
    global x # global keyword is used to access the variable from outside of the function. If not used, it will create
    return print(x)

print_number2()



def outer():
    x = 100

    def inner():
        nonlocal x # nonlocal keyword allows access to the variable from an enclosing function. It does not allow access to a global variable of the same name.
        x += 100

    inner()
    return print(x)

outer()
