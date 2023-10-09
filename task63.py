# Task 63
# Get three user input of three numbers and store that value in an array called “user_inputs”
# Google “array methods in python” to see how to add values to an array 
# Write a function called "is_even" that takes in the user_inputs array as an argument and displays which numbers are even and which are odd.
# Example: 
# is_even([1,2,5]) will display the output as
# 1 is odd
# 2 is even
# 5 is odd 

# Function to check if a number is even and display the result
def is_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")

# Get three user inputs and store them in a list called "user_inputs"
user_inputs = []
for i in range(3):
    user_input = int(input(f"Enter number {i + 1}: "))
    user_inputs.append(user_input)

# Call the "is_even" function with the "user_inputs" list
is_even(user_inputs)
