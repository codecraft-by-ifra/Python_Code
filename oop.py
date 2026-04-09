class Home:                      # class
    color = "white"
    location = "kasur"

room = Home()                    # object
hall = Home()
print(room.color)
print(hall.location)


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

ss = Student("ifra", 95)
print(ss.name, ss.marks)
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
