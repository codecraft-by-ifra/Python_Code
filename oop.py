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

