def fibonacci(number):
    a,b=0,1
    if number == 1:
        print(a)
    elif number == 2:
        print(a,b,end=" ")
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b,end=" ")
n=int(input("Enter the number"))
print(fibonacci(n))
