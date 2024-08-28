employees = ['Hasan', 'Omar', 'Ahmed', 'Mohamed', 'Sharawi', 'Ali', 'Mariam']

# append() function adds an element to the end of the list.
employees.append('Adel')
print(employees)

oldEmployee = ['Ola', 'Roha', 'Hana', 'Jana', 'Aycel']
employees.append(oldEmployee)
print(employees)
print(employees[8])
print(employees[8][4])

print('-'*15)
# extend() function adds an array of items to the end of the list.
currEmployee = ['Haneen', 'Aya', 'Malak']
employees.extend(currEmployee)
print(employees)

print('-'*15)
# insert() function adds an item to the list at the user-specified location.
employees.insert(1, 'Belal')
print(employees)

print('-'*15)
# del keyword deletes objects of any type (list, string, dictionary, etc.).
del employees[9]
print(employees)

print('-'*15)
# remove() function removes the first item in the list whose value equals the user-specified value.
employees.remove('Haneen')
print(employees)

print('-'*15)
# pop() function deletes the element at the user-specified location.
employees.pop(-1)   # will remove the last element
print(employees)

print('-'*15)
# sort() function in Python is used to sort a list in place by comparing list elements using only the > operator.
employees.sort()
print(employees)

nums = [123, 1594252, 15452, 3.14, -10, 7, 0]
nums.sort()
print(nums)
nums.sort(reverse=True)     # reverse is False by default # revers method will reverse arrangement
print(nums)

# we can't use list gather string and int in the sort method like this
gather = [1, 7, 'Omar', 'Mohamed', 'Sharawi']
# gather.sort()   # this error

print('-'*15)
# reverse() function in Python is used to reverse a list.
l = ['Sharawi', 'Mohamed', 'Omar']
l.reverse()
print(l)