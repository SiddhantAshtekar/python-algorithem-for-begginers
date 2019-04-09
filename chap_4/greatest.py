def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
print(greatest(4,5,3))