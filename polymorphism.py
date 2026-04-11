# Dunder/ magic  methods
class Complex:

    def __init__(self, real , img ):
        self.real = real
        self.img = img

    def addnumb(self):
        print(f'{self.real}i + {self.img}j')

    def subnumb(self):
        print(f'{self.real}i - {self.img}j')

# use underscore in end or start for dunder method
    def __add__(self, num2):                  # self = num1
        Nreal = self.real + num2.real
        Nimg = self.img + num2.img
        return Complex(Nreal, Nimg)
    
    def __sub__(self, num2):                  # self = num1
        Nreal = self.real - num2.real
        Nimg = self.img - num2.img
        return Complex(Nreal, Nimg)
    

num1= Complex(1,3)
num2= Complex(5,2)
num3 = num1 + num2
num4 = num1 - num2

# for addition printing 
num1.addnumb()
num2.addnumb()
print('--------')
num3.addnumb()
print('--------')
print('--------')


# for subtraction printing
num1.subnumb()
num2.subnumb()
print('--------')
num4.subnumb()
print('-------------------------------------------------------------')

# Qs. Create a class called Order which stores item & its price.
# Use Dunder function __ gt_() to convey that:
# order1 > order2 if price of order1 > price of order2
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = Order('Lays', 150)
ord2 = Order('sprite', 120)
print(ord1 > ord2)
        