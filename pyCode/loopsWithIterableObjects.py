units = {'mg': 0.001, 'cg': 0.01, 'dg': 0.1, 'g': 1, 'kg': 1000}

print('1)', end=' ')
for unit in units: # it will print all the keys of the dictionary
    print(unit, end=', ')

print('2)', end=' ')
for unit in units.keys(): # Use the keys() method to get a list of all available keys
    print(unit, end=', ')

print('3)', end=' ')
for unit in units.values(): # Use the values() method to get an iterator over the dictionary's values
    print(unit, end=', ')

print('4)', end=' ')
for unit in units.items(): # The items() method returns a list of tuples containing key-value pairs
    print(unit, end=', ')



# another way to display the dictionary in the better format
print('\n5)')
for key, value in units.items():
    print('unit= ', key, ', conversion factor= ', value)



print('\n6)')
for x,y in (1,2),(3,4),(5,6):
    print(x,y)



employees = ['John Doe','Jane Smith','Alice Johnson']
salaries = [50000,75000,85000]

# using zip function to combine two lists
print('\n7)')
for employee, salary in zip(employees, salaries):
    print('Employee Name=', employee,', Salary=', salary)

print('\n8)')
print('Employees')
print('='*9)
for index in range(len(employees)):
    print(index+1, employees[index], '$', salaries[index]) # typed index+1 to show numbering for each employee start from 1

# another way to display this list
print('\n9)')
print('Employees')
print('='*9)
for count, value in enumerate(employees, start=1): # enumerate method used to iterate over elements along with their indices # takes 2 arguments
    print(count, value)

# another way to display this list by while loop instead of for loop
print('\n10) using while loop')
print('Employees')
print('='*9)
index = 0
while index < len(employees):
    print(index+1, employees[index])
    index+=1
