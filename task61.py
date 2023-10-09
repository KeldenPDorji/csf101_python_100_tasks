# Task 61
# Get user input of a number and store that value in a variable called “user_input” 
# Write a function called "is_even" that takes an integer as an argument and returns True if it's even, False otherwise.
# Call the function and display the output for is_even(6)

# Define the "is_even" function
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Get user input for a number and store it in the variable "user_input"
user_input = int(input("Enter a number: "))

# Call the "is_even" function with the user's input and display the output
result = is_even(user_input)
print(result)
