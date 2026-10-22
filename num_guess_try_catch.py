#!/usr/bin/env python3
# Created by: Joyceline
# Created on: Oct 21 2026
# This program asks the user to guess a random number between 0 and 9 and checks if it is correct or not.
import random

rand_number = random.randint(0, 9)


def main():
    # Get the user's guess as a string(0 and 9)
    user_guess_as_string = input("Enter an integer: ")

    try:
        user_guess_as_int = int(user_guess_as_string)
        if user_guess_as_int == rand_number:
            print("you guessed it correctly!")
        else:
            print("you guessed it wrong!")
            print("The correct answer is {}".format(rand_number))
    except:
        print("{} is not a valid integer".format(user_guess_as_string))

    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
