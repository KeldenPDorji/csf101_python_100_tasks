# Task 69
# Write a function called "count_chars" that takes a string and a character as arguments and returns the number of times the character appears in the string.

# Function to count the number of times a character appears in a string
def count_chars(input_string, character):
    count = 0
    for char in input_string:
        if char == character:
            count += 1
    return count

# Example usage:
input_string = "hello world"
character_to_count = "o"
result_count = count_chars(input_string, character_to_count)

print("The character '{}' appears {} times in the string.".format(character_to_count, result_count))
