# Task 66
# Write a function called "calculate_average" that takes a list of numbers as an argument and returns the average of the numbers.
# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
numbers_list = [12, 45, 6, 78, 32, 9]
average_value = calculate_average(numbers_list)

if average_value is not None:
    print(f"The average of the numbers is: {average_value}")
else:
    print("The list is empty.")
