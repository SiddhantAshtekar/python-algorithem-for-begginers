#function practice
# def a(name):
#     return name[-1]

# nam=input("Enter your name")
# print(a(nam))



n=int(input("Enter the number"))
def odd_even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(odd_even(n))

def b(n):
    return n%2==0
print(b(n))

def a(n):
    if n%2==0:
        return True
    return False
print(a(n))
def s():
    return 'Have a nice Day'
print(s())