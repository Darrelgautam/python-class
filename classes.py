import math

# Define classes
class MyCollege:
    x = 'Ram'

obj = MyCollege()
print(obj.x)

class ClassWithCons:
    def __init__(self):
        print('This is being called when initializing object')

obj1 = ClassWithCons()

class ClassWithData:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        print(self.name)
        print(self.address)

obj2 = ClassWithData('Ram', 'Dang')

class MultipleFunctionClass:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def printName(self):
        print(self.name)

    def printAge(self):
        print(self.age)

    def printAddress(self):
        print(self.address)

obj3 = MultipleFunctionClass('Kunjan', 18, 'Bhaktapur')
obj3.printName()
obj3.printAge()
obj3.printAddress()

# Calculator class
class Calculator:
    def __init__(self, num):
        self.number = num
        self.amt = 0
        self.splited_data = None

    def sumFunction(self):
        self.amt = int(self.splited_data[0]) + int(self.splited_data[1])
        print(self.amt)

    def subFunction(self):
        self.amt = int(self.splited_data[0]) - int(self.splited_data[1])
        print(self.amt)

    def mulFunction(self):
        self.amt = int(self.splited_data[0]) * int(self.splited_data[1])
        print(self.amt)

    def divFunction(self):
        self.amt = int(self.splited_data[0]) / int(self.splited_data[1])
        print(self.amt)

    def splitFunction(self):
        if '+' in self.number:
            self.splited_data = self.number.split('+')
            self.sumFunction()
        elif '-' in self.number:
            self.splited_data = self.number.split('-')
            self.subFunction()
        elif '*' in self.number:
            self.splited_data = self.number.split('*')
            self.mulFunction()
        elif '/' in self.number:
            self.splited_data = self.number.split('/')
            self.divFunction()

# Calculator usage loop
while True:
    input_number = input("Enter the expression (or type 'exit' to quit): ")
    if input_number == 'exit':
        break
    else:
        calc = Calculator(input_number)
        calc.splitFunction()

# Inheritance example
class ParentClass:
    def __init__(self, name):
        self.name = name
        self.class_type = 'BIT'
        print('This is parent class')

    def printName(self):
        print(self.name)

class ChildClass(ParentClass):
    pass

obj1 = ChildClass('Ashim')
print(obj1.class_type)
obj1.printName()

# Another inheritance example
class Parent2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('This is parent class')
        print(f"{self.name} {self.age}")

class Child2(Parent2):
    def printNumber(self):
        print('This is number')

obj3 = Child2('Bibek', 'Bouddha')
obj4 = Child2('Ram', 'Sindhuli')
obj5 = Child2('Sam', 'Chabahil')

# Using math module
print(math.sqrt(300))