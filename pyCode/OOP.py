class Product():
    # def __init__(self) -> None:
    #     pass

    def __init__(self, id, name, model, price, count): # init method for creating a new object of the class
        self.id = id
        self.name = name
        self.model = model
        self.price = price
        self.count = count

    def discount(self, ratio):
        self.price = self.price - self.price*ratio

    def info(self):
        return f'\n Information about id: {self.id} \n =======================\n Name: {self.name}, Model: {self.model}, Price: ${self.price}, Count: {self.count}'



p1 = Product(1,'Apple','iPhone 15 pro max', 1500, 30)
p2 = Product(2,'Samsung','Galaxy S25 Ultra', 1500, 50)
p3 = Product(3,'Oppo','Reno 7', 1000, 10)

print('\n','Original prices:'+'\n','='*16)
print(f'{p1.name}, {p1.model}, ${p1.price}')
print(f'{p2.name}, {p2.model}, ${p2.price}')
print(f'{p3.name}, {p3.model}, ${p3.price}')

print('\n','After discount:\n', '='*15)
p3.discount(0.30)
print(f'{p3.name}, {p3.model}, ${p3.price}')

print(p1.info())
print(p2.info())
print(p3.info())
