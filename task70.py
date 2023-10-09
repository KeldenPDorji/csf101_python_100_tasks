# Task 70
# Write a function called "multiply_lists" that takes two lists of equal length as arguments and returns a new list where each element is the product of the corresponding elements from the input lists.
# Example:
# List1 = [1,2,3]
# List2 = [4,5,6]
# multiply_lists(List1, List2))  Should print [4, 10, 18]

# Function to multiply two lists element-wise
def multiply_lists(list1, list2):
    if len(list1) != len(list2):
        return None  # Return None if the lists are not of equal length
    
    result = []
    for i in range(len(list1)):
        result.append(list1[i] * list2[i])
    
    return result

# Example usage:
List1 = [1, 2, 3]
List2 = [4, 5, 6]
result_list = multiply_lists(List1, List2)

if result_list is not None:
    print(result_list)
else:
    print("Lists are not of equal length.")
