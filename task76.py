# Task 76
# Write a function called "is_sorted" that takes a list of numbers as an argument and returns True if the list is sorted in ascending order, False otherwise.
# Function to check if a list is sorted in ascending order
def is_sorted(num_list):
    for i in range(1, len(num_list)):
        if num_list[i] < num_list[i - 1]:
            return False
    return True

# Example usage:
numbers = [1, 2, 3, 5, 7]
result = is_sorted(numbers)

print(result)
