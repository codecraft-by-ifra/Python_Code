#single inheritence
class Car:

    color = 'black'

    @staticmethod
    def start():
        return 'car is start....'
    
    @staticmethod
    def end():
        return 'car is stoped.'
    
    def __init__(self,b_name):
        self.b_name = b_name
        

c1 = Car('Mehran')
c2 = Car('Cultus')
print(c1.start())
print(c2.b_name)

# multilevel inheritence

class Hondye(Car):

    def __init__(self, b_name, type):
        super().__init__(b_name)
        self.type = type


    @classmethod
    def engine(cls, eng):
        cls.eng = eng

H1 = Hondye('mehran','PETROL')
H2 = Hondye('cultus','DIESEL')
H3 = Hondye('vegon','GAS')

Hondye.engine('1200 CC')

print('...............multilevel..................')
print(H1.start())
print(H3.type, H3.b_name)

print(H3.end())
print(H1.eng)
print('...............multiple..................')     

#simple class

class Abc:
    varA = "its be the content of class Abc"

# multiple inheritence
class All(Car, Abc):
    varg = 'class all content'

    def __init__(self, b_name):
        super().__init__(b_name)

al = All('kia')


print(al.start())
print(al.b_name)
print(al.varA)
print(al.varg)
print(al.end())
