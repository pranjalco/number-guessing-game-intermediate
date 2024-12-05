import art
import random
from how_to_play import *

"""
# Project 9: Number Guessing Project
## Description:
A fun and interactive number-guessing game where the player attempts to guess a randomly generated number within 
a specified range. The game offers two difficulty levels—Easy and Hard—each with a different number of attempts.

### Features:
- Random number generation within a range (1 to 100).
- Two difficulty levels: Easy (10 attempts) and Hard (5 attempts).
- User-friendly inputs with error handling for invalid guesses.
- Feedback provided for each guess (e.g., too high, too low).
- Modular design with separate functions for key tasks.
- A welcoming and interactive interface with clear instructions.

# Level: Intermediate
Author: Pranjal Sarnaik
Date: 2024-12-05
"""


def add_blank_line():
    """This function is used to add a new blank line in the program"""
    print("")


def user_guess():
    """This function asks user to guess number and return the number as output"""
    while True:
        try:
            guess = int(input("Make a guess: "))
            return guess
        except ValueError:
            print("Error: please enter integer value between 1 and 100.")


def easy():
    """When user choose 'easy' as difficulty level then this function gets called with 10 attempts to guess a number"""
    attempts = 10
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess a number.")
        guessed_number = user_guess()
        attempts -= 1
        if number_to_guess > guessed_number:
            print("Too low")
            print("Please try again")
            add_blank_line()
        elif number_to_guess < guessed_number:
            print("Too high")
            print("Please try again")
            add_blank_line()
        else:
            add_blank_line()
            print(f"You guessed it right! The number is {guessed_number}")
            break

        if attempts == 0:
            return attempts


def hard():
    """When user choose 'hard' as difficulty level then this function gets called with 5 attempts to guess a number"""
    attempts = 5
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess a number.")
        guessed_number = user_guess()
        attempts -= 1
        if number_to_guess > guessed_number:
            print("Too low")
            print("Please try again")
            add_blank_line()
        elif number_to_guess < guessed_number:
            print("Too high")
            print("Please try again")
            add_blank_line()
        else:
            add_blank_line()
            print(f"You guessed it right! The number is {guessed_number}")
            break

        if attempts == 0:
            return attempts


print(instructions)
print(art.logo)

print("Welcome to the Number guessing Game!")

number_to_guess = random.randint(1, 100)
print("I am thinking of a number between 1 and 100.")
add_blank_line()

on = False
while not on:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    add_blank_line()
    if difficulty == 'easy':
        attempt_number = easy()
        on = True
    elif difficulty == 'hard':
        attempt_number = hard()
        on = True
    else:
        print(f"Please type 'easy' or 'hard', the input '{difficulty}' which you have provided is wrong.")

add_blank_line()

# In case when user lose then below code will tell the answer to the user.
if attempt_number == 0:
    print(f"The number to guess is {number_to_guess}, Best of luck for next time!")
my_name()
