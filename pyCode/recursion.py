def fact(x):
    if x <= 1:
        return 1
    else:
        return x * (fact(x-1)) # recursion

print(fact(7), '\n')



# program
data = [[1,2,3,'Omar','Mohamed'],(1,2,3,'Omar','Mohamed'),'Hello World',7]

def print_data(data):
    if not data: return

    if (type(data[0]) == list or type(data[0]) == tuple):
        print_data(data[0])
    else:
        print(data[0])

    print_data(data[1:])

print_data(data)
