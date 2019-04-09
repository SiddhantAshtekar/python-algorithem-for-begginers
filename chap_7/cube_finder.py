def cu(n):
    cu1={}
    for i in range(1,n+1):
        cu1[i]=i**3
    return cu1
a=int(input("Enter the number"))
print(cu(a))
