# Task 48
# Write a program that asks the user to guess a secret number (e.g., 42).
# The secret is a random number between 1 to 100 inclusive
# Keep asking for guesses until the user guesses the correct number.
# Provide feedback such as "Too high" or "Too low" after each guess.
# NOTE: USE WHILE LOOP

import random

# Generate a random secret number between 1 and 100 inclusive
secret_number = random.randint(1, 100)

# Initialize a variable to keep track of the number of attempts
attempts = 0

# Use a while loop to repeatedly ask for guesses
while True:
    # Get the user's guess as input
    user_guess = int(input("Guess the secret number (between 1 and 100): "))
    
    # Increment the number of attempts
    attempts += 1

    # Check if the guess is correct
    if user_guess == secret_number:
        print(f"Congratulations! You guessed the secret number {secret_number} correctly in {attempts} attempts.")
        break  # Exit the loop if the guess is correct
    elif user_guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
