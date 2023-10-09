# Task 46
# Define a variable called "user_number" and get the number from user
# Calculate the factorial for the user_number given by the user
# Display the factorial at the end
# NOTE: USE WHILE LOOP
# Get the user's number as input
user_input = input("Please enter a number: ")

# Convert the user input to an integer
user_number = int(user_input)

# Initialize a variable to store the factorial
factorial = 1

# Check if the input number is negative
if user_number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate the factorial using a while loop
    while user_number > 0:
        factorial *= user_number
        user_number -= 1

    # Display the factorial
    print("Factorial:", factorial)
