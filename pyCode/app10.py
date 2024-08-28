# divide list into lists of equal length

list = [1,2,3,4,5,6,7,8,9]
division = []
size = 3

for i in range(0, len(list), size):
    division.append(list[i:i+size])

print(division)



# another solution
division = [list[i:i+size] for i in range(0, len(list), size)]
print(division)
