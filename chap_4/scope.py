x=5
def func():
    global x
    x=7
    return x
print(x)
print(func())
print(x)
