def is_palindrom(name):
    name1=name[-1::-1]
    if name1==name:
        return True
    return False
def pal(word):
    return word==word[::-1]

print(is_palindrom("siddhant"))
print(is_palindrom("nayan"))
print(pal("siddhant"))
print(pal("nayan"))