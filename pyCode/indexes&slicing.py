metals = ['iron', 'copper', 'silver', 'nickel', 'gold']
print('1)', metals[1:4], end=' ') # end method makes no new line
print('2)', metals[0:1], end=' ')
print('3)', metals[:3], end=' ') # this a shortcut to print from start to index-1
print('4)', metals[0:], end=' ') # this a shortcut to print from start to end list
print('5)', metals[-1:]) # this a shortcut to print from the end

print('6)', metals[0:4:3], end=' ') # this method make movement in steps of 3, starting at position 0.
print('7)', metals[4:0:-3]) # this method make movement in steps of -3, starting at position 4 and going backwards.

print('8)', metals[5:], end= ' ') # this will give us all elements after index 5 if found
print('9)', metals[0:30]) # out of range index so it gives error

print('10)', metals[:]) # this is just a copy of whole list   # print from start to finish list

metals[1] = 77
print('11)', metals)

# metals[1:3] = 77 # this an error because should take a string or number not tuple
metals[1:3] = '77'
print('12)', metals)

metals[1:3] = [7,777] # you can add more indexes
print('13)', metals)

metals[0:3] = [] # you can add null value   # can use () or '' instead of []
print('14)', metals)
