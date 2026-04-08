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


    
marks =[23, 67,45,33]
for ss in marks:
    print(ss)
marks.append(99)
marks.insert(2, 77)
marks.insert(3, 47)
print(marks)
print("..........................")

for mark in marks:
    if mark==45:
        break;
    print(mark)
print("..........................")
print(marks)
print("..........................")

for mark in marks:
    if mark==45:
        continue
    print(mark)
print("..........................")