# github_test.py - Number Guessing Game

import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    print("=== Number Guessing Game ===")
    print("I have picked a number between 1 and 100. Try to guess it!")

    while True:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try higher.")
        elif guess > number:
            print("Too high! Try lower.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

    if attempts <= 5:
        print("Amazing! You're a mind reader.")
    elif attempts <= 10:
        print("Good job! Not bad at all.")
    else:
        print("Keep practicing!")

play_game()