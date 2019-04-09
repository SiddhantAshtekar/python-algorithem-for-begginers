# word counter
def word_counter(a):
    c={}
    for i in a:
        c[i]=a.count(i)
    return c
string1=input("Enter the string")
print(word_counter(string1))