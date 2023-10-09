# Task 74
# Write a function called "reverse_words" that takes a string as an argument and returns a string where the words are reversed.
# For example, "Hello, world!" should become "olleH, dlrow!".
# Function to reverse the words in a string
def reverse_words(input_string):
    words = input_string.split()  # Split the string into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    return ' '.join(reversed_words)  # Join the reversed words back into a string

# Example usage:
input_string = "Hello, world!"
result_string = reverse_words(input_string)

print(result_string)
