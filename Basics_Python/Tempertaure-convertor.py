def celsius_to_fahrenheit(c):
    return (c * 9/5) - 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def Kelvin_to_celsius(k):
    return k - 273.15

def celsius_to_Kelvin(c):
    return c + 273.15


print("Welcome to Temperature Converter!")
print("Choose conversion type:")
print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")
print("3: Kelvin to Celsius")
print("4: Celsius to Kelvin")

Choice = input('Enter the choice  1 / 2 / 3 / 4  : ')

if Choice == '1':
    c = float( input ('Enter temperature in Celsius: '))
    print(f'{c}°C = {celsius_to_fahrenheit(c):.2f}°F')

elif Choice == '2':
    f = float( input ('Enter temperature in Fahrenheit: '))
    print(f'{f}°F = {fahrenheit_to_celsius(f):.2f}°C')

elif Choice == '3':
    k = float( input ('Enter temperature in Kelvin: '))
    print(f'{k} K = {Kelvin_to_celsius(k):.2f}°C')

elif Choice == '4':
    c = float( input ('Enter temperature in Celsius: '))
    print(f'{c}°C = {celsius_to_Kelvin(c):.2f} K')

#