# index() function determines the location of an item within a list.
l = ['Omar', 'Sharawi', 'Mohamed', 'Omar']
print(l.index('Omar'))

print('-'*30)
# count() function determines the number of times an element in a list is repeated.
print(l.count('Omar'))

print('-'*30)
# copy() function returns a copy of the list.
test = l.copy()
print(test)

print('-'*30)
# clear() function clears all list items.
test.clear()
print(test)