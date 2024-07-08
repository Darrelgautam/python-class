# Variable
# Datatype
# Condition 
# Loop
# List
# Dictionary
# Set
# Funtion

# name = "Samira Rijal"
# print(type(name))
#How to identify the given number is odd or even
num1 = input("Enter a number:")
print(num1)
if int(num1)%2 == 0:
     if int(num1) < 100:
          print("Given number is less than 100")
     print("This number is even")
else:
     print("This number is odd")

#Loop
for i in range(1,1000):
     if i == 300:
          print("I have got 300")
          break # Loop will stop
     print(i)
num = 5
for i in range(1,num+1):
    for j in range(i):
       print("*", end="")
    print()
    
    #list in python
    # list1 = [1,2,3,4,5,6,7,8
    # list2 = ["Samira","Rijal","Kathmandu","Nep
   
    #string in list
fruit_list=['mango','apple','banana','grapes','orange']
print(fruit_list)
if 'mango'in fruit_list:
     print("mango is available in the list")
else:
    print("mango is not available in the list go home")
    new_fruits =input("enter new fruits bought in department :")
    fruit_list.append(new_fruits)
    print("fruit list after adding new item")
    print(fruit_list)
    