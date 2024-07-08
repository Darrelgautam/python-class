import Calculate
import odd_even

print("\t welcome here please select your option")
print("\t choose 1 for odd even and 2 for calculation")

choosen_opt=input("enter your option: ")

if choosen_opt=='1':
    num=int(input("Enter number to find odd even: "))
    odd_even_result=odd_even.findOddEven(num)
    if odd_even_result:
        print("number is even")
    else:
        print("number is odd")
elif choosen_opt=='2':
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    sum_data=Calculate.calc(num1, num2)
    print("sum of two number is: ",sum_data)
else:
    print("invalid option")