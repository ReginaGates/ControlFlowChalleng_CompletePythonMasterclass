#Complete Python Masterclass - Tim Buchalka & Jean-Paul Roberts
#Challenge - Program Flow While Loops

#Modified by Regina Gates

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}, or 0 to quit: ".format(highest))
guess = int(input())
if guess == answer:
    print("You got it first time")
else:
    while guess != answer:
        # Quit option
        if guess == 0:
            break
        elif guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than number
            print("Please guess lower")
        guess = int(input())
    else:
        print("Well done, you guessed it")
