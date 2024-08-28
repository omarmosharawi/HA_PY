print('math part:')

import math

print('1)', math.gcd(3, 5, 7)) # Greatest Common Divisor (GCD), also known as the greatest common factor (GCF) # can add any numbers as u like
print('2)', math.lcm(3, 5, 7)) # lcm() method returns the least common multiple of given numbers

print('4)', math.floor(4.7)) # floor() function rounds down the specified number to the nearest integer
print('5)', math.ceil(4.1))  # ceil() function rounds up the specified number to the nearest integer
print('6)', round(4.7))      # round() function rounds a number to the nearest integer
print('7)', round(4.1))

print('8)', math.exp(3))     # exp() function calculates Euler's number raised to the power of x (e^x)

print('9)', math.log(1000))      # log() function returns the natural logarithm of x (ln(x), or the
print('10)', math.log(1000, 10)) # base-10 logarithm of x (log10(x))
print('11)', math.log10(1000))   # log10() is equivalent to log (x, 10). It computes the base-10 logarithm of x

print('12)', math.pow(3,2)) # pow() function returns the result of x**y; it is equivalent to x*x in this case
                            # The pow() function can be used in two ways:
                            # 1- Without a second argument, it computes the square root of the first argument.
                            # 2- With a second argument, it raises the first argument to the power of the second argument.
# when you use the pow() it will return a decimal number and when you don't use the pow() it will return an integer
print('13)', 3**2)

print('14)', math.sqrt(144)) # sqrt()  function returns the square root of the specified number
                             # It also works with complex numbers
                             # return a decimal number

print('15)', math.sin(1)) # sin() function returns the sine of an angle in radians.
print('16)', math.cos(1)) # cos() function returns the cosine of an angle in radians.
print('17)', math.tan(1)) # tan() function returns the tangent of an angle in radians.

print('18)', math.pi) # pi constant represents the mathematical constant pi (approximately equal to 3.14)
print('19)', math.e)  # e constant - mathematical constant equal to approximately 2.718281828459045



print('='*30)
print('decimal part:')

import decimal

print('1)', decimal.getcontext()) # getcontext() will print all current context information

d1 = decimal.Decimal(7) # Decimal class converts a string or number to a decimal object
print('2)', d1)
d2 = decimal.Decimal('3.14') # Decimal objects support arithmetic operations like addition and subtraction
print('3)', d2)
d3 = decimal.Decimal(3+4) # You can make operators(*,/,+,-) on integers and floats together as decimals
print('4)', d3)

decimals = [d1, d2, d3]
print('5)', sum(decimals)/len(decimals))   # you can use sum() method for adding up values in list
                                           # len() function gives the count of elements in list
print('6)', max(decimals))                 # max() function returns the largest item in list
print('7)', min(decimals))                 # min() function returns the smallest item in list
print('8)', d1.sqrt())                     # sqrt() and other methods are available for Decimal objects too



print('='*30)
print('random part:')

import random

print('1)', random.random())       # It generates a random float number between 0 and 1
print('2)', random.randint(1, 10)) # randint() function returns a random integer between given two numbers
print('3)', random.randrange(10))  # randrange() is used when we need a random integer within a range

names = ['Omar', 'Mohamed', 'Ahmed', 'Joe', 'Ali', 'Michel', 'Abram']
print('4)', random.choice(names))       # choice() function randomly selects an element from the passed iterable
print('5)', random.choices(names))      # choices() function works just like choice(), but it returns a list with multiple random items
print('6)', random.choices(names, k=3)) # choices() function return a specific length list with random selection

print('7)', names)    # before shuffle
random.shuffle(names) # shuffle() rearranges the items in the list randomly
print('8)', names)    # after shuffle
