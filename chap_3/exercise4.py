num1=input("enter the number more than one digits")
i=0
sum=0
while i<len(num1):
    sum+=int(num1[i])
    i+=1
print(f"sum:{sum}")
