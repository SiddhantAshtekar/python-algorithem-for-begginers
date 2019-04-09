def cf(n):
    c={}
    for i in range(1,n+1):
        c[i]=i**3
    return c
n1=int(input("Enter the number"))
print(cf(n1))