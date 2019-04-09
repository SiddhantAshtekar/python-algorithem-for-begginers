import random
winning_number=random.randint(1,100)
guessing_number=int(input("Guess the number between 1 to 100:"))
guess=1
Game_over=False
while not Game_over:
    if guessing_number==winning_number:
        print(f"You Win !!! n u guess this in {guess} attempt")
        Game_over=True
    else:
        if guessing_number>winning_number:
            print("too high")
        else:
            print("too low")

        guess+=1
        guessing_number=int(input("guess again"))
