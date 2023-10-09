# Task 52
# Get a number from the user
# Display the multiplication table of that number from 1 till 20
# NOTE: USE WHILE LOOP

# Get a number from the user
user_number = int(input("Enter a number: "))

# Initialize a counter for the multiplication table
counter = 1

# Use a while loop to display the multiplication table
while counter <= 20:
    result = user_number * counter
    print(f"{user_number} x {counter} = {result}")
    counter += 1
