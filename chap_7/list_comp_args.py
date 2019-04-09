def a(n,*args):
    if args:
        return [i**n for i in args]
    else:
        "you didn't pass any args"
b=[]
print(a(3,(*b)))