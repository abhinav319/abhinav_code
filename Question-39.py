''' Write a program able to play the "Guess the number"-game, where the number to be
guessed is randomly chosen between 1 and 20. (Source: http://inventwithpython.com)
This is how it should work when run in a terminal '''

from random import *

initial_num = randint(1,20)

print("Guess the random number between from 1 to 20")

while True:
    user_num = int(input("enter your guess: "))
    if( initial_num==user_num ):
        print("Good Job,you are right")
        break
    elif (initial_num>user_num):
        print("Your guess is too low",end='\n\n' )
    else:
        print("Your guess is too high",end='\n\n')
