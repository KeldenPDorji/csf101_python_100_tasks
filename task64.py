# Task 64
# Write a function called "find_max" that takes a list of numbers as an argument and returns the maximum value in the list.

# Function to find the maximum value in a list of numbers
def find_max(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    
    max_value = numbers[0]  # Initialize max_value with the first element
    
    for number in numbers:
        if number > max_value:
            max_value = number  # Update max_value if a larger number is found
    
    return max_value

# Example usage:
numbers_list = [12, 45, 6, 78, 32, 9]
max_value = find_max(numbers_list)

if max_value is not None:
    print(f"The maximum value in the list is: {max_value}")
else:
    print("The list is empty.")
