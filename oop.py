class Home:                      # class
    color = "white"
    location = "kasur"
    comp = 'azire'

    @classmethod          # for chnging the value permanently
    def changename(cls, comp):
        cls.comp = comp

room = Home()                    # object
hall = Home()
print(room.color)
print(hall.location)

print(f'first name of company is : {room.comp}')
room.changename("cringe")
print(f'modified of comapny is : {room.comp}')


# Constructor
class Student:

    def __init__(self, name, marks):             # constructor self call when object make
        print(" perametrized constrctor called")
        self.name = name
        self.marks = marks
    
    def welcome(self):
        return "welcome to the console  " + self.name


s = Student("mehar", 98)
print(s.name, s.marks)

d = Student("giya", 98)
print(s.name, s.marks)

ss = Student("ifra", 95)
print(ss.name, ss.marks)
del d        # del d  deleting the instance d



print(s.welcome())
print('..................................................')

# questions
# Create student class that takes name & marks of 3 subjects as arguments in  constructor.
# Then create a method to print the average.

class Std:

    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    
    def average(self):
        avg = (self.sub1 + self.sub2 + self.sub3)/3
        print(f"The average marks of {self.name} is: {avg:.2f}")

    @staticmethod                    # static method function used to avoid self parameter
    def conclusion():
        print( 'its endinggggg ')

   

c1 = Std("alia", 66, 84, 98)
c2 = Std("saba", 87, 54, 45)
c3 = Std("zuha", 56, 83, 67)

# c1.name = 'ifra'
c1.average()
c2.average()
c3.average()
c3.conclusion()



# property decorator

class Books:
    def __init__(self, bio, sst, geo):
        self.bio = bio
        self.sst = sst
        self.geo = geo
    
    @property
    def percentage(self):
        prcnt = (self.bio + self.sst + self.geo)/3
        return str(f'Percentage is {prcnt:.2f}')
    
bk1 = Books(98,97,99)
print(bk1.percentage)

bk1.sst = 86

print(bk1.percentage)
