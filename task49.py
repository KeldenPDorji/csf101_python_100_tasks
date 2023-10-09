# Task 49
# Do the same task as task 48 but USE FOR LOOP to achieve the same task
import random

# Generate a random secret number between 1 and 100 inclusive
secret_number = random.randint(1, 100)

# Define the maximum number of attempts
max_attempts = 10

# Use a for loop to allow the user to make a fixed number of guesses
for attempt in range(1, max_attempts + 1):
    # Get the user's guess as input
    user_guess = int(input(f"Attempt {attempt}/{max_attempts}: Guess the secret number (between 1 and 100): "))
    
    # Check if the guess is correct
    if user_guess == secret_number:
        print(f"Congratulations! You guessed the secret number {secret_number} correctly in {attempt} attempts.")
        break  # Exit the loop if the guess is correct
    elif user_guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

# If the user didn't guess the number in the allowed attempts
else:
    print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")
