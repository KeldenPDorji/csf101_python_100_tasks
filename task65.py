# Task 65
# Write a function called "reverse_string" that takes a string as an argument and returns the reverse of the string.

# Function to reverse a string
def reverse_string(input_string):
    return input_string[::-1]

# Example usage:
original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print(f"Original String: {original_string}")
print(f"Reversed String: {reversed_string}")
