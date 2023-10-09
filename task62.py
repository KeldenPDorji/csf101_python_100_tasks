# Task 62
# Get three user input of three numbers and store that value in an array called “user_inputs”
# Google “array methods in python” to see how to add values to an array 
# Write a function called "is_even" that takes in the user_inputs array as an argument and returns True if all of the numbers are even, False otherwise.

# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Get three user inputs and store them in a list called "user_inputs"
user_inputs = []
for i in range(3):
    user_input = int(input(f"Enter number {i + 1}: "))
    user_inputs.append(user_input)

# Function to check if all numbers in the list are even
def are_all_even(numbers):
    for number in numbers:
        if not is_even(number):
            return False
    return True

# Call the "are_all_even" function with the "user_inputs" list and display the output
result = are_all_even(user_inputs)

if result:
    print("All numbers are even.")
else:
    print("Not all numbers are even.")
