str1 = 'this is string one'

# indexing # get one object
print(str1[0])
print(str1[7])
print(str1[17])
print(str1[-1])
print(str1[-3])

print('-'*7)

# slicing [start:end:step(optional)] # get more one object # indexes start from zero
print(str1[:])       # print from start to end
print(str1[0:])      # start from the index[0] to the end
print(str1[:18])     # start from the first to index[18]
print(str1[0:18:1])  # will start from index[0] to index[18] by 1 step # will print completed sentence
print(str1[::1])     # will moving from start to end by 1 step
print(str1[::2])     # will moving from start to end by 2 step
print(str1[::-1])    # will moving from end to start by 1 step
print(str1[::-3])    # will moving from end to start by 3 step
print(str1[5:14])    # start from index[5] to index[13]
print(str1[:-3])     # start from start(index[0]) to the last index before end point # will print all strings without the last 3 indexes
print(str1[5:-3])    # will start from index[5] from right to index[4] from left
print(str1[-13:-4])  # will start from index[13] from left to index[5] from left # can't move by negative in this case