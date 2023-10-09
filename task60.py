# Task 60
# Write a function called "is_even" that takes an integer as an argument and returns True if it's even, False otherwise.
# Call the function and display the output for is_even(6)
# Define the "is_even" function
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Call the "is_even" function with an argument of 6 and display the output
result = is_even(6)
print(result)
