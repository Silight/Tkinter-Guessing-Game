__author__ = 'Andrew Edwards'
# Console Version of the guessing game.

from random import *

#Variables
number = randrange(50)
player_guess = 0
number_guesses = 0


def main_loop(number_guesses):
    while True:
        print("Take a guess")
        guess = int(input("> "))
        number_guesses += 1
        if guess == number:
            print("You got it in " + str(number_guesses) + " guesses!")
            break
        elif guess < number:
            print("Too Low")
        else:
            print("Too high")
        if number_guesses > 10:
            print("You used all your guesses.")
            print("The number I was thinking of is " + str(number))
            break

print("I'm thinking of a number between 0 and 50")
main_loop(number_guesses)
print("Thanks for Playing!")
