def greatest_num(a,b):
    if a>b:
        return a
    else:
        return b
num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
greatest=greatest_num(num1,num2)
print(f"{greatest} is greatest number")