numbers = [1,2,3,4,5,6,7]

def getSquare(x):
    return x ** 2

# map() function makes a new list by applying the given function to each element of an iterable
squares = map(getSquare, numbers)
print(squares) # will be print location
print(list(squares))

# we can use lambda to make short code
squares = map(lambda x: x**2, numbers)
print(squares) # new located because we made an update
print(list(squares))



# program convert temp from Celsius to Fahrenheit
temps = [('Cairo',22),('Canada',3),('London',7),('KSA',25),('Palestine',17)]

def CtoF(c):
    return c[0], (1.8)*c[1] + 32

final_temp = list(map(CtoF, temps))
print('\n', final_temp)

# by using lambda function
CtoF = list(map(lambda c: (c[0], (1.8)*c[1] + 32), temps))
print(CtoF)

# another way using another paradigms
f_temps = []

for temp in temps:
    f = (1.8) * temp[1] + 32
    f_temps.append((temp[0], f))

print(f_temps)



# filter() method creates a new list with all elements that pass the test implemented by the provided function
languages = [('C',1972),('C++',1985),('Java',1995),('JS',1995),('PHP',1994),('Python',1991)]

def old(y):
    return y[1] < 1990

oldLang = filter(old, languages)
print('\n', list(oldLang))



# program
def find(iterable, text):
    def finder(lang):
        for i in lang:
            if str(i).startswith(text): return True
            return False
    return list(filter(finder, iterable))

result = find(languages, 'P')
print('\n', result)

result = find(languages, 'C')
print(result)

result = find(languages, 'C++')
print(result)



# reduce() function used to apply a particular function passed in its argument to all the elements of an iterable in a single line
from functools import reduce

add = lambda x, y : x + y
multi = lambda x, y : x * y

numbers = [1, 2, 3, 4, 5, 6 ,7]

summation = reduce(add, numbers)
print('\nsummation of all elements using add function: ', summation)
product = reduce(multi, numbers)
print('product of all elements using multi function: ', product)

maxNumber = reduce(lambda x,y: x if x > y else y, numbers)
print(f'maximum number in list using lambda function: {maxNumber}')
print('largest number in list', max(numbers)) # max() is a built-in Python function that returns the largest item in an iterable or the largest
