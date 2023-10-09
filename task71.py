# Task 71
# Write a function called "find_common_elements" that takes two lists as arguments and returns a new list containing the common elements between the two input lists.

# Example:
# find_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))  # Should print [3, 4, 5]

# Function to find common elements between two lists
def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2:
            common_elements.append(item)
    return common_elements

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements_list = find_common_elements(list1, list2)

print(common_elements_list)
