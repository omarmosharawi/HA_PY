numbers = [12,1,345,67,890,123,30,45,78,90,7]

myNumbers = []
for number in numbers:
    if number > 30:
        myNumbers.append(number)
print('1)', myNumbers)

# another way to do it using list comprehension
myNumbers = [number for number in numbers if number > 30]
print("2)", myNumbers)



# another example
squares = []
for i in range(10):
    squares.append(i*2)
print('3)', squares)

# using list comprehension
squares = [i*2 for i in range(10)]
print('4)', squares)



# another example to use if - else
percentages = [20,100,45,150,99,65,105]
new_percentage = [i if  i <= 100 else None for i in percentages]
print('5)', new_percentage)

# using in dictionary format
percentages2 = {i: i*2 for i in percentages}
print('6)', percentages2)



numbers2 = [1,4,5,5,6,7,7,7,10,25,1,2,3,3,5,7,1,7,30]
dictForTest = {i for i in numbers2}
print('7)', dictForTest) # this will give us a set of unique elements from the list without repeat



# using matrix
matrix = [[0,1,2],[0,1,2],[0,1,2],[0,1,2],[0,1,2]]
print('8)', matrix)

# matrix using comprehensions
newMatrix = [[i for i in range(3)] for j in range(5)]
print('9)', newMatrix)
