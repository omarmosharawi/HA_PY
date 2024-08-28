l = []
t = ()
print("1)", type(l), type(t))

names = (('omar','mohamed'),'adel','abdullah','abdelrahman') # tuples are immutable # can't be changed after creation
print('2)', names)



var_names = list(names)  # convert tuple to a list, so we can  modify it
var_values = [0]*len(var_names)   # create a list of zeros with the same length as names

def get_variable(name):
    """Get the value of a variable. If the variable is not defined, return None."""
    if name in var_names:
        return var_values[var_names.index(name)]
    else:
        print("Error: Variable '" + str(name) + "' is undefined.")
        return None

def set_variable(name,value):
    """Set the value of a variable. If the variable is not defined, add it to the list of variables."""

t1 = (1) # defined a mathematic operation
t2 = (3,) # defined a tuple
t3 = 1,2,3 # defined a tuple
print("3)", type(t1), type(t2), type(t3))
print('4)', len(t3))
print('5)', len(t2) , len(t3))
print('6)', len(t2) + len(t3))
print('7)', t2+t3)
print('8)', 1 in t3)
print('9)', 5 in t3)

t4 = 1,2,3,4,5 # defined a tuple
t5 = 'one','two','three','four','five' # defined a tuple
print('10)', t5)
t5 = t4 # swapping tuples
print('11)', t5)

t6 = 2022
t7 = 2024
t7, t6 = t6, t7 # swap values of two variables # The process of assigning two elements to each other
print('12)', t6, t7)
