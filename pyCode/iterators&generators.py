x = iter(['a', 'b', 'c'])
print(x) # list iterator

print('\n', next(x)) # get next value from iterator, move to next position in sequence # it will be a
print(next(x)) # b
print(next(x)) # c
# print(next(x)) # it will be error - raise StopIteration if there is no more values to return

print('\n', list(iter('abc'))) # convert iterator back into a list (all values)



def myGen():
    i = 1
    print('\n', 'first value:')
    yield i # yield used for returning first value of the generator function and  then pausing execution. It acts like return statement but instead of stopping the function. using instead of return because return statement will be stopped the function.
    i += 1
    print('\n', 'second value:')
    yield i
    i += 1
    print('\n', 'third value:')
    yield i

my_gen = myGen()
print(next(my_gen)) # will be print first value and then will show the result of first yield # 0
print(next(my_gen)) # will be print second value and then will show the result of second yield # 1
print(next(my_gen)) # will be print third value and stop iteration. Will not show anything after this point. # 2



# pipelining operator for parallel processing
# means that we can pass generator function as an argument to another generator function

# program to print sum of squares of odd numbers till n using generators
def odd_number(oddNumbers):
    for num in range(1, oddNumbers,2):
        yield num

def square(sqr):
    for num in sqr:
        yield num ** 2

print('\n', sum(square(odd_number(7)))) # sum of squares of odd numbers



# generators comprehension
odd_number2 = (num for num in range(1, 7, 2))
square2 = (num ** 2  for num in odd_number2)

print('\n', sum(square2))



# abbreviation the code # We don't recommend using this method because it will reduce the ability to understand the code
result = sum(x**2 for x in (x for x in range(1,7,2)))

print('\n', result)



# we can use generators inside list comprehension or dictionary comprehension
squares = [num**2 for num in odd_number(7)]
cubes = [num**3 for num in squares]

print('\n', cubes)
