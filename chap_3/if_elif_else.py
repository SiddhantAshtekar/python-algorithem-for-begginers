age=int(input("Please input your age: "))
if age==0 or age<0:
    print("u can't watch")
elif 1<age<=3:
    print("Ticket prise is:Free")
elif 4<age<=10:
     print("Ticket prise is:150")
elif 11<age<=60:
     print("Ticket prise is:250")
else:
     print("Ticket prise is:200")