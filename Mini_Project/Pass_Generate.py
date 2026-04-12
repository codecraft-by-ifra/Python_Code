import string
import random

print('Welcome To Password Generator')
Upper = string.ascii_uppercase
Lower = string.ascii_lowercase
Digits = string.digits
Symbols = string.punctuation

All = list(Upper + Lower + Digits + Symbols)
random.shuffle(All)

try:
    Pass_Length = int(input('Enter The Length Of Password = '))
    print("".join (All[0:Pass_Length]))
except ValueError:
    print('Invalid input! Please enter numbers only (e.g. 8, 10, 12).')


