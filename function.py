#type of function are 2
#1. built in function
#2. user defined function
#example of in built function
print("hello world")

#example of user defined function
def my_function():
    print("hello world")
    my_function()
    
 # how to perform calculation within function   

def calculation():
    a=10
    b=20
    c=a+b
    print(c)
calculation()

#how to return any operation frim function
def returningFunction():
    num1 = 80 
    num2 = 200
    return num1+num2
return_data = returningFunction()
print(return_data)

#how to send parameter as an argument of function and perform operation
def parameterfunction(num1,num2,num3):
    print(num1)
    print(num2)
    print(num3)
#sending parameter to function
num1 =input("enter the number 1:")
parameterfunction(10,20,30,)

#how to perform parameter operation inside function using parameters
def paraFunction(naming,year):
    print ("the user name is:",naming)
    print("The user age is")
    current_year=2024
    real_age=current_year-int(year)
    print("the user age is:",real_age)
   
    

name =input("enter your name :")
age=input("enter your Date of birth id AD:")
paraFunction(name,age) #function call or sending parameter

#how to handle arbitary arguments
def arbitaryFunction(*args):
    selected_users =['ram','shyam']
    print(args)
    for i in args :
        print(i)
    if i in selected_users:
     print("selected user argument found",i)
arbitaryFunction('ram',"shyam",'sita','gita','ramita')

#how to handle key words argument
def keyWordFunction(**kwargs):
    #it is distanary form
    print (kwargs)
keyWordFunction(name="ram",age=20,city="Kathmandu",country="Nepal")

#default value function
def defaultFunction(name="ram",age=20):
    print("your name is:",name)
    print("your age is:",age)
defaultFunction()
defaultFunction('Gautam',21)

#how to define and acess global variables
street ="jorpati"
def function1():
    street="Chabahil"
    print("the street name is:",street)
function1()
print("the street name is:",street)

    





    
    

