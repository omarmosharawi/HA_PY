class point:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        return point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self): # without this function the result will be printed in the location type
        return f'New point after addition: ({self.x},{self.y},{self.z})'

pt1 = point(1,2,3)
pt2 = point(1,2,3)

print(pt1+pt2) # this an error before we added the __add__ function # we have to find a key to make this operator
# print(dir(int)) # dir() this will print Magic keys



class cart:
    def __init__(self,items):
        self.items = items

    def __getitem__(self, key):
        return self.items[key]

order = cart(['Pen', 'Pencil', 'Book', 'Notebook', 'Calculator'])
print(order) # will print the location in the memory
print(order.items) # will print the list
print(order.items[0]) # will print the first element in the list
print(order[1]) # will be print an error before declaration of the __getitem__ function
