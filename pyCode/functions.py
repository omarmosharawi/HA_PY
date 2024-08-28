# define empty function
def my_function():
    pass # pass is a keyword in Python that does nothing. It's used as a placeholder for code that will



# define simple function
def simple_function():
    print('1) This is a simple function')

# call the function
simple_function()



# using return statement to get value from a function # return statement can be used to send back any type of data (value or object)
# return statement can be used more than one time within another code block and one time only in the one code block
def new_function():
    return 'Hello, I am a new function!' # this line returns a value which can be stored in a variable or printed
    # examples of calling other functions from within this one
    # return 45
    # return 5*5
    # return [1,2,'hello']

x = new_function() # calling a function and assigning its return value to a variable
# x = new_function()[0]  # accessing an element of what was returned by the function (a list or tuple)
print('2)', x)
