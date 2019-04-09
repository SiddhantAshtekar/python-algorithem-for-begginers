import random
Winning_number=43
Guessed_number=int(input("Guess the Winning_number"))
a=0
for Winning_number in range(1,101):
    if Winning_number==Guessed_number:
        print("you win!!!")
    else:
        if Winning_number>Guessed_number:
            print("too low")
        else:
            print("too high")
    a+=1
    print(f"intut number {a} times")
