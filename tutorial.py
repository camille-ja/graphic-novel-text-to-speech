print('Hello World')
print("Hello World!") #can use single or double quotes

#variables
price = 19.999 #don't need to declare type of variable
variable_name = 20 #use underline to separate words instead of uppercase
bool = True
print(variable_name + price)

#Reciving input
name = input("What's your name? ") #prints to console
print("Hello " + name + "!") #string concatination

#Type conversion
birth_year = input("Enter your birth year: ")
#age = 2024 - birth_year: crashes program bc birth_year = string
age = 2024 - int(birth_year) #float() <-double, #bool(), #str()
print(age)
first = input("First: ")
second = input("Second: ")
sum = float(first) + float(second)
print("Sum:", sum) #need a comma when printing numbers you don't want to add

first = float(input("First: "))
second = float(input("Second: "))
sum = first + second
print("Sum: " + str(sum))

#Strings
course = 'math 201'
print(course.upper() + " " + course.lower())
print(course.find('m'), course.find('M'), course.find('math'))
print(course.replace('math', 'bio')) #doesn't modify og string- strings in python are immutable
print('math' in course) #works the same as find but returns bool not index

#Arithmitic
print(19 / 2) #decimal
print(19 // 2) #integer
print(10 ** 3) #10^3
x = 10
x+=3
print(x)
y = 10 + 3 * 2
print(y) #PEMDAS
z = 3 > 2 #all comparisons (>= != ect) are same as java!
print(z)

#Logical Opperators
price = 25
print(price > 10 or price < 30)
price = 11
print(price < 10 or price > 30)
print(not price < 10)

#If Statements
temp = 4
if temp > 30: 
    print("it's a hot day! (celsius)")
    print("drink plenty of water")
elif temp > 20:
    print("nice day!")
elif temp > 10:
    print("chilly!")
else:
    print("cool day!")
print("done")

weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit == 'l' or unit == 'L':
    print("Weight in Kg: ", weight / 2.205)
elif unit.upper() == 'K':
    print("Weight in lbs: " + str(weight * 2.205))
else:
   print("wrong measurment system!")

#Loops
i = 1
while i <= 10: 
    print(i * '*') #will print astriks as many times as there's an i
    i+=1

while i <= 1_000: #_ is like a comma
    i+=1

#Lists
names = ["camille", "john", "bob", "mary"]
print(names, " ", names[0], names[-1], names[-2], names[-3])
names[1] = "jon"
print(names, names[0:2]) #end isn't inclusive
numbers = [1,2,3,4,5]
numbers.append(6)
numbers.insert(0,0)
numbers.remove(3)
print(numbers)
print(1 in numbers) #prints if 1 is in list
print(10 in numbers)
print(len(numbers)) #number of elements in list
numbers.clear()
print(numbers)

#Loops
numbers = [1,2,3,4,5]

#For loop
for i in numbers: #automatically incraments i
    print(i)

#While loop
i = 0
while i < len(numbers):
    print(numbers[i])
    i+=1

#Range function
nums = range(1,5) #range of 0-5 excluding 5
print(nums)
for number in nums:
    print(number)
nums = range(5,10,2) #increase by 2
print()
for number in nums:
    print(number)
print()
for number in range(5): #prints 0-4
    print(number)

#Tuples: like lists but are immutable
numbers = (1, 2, 3)
#numbers[0] = 10 #gives error- can't change!