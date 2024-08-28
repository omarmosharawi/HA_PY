numbers = {1,2,3,4,5,6,7} # is a set
fruits = {'apple','banana','lemon'} # is a set
empty = {} # is a dict

list = ['omar','mohamed'] # is a list
# can use set() function to convert it into a set.
makeListToSet = set(list)
print('1)', type(list),'2)', type(makeListToSet))

x = {'string', 7, 7.7, 3+4j, (0,3)} # can use mixed data types in a set

# check if an item exists in the set using 'in' keyword
print('3)', "Is apple in fruits? ", 'apple' in fruits)
print('4)', "Is orange in fruits? ", 'orange' in fruits)
print('5)', "Is orange in fruits? ", 'orange' not in fruits)

print('6)', len(x))



# sets operators
s1 = {1,2,3,4}
s2 = {4,5,6,7}
s3 = {4,7,9,11,13}

# union (|) used to combine two or more sets and returns a new set with all elements from both sets
print('7)', s1 | s2) # or use set1.union(s2)
print('8)', s1 | s2 | s3) # or use set1.union(s2, s3)

# intersection (&) gives common elements between two sets and return a new set with those common elements only
print('9)', s1 & s2) # or use set1.intersection(s2)
print('10)', s1 & s2 & s3) # or use set1.intersection(s2, s3)

# difference (-) used to return a new set that contains items present in one set but not the other
print('11)', s1 - s2) # or use set1.difference(s2)
print('12)', s1 - s2 - s3) # or use set1.difference(s2, s3)

# symmetric_difference (^) used to return a new set containing only the members of either set
print('13)', s1 ^ s2) # or use set1.symmetric(s2)
print('14)', s1 ^ s2 ^ s3) # or use set1.symmetric(s2, s3)



y = set()
y.add(1) # add method is used to insert one element into the set
print('15)', type(y), y)
y.remove(1) # remove method is used to delete/remove an element if found from the set
print('16)', y)
# y.remove(1)
# print('16)', y) # error because not found the number to remove it
y.discard(1) # discard method is used to remove an element from the set (no error if not found the element)
print('17)', y)
# pop() method removes and returns an arbitrary object from Set. It should be used when you want to get rid of
# clear() method removes all elements from the set
