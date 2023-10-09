# Task 47
# Do the same task as task 46 but USE FOR LOOP to achieve the same task
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
    # Calculate the factorial using a for loop
    for i in range(1, user_number + 1):
        factorial *= i

    # Display the factorial
    print("Factorial:", factorial)
