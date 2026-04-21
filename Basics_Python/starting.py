message = 'hello its ifra'  
         # OR
message = "hi, its mehar"

# msg='there's s polybag'      to avoid this use slash
msg='there\'s a polybag'
         # OR
msg="there's a polybag"
# []  -->   list
# {}  -->   set    has unique values
# ()  -->   tuples    not changeable , allow duplicates

num= [3,7,9,4,1,3]
course = ["math", "physics","chemistry", "literatre", "english"]


c_str = ','.join(course)
d_tr = ' - '.join(course)
print (course)      # this give output ['math', 'physics', 'chemistry', 'literatre', 'english']
print (c_str)       # this give output  math,physics,chemistry,literatre,english
print (d_tr)       # this give output  math - physics - chemistry - literatre- english


course[1]='computer'
print(course)

course.append("biology")
print (course)
course.extend("sst")
print (course)
course.insert(1,"sicology")
print (course)
course.remove("math")
print (course)
course.reverse()
print (course)
course.sort()
num.sort()
print (course)
print(num)
num.sort(reverse=True)  #descending order
print(num)
print(min(num))
print(max(num))
print(min(course))
print(max(course))

#for loop
for subject in course:
    print(subject)
for index, subject in enumerate (course):          #enumerate() is liye use hota hai jab loop ke sath index (position)
    print(index, subject)
print('...........................')


for i in range(0,6):
    print(f'NO :{i}')
print('...........................')


for subject in course:
    if subject =='literatre':
        break
    print(subject)
print('...........................')



#sets

sub1= {'lm','vm','rg','xi'}
sub2= {'fg','pe','xi'}

print(sub1.difference(sub2))
print(sub1.intersection(sub2))
print(sub1.union(sub2))



# dictionary      changeable and no duplicate
#   key:value pair   mean a word (small) is key and its meanng is value (little)

marks = {"Ali": 80, "Sara": 90, "Ahmed": 75, "Hira": 90}
print(marks)


print(marks.get('Sara'))
print(marks.get('zain', 'not found'))
marks['zain']='34'
print(marks.get('zain', 'not found'))


marks.update( {"Ali": 83, "Sara": 96, "Alina": 75, "Hira": 90})
print(marks)
del marks['Hira']
print(marks)


synonyms = {
    "happy": ["glad", "joyful", "cheerful"],
    "big": ["large", "huge", "giant"],
    "fast": ["quick", "rapid", "speedy"]
}

print(synonyms["happy"])

print (synonyms.keys())
print (synonyms.values())
print (synonyms.items())