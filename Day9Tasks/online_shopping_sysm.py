class Product:
    def __init__(s,name): s.name = name

class ElectronicProduct(Product):
    def __init__(s,name,brand):
        super().__init__(name)
        s.brand = brand

class MobilePhone(ElectronicProduct):
    def __init__(s,name,brand,price):
        super().__init__(name,brand)
        s.price = price

    def show(s):
        print(s.name, s.brand, s.price)

m = MobilePhone("Phone","Samsung",25000)
m.show()

#super:used to call parent constructor
