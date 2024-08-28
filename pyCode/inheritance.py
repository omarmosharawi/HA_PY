class Product:
    def __init__(self, id, brand, model, price, count):
        self.id = id
        self.brand = brand
        self.model = model
        self._price = price # _ is a protected attribute (this allowed in the same class but not in subclasses (inheritance))
        self.count = count

    def discount(self, ratio):
        self._price = self._price - self._price*ratio

    def get_info(self):
        info =  f"\nInformation about ID: {self.id}" \
                f'\n=========================' \
                f'\nBrand: {self.brand}' \
                f"\nModel: {self.model}" \
                f"\nPrice: ${self._price}" \
                f"\nCount: {self.count}"
        return info
        # return f'\n Information about id: {self.id} \n =========================\n Brand: {self.brand}\n Model: {self.model}\n Price: ${self._price}\n Count: {self.count}'

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return f'\nThe price of {self.brand} {self.model} is ${self._price}'

class Mobile(Product): # Inheritance from the parent class "Product"
    def __init__(self, id, brand, model, price, count, screen_size, storage, ram, color, battery, front_camera, back_camera, cpu, weight):
        self.id = id
        self.brand = brand
        self.model = model
        self._price = price
        self.count = count
        self.screen_size = screen_size
        self.storage = storage
        self.ram = ram
        self.color = color
        self.battery = battery
        self.front_camera = front_camera
        self.back_camera = back_camera
        self.cpu = cpu
        self.weight = weight

    def mobile_info(self):
        # Get information about product (from base class) and additional info about a mobile phone # super() is a function can returns an object that represents the parent class
        info = super().get_info() + \
            f"\nScreen size: {self.screen_size}"\
            f"\nStorage: {self.storage}"\
            f"\nRAM: {self.ram}"\
            f"\nColor: {self.color}"\
            f"\nBattery: {self.battery} hours"\
            f"\nCameras (Front/Back): {self.front_camera}/{self.back_camera}"\
            f"\nCPU: {self.cpu}"\
            f"\nWeight: {self.weight}"
        return info

class Laptop(Product): # Inheritance from the parent class "Product"
    def __init__(self, id, brand, model, price, count, display, storage, ram, color, battery, camera, cpu, screen_card, windows, weight, touch_screen):
        self.id = id
        self.brand = brand
        self.model = model
        self._price = price
        self.count = count
        self.display = display
        self.storage = storage
        self.ram = ram
        self.color = color
        self.battery = battery
        self.camera = camera
        self.cpu = cpu
        self.screen_card = screen_card
        self.windows = windows
        self.weight = weight
        self.touch_screen = touch_screen

    def laptop_info(self):
        info = super().get_info() + \
            f"\nDisplay: {self.display}"\
            f"\nStorage: {self.storage}"\
            f"\nRAM: {self.ram}"\
            f"\nColor: {self.color}"\
            f"\nBattery: {self.battery}"\
            f"\nCamera: {self.camera}"\
            f"\nCPU: {self.cpu}"\
            f"\nGraphics: {self.screen_card}"\
            f"\nWindows: {self.windows}"\
            f"\nWeight: {self.weight}"\
            f"\nTouch screen: {self.touch_screen}"
        return info

class Monitor(Product): # Inheritance from the parent class "Product"
    def __init__(self, id, brand, model, price, count, rgp):
        super().__init__(id, brand, model, price, count) # Calling the constructor of the parent class
        self.rgp = rgp

    def monitor_info(self):
        info = super().get_info() + "\nRGP: {}".format(self.rgp) # .format is used to insert variables into a string</ instead of f'RGP: {self.rgp}'
        return info



# Create objects for each classes

phone1 = Mobile(id='M01', brand='Apple', model="IPhone7 4G 1NanoSIM", price=130, count=5, screen_size="4.7 inches 1337×750", storage='64GB', ram='2GB', color='Gold', battery='1960MA', front_camera='7MP', back_camera='12MP', cpu='A10 4N 2.34GZ', weight='138g')
# print(phone1.get_info()) # will get information about phone1 object from Product class
print(phone1.mobile_info()) # will get information about phone1 object from Mobile class



laptop1 = Laptop(id='L01', brand='HP', model="ZBook Studio G10 16", price=3750, count=3, display="40.6 cm (16), (3840×2400), OLED", storage='512GB SSD + 1TB SSD', ram='2× 32GB DDR5-5600 MHz', color='Gray Silver', battery='200W external AC power adapter 6-cell, 86Wh Li-ion polymer', camera='720p HD IR', cpu='Intel Core i9-13900H up to 5.4GHz with intel turbo boost technology, 14cores, 20threads', screen_card='NVIDIA GetForce RTX 4080 - 12GB GDDR6', windows='11 pro', weight='1.75 Kg', touch_screen=True)
# print(laptop1.get_info()) # will get information about laptop1 object from Product class
print(laptop1.laptop_info()) # will get information about laptop1 object from Laptop class



monitor1 = Monitor(id='T01', brand='ASUS', model="ProArt PA329CV - 32-inch - 4k UHD", price=1300, count=10, rgp=False)
# print(monitor1.get_info()) # will get information about monitor1 object from Product class
print(monitor1.monitor_info()) # will get information about monitor1 object from Monitor class
