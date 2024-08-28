lst1 = [1,2,3,4,5]
lst2 = [5,7,8,9,10]
lst3 = [lst1,lst2]
myList = [7,7.3,'Omar',False]
nestedList = [7,['omar','mohamed'], True]

print('1)', type(myList))
print('2)', lst1+lst2)
print('3)', lst3)
print('4)', myList)
print('5)', myList[1])
print('6)', myList[-2])
print('7)', nestedList[1])
print('8)', nestedList[1][0])

nestedList[1][1] = 'sharawi'
print('9)', nestedList)

del myList[-1] # removed index -1 from right or 3 from left which is the last element in list
print('10)', myList)

myList +=  [11, "Omar Sharawi"] # added a new item to the end of the list
print('11)', myList)

# insert an item at specific position
myList.insert(1, "adel")
print('12)', myList)

# remove item by value not position
try:
    myList.remove("adel")
except ValueError as e:
    print('13)', str(e))

print('14)', myList)

myList.append('adel') # append added a new item to the end of the list # append takes 1 argument only
print('15)', myList)

myList.append(['mariam', 11])
print('16)', myList)

# check if an item exists in the list using the in keyword
if 'adel' in myList:
    print('17) Adel exist in the list!')
else:
    print('17) Adel does not exist in the list!')

myList.append(lst1) # add a new list in current list
myList.extend(lst1) # extend adds all items of another list into the current list # it can take multiple lists as arguments
print('18)', myList)

lst3.pop() # removes and returns the last item in the list # it can take a position but here we used it without any parameter so it will remove the last item
print('19)', lst3)
lst2.pop(2)  # remove one item from the list by its index (not value)
print('20)', lst2)

# pop item by reference not by value
lst3.append([1,2,3])
print('21)', lst3)

index = lst3.index([1,2,3])   # return first occurrence of the specified value
                                # raises a ValueError if the value is not present.
print('22) Index of [1,2,3] : ', index)

element = lst3.pop(index)     # removes and returns the element at the given position in the list
print('23) Removed Element : ', element)
print('24) After removing [1,2,3], lst3 becomes : ', lst3)

# check if all items are in another list using all() function
print('25) Checking if all elements in lst1 are in myList : ', all(i in myList for i in lst1))

# check if any item is in another list using any() function
print('26) Checking if any element from nums is in myList : ', any(i in myList for i in lst1))

try:
    x = myList.remove('not_exist')   # remove tries to remove the first occurrence of the value
except ValueError as ve:
    print("Caught expected exception : ", ve)
finally:
    print('After trying to remove "not_exist" : ', myList)

print('27)', 'omar' in myList)
print('28)', 7 in myList)

newList = [7,3,10,11,1]
print('29)', newList)
newList.sort() # sort the list in ascending order # can't written into print functaion
print('30)', newList)
newList2 = ['omar','mohamed','sharawi','adel','abdullah']
print('31)', newList2)
newList2.sort()
print('32)', newList2)
newList2.sort(reverse=True) # sort the list in descending order
print('33)', newList2)

# count how many times an item appears in the list using count() method
print('34) How many times does "adel" appear in newList2? : ', newList2.count('adel'))

# find the index of an item that occurs more than once using the index() method
first_occurrence = newList2.index('adel')
print('35) The first time Adel appeared in newList2 was at this index : ', first_occurrence)

print('36)', len(newList)) # len() method gives you the number of items (length) in a list # count start from 1
