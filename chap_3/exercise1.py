winning_number=12
guessed_number=int(input("Guess the winning number"))
if winning_number==guessed_number:
    print("You Won!!")
else:
    if winning_number>guessed_number:
        print("too low")
    else:
        print("too high")