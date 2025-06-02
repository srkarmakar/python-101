# Correct Way Many Values to Multiple Variables
x,y,z = 1, 2, 3
print(x,y,z)
# Incorrect Way Many Values to Multiple Variables

# x,y,z,a = 1, 2, 3
# print(x)
# print(y)
# print(z)
# print(a)

# x,y,z = 1, 2, 3, 4
# print(x)
# print(y)
# print(z)

#Correct way to Upack Collection
numbers = [4,5,6]
x,y,z = numbers
print(x,y,z)

a,b,c = [7,8,9]
print(a,b,c)

d,e,f = [{'age': 10},{'age': 20},{'age': 30}]
print(d['age'])
print(d,e,f)

#Incorrect way to Upack Collection
# numbers = [4,5,6,9]
# x,y,z = numbers
# print(x)
# print(y)
# print(z)

# a,b,c, d = [7,8,9]
# print(a)
# print(b)
# print(c)

#Global Variable
global_variable = "Awsome"

def myFunction():
    global_variable = 'Fantastic'
    print("Python is " + global_variable + '.')

myFunction()

print("Python is " + global_variable + '.')


var = "Easy"
def myFunc():
    global var
    var = "Beautiful"
    print("Python is " + var)

myFunc()
print("Python is " + var)


def myFunc():
    global var
    var = "Beautiful"
    print("Python is " + var)

myFunc()
var = "Easy"
print("Python is " + var)

