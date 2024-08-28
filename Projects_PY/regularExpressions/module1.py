import re

# search() function searches for the first location where a given regular expression matches, and returns the corresponding match object.
text = 'My name is Omar Mohamed'
search = re.search("[A-Za-z]", text)
print(search)
print(dir(search))  # to know all built-in functions for a specific attribute

print('-'*30)
# findall() function returns all matches with the given regular expression.
t = """
Hello, my number is 476-597-1654
my friend number is 623-456-1694
"""
s = re.findall(r"\d{3}-\d{3}-\d{4}", t)
print(s)

print('-'*30)
# group() function returns the string of characters found in the text and stored in a match object.
print(search.group())

print('-'*30)
# span() function returns a tuble representing the start and end positions of the found match object.
print(search.span())



print('-'*30)
txt = 'Call me at 415-564-7590 tomorrow. 415-555-9999 is my office'
test = re.search(r"\d{3}-\d{3}-\d{4}", txt)
print(test)
print(test.group())



print('-'*30)
# simple app using findall() function

pNumber = input("Enter your number: ")
sPhone = re.findall(r"\d{3}-\d{3}-\d{4}", pNumber)
list = []

if sPhone == []:
    print('this number is not valid')
else:
    list.append(sPhone)
    print('the number is added')