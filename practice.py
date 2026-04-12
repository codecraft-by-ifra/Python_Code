# write a function which takes input and print the input is even or odd
def isEven_Odd(n):
    if n%2 == 0:
        return (f'{n} is the Even Number')
    else:
        return (f'{n} is the Odd Number')
    
num = int(input('Enter a Number : '))
print (isEven_Odd(num))
print('.........................................')


# write a function to find the factorial of n
def isFactorial(n):
    fact= 1
    for i in range(1, n+1):
        fact *= i
    return(f'The Factorial of {n} = {fact} ')

print (isFactorial(3))
print('.........................................')


# Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the
# circle.

class Circle:

    def __init__(self, radius):
        self.radius = radius
    def showradius(self):
        return(f'The Radius Of Circle is : {self.radius} ')
    def area(self):
        ar = (22/7)* self.radius**2
        return(f'The Area of Circle is : {ar}')
    def perimeter(self):
        per = 2*(22/7)* self.radius
        return(f'The Perimeter of Circle is : {per}')


c1 = Circle(21)
print(c1.showradius())
print(c1.area())
print(c1.perimeter())
print('.......................................')

# Define a Employee class with attributes role, department & salary. 
# This class also a showDetails( ) method.

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showdetails(self):
        print(f'The Role of Employee is : {self.role}')
        print(f'The Department of Employee is : {self.department}')
        print(f'The Salary of Employee is : {self.salary}')
        
Emp = Employee('Manager', 'Softwar Tech', 120000)
Emp.showdetails()
print('.......................................')

# Create an Engineer class that inherits properties from Employee & 
# has additional attributes : name & age.

class Engineer(Employee):
    def __init__(self, role, department, salary, name, age):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age
    def showEngDetail(self):
        print(f'The Name of Engineer is : {self.name}')
        print(f'The Salary of Engineer is : {self.salary}')
    

Eng = Engineer('Accountant','Finance','80000', 'Zain', 22)
Eng.showEngDetail()
Eng.showdetails()
print('............................................')