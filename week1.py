#Finish the "Guess the Number" game, ensuring it handles valid input, gives appropriate hints, and stops when guessed.
import random
Number = random.randint(1, 10)
for i in range(10):
    if Number == 3:
        print("your Guess is correct")
        break
    elif Number > 3:
        print("Too high")
        Number = int(input("Guess a number between 1 and 10:" ))
    elif Number < 3 :
        print("Too Low")
        Number = int(input("Guess a number between 1 and 10:" ))
    else:
        print("Try again")
        Number = int(input("Guess a number between 1 and 10:" ))