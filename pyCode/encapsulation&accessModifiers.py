class Product:
    def __init__(self, id, name, model, price, count):
        self.__id = id # __ is a private attribute (this not allowed to access from outside)
        self.name = name
        self.model = model
        self._price = price # _ is a protected attribute (this allowed in the same class but not in subclasses (inheritance))
        self.count = count

    def discount(self, ratio):
        self._price = self._price - self._price*ratio

    def info(self):
        return f'\n Information about id: {self.__id} \n =======================\n Name: {self.name}, Model: {self.model}, Price: ${self._price}, Count: {self.count}'

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return f'\nThe price of {self.name} {self.model} is ${self._price}'

p1 = Product(1,'Apple','iPhone 15 pro max', 1500, 30)

p1.__id = 7
# it will not change the product id because it's a private but you can do this trick to change it => print(p1.__id = 7)
print(p1.info())

# p1.price = 5
# it will not work now because we make the price is a protected attribute but we can use p1._price or the function p1.set_price() to change it
p1.discount(0.25)
print(p1.get_price())

# this way to change the private attribute value
p1.__id = 7
print(f'\n{p1.__id} is a product id of {p1.model} after we make changes in private attributes')

# this another way to change the private attribute value
p1._Product__id = 3
print(f'\nThis a new product id of {p1.model} after we make another changes in private attributes:')
print(p1.info())
