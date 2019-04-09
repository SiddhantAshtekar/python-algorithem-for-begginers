# Data stucture 
# List ---->this chapter 
# ordered collection of items
# you can store anything in lists int , float ,string 
numbers=[1,2,3,4]
print(numbers)
print(numbers[1])


words=['word1','word2','word3']
print(words)
print(words[:2])

mixed =[1,2,3,4,"five","six",2.3,None]
print(mixed[1:3])

mixed[1]='two'
print(mixed)

mixed[1:]="two"
print(mixed)

mixed[1:]=["three","four"]
print(mixed)