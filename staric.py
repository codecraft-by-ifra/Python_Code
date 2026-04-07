i = 1
while i <= 6:
    print(i * "*")
    i = i+1


print("pyramid design ")

urows = 59
i=1
while i<= urows:
    print(" " * (urows-i) + "*" * (2*i -1))
    i= i+1

drows = 59
i= 59
while i>= 1:
    print(" " * (drows-i) + "*" * (2*i -1))
    i= i-1