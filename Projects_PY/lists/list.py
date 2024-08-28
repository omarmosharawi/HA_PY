employees = ['Hasan', 'Omar', 'Ahmed', 'Mohamed', 'Sharawi', 'Ali', 'Mariam']

print(employees)        # will print all list(array)

print(employees[0])     # will print index first index
print(employees[-1])    # will print last index
print(employees[3])     # will print index 3 or fourth from left to right
print(employees[-3])    # will print the third from right to left
# print(employees[10])    # will print error because the index out of range

# using slicing
print(employees[1:4])   # will print from index 1 to 3
print(employees[:])     # will print full list
print(employees[1:])    # will print from index 1 to end
print(employees[:3])    # will print from start to index 2
print(employees[::1])   # will print from start to end by 1 step

# update
employees[0] = 'Adel'   # update index 0
print(employees)

employees[5:] = 'Abdelrahman', 'Roha', 'Emad'   # update from index 5 to end and add new index
print(employees)

employees[:] = ''   # will remove all indexes
print(employees)
print(len(employees))

# using for loop
employees = ['Omar', 'Mohamed', 'Ali']
for i in range(3):  # must use num of indexes in range
    print(employees[i])

for i in range(len(employees)):     # using len of the list to avoid errors
    print(employees[i])

for i in range(len(employees)):
    print(f'The index {i} is: {employees[i]}')  # using string format

for index, item in enumerate(employees):    # using enumerate function
    print(f'The index {index} is: {item}')

# checks
print('Omar' in employees)
print('Omar' not in employees)

print('-'*10)
import random

print(random.choice(employees))     # will print random value in string
print(random.choices(employees))    # will print random value in list

random.shuffle(employees)   # shuffle() function shuffles the elements of a list or an iterable object
print('after shuffle function', employees)