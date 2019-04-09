def scl(l):
    c=0
    for i in l:
        if type(i) == list:
            c+=1
    return c
mixed=[1,2,3,[1,7.9],["sid",2.0]]
print(scl(mixed))