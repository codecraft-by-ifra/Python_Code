First = int( input( "Enter your 1st number : "))
Operator =  input ("Enter the opertar ( + , - , * , / , ** , % ):")
Second = int( input( "Enter your 2nd number : "))

if Operator == "+":
    print("Sum: ", First + Second)
elif Operator == "-":
    print("Subtract: ", First - Second)
elif Operator == "*":
    print("Multiply: ", First * Second)
elif Operator == "/":
    if Second != 0:
        print("Divide: ", First / Second)
    else:
     print("Error: Division by zero")

elif Operator == "**":
    print("Power: ", First ** Second)
elif Operator == "%":
    print("Modulo: ", First % Second)
else:  
    print("Invalid operator" )