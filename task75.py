# Task 75
# Write a function called "find_longest_word" that takes a string as an argument and returns the longest word in the string.
# Assume that words in the string are separated by spaces, and there are no punctuation marks.

# Function to find the longest word in a string
def find_longest_word(input_string):
    words = input_string.split()  # Split the string into words
    longest_word = ""
    
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word

# Example usage:
input_string = "Write a function called find_longest_word"
result_word = find_longest_word(input_string)

print(result_word)
