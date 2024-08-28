def myFunction(x):
    return x

# this function using lambda expression to define a new function
lambda x: x

print(myFunction)
print(lambda x: x)



print((lambda x: x+2)(5))

addTwo = lambda x,y: x+y
print(addTwo(3,4))



student_name = lambda firstname, lastname: f'Hello, {firstname.title()} {lastname.title()}'
print(student_name('omar', 'mohamed'))



# program using *args and **kwargs in the same function
def greet(*greetings, **names):
    for greeting in greetings:
        print(f"{greeting}, ", end='')

        if names:
            for name in names:
                print(names[name], sep=', ')
        else:
            print("Everyone")

    print()

greet("Good morning", "Good afternoon", "Good evening")
greet("Morning", "Afternoon", "Evening", firstname="Omar", lastname="Mohamed")



# can use lambda function with *args and **kwargs
print((lambda *args: sum(args))(1, 2, 3, 4, 5))
print((lambda **kwargs: sum(kwargs.values()))(a = 100, b = 200, c = 300))



# program
ids = ['id20', 'id47', 'id89', 'id71', 'id16']

ids.sort() # this will sort ids list in ascending order by alpha
print('\n',ids)

# we can use lambda function her to make some changes on control of list to arrangement
ids.sort(key = lambda  x: int(x[2:])) # this will sort the id based on their numbers at the end
print('\n',ids)

# another way in normal function
def sort_ids(x):
    return int(x[2:])

ids.sort(key = sort_ids)
print('\n', ids)
