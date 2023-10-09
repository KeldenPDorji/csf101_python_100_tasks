# Task 68
# Write a function called "capitalize_words" that takes a string as an argument and returns the string with each word capitalized.
# Example: 
# If input is “hello world”, the function should return “Hello World”

# Function to capitalize each word in a string
def capitalize_words(input_string):
    words = input_string.split()  # Split the string into words
    capitalized_words = [word.capitalize() for word in words]  # Capitalize each word
    return ' '.join(capitalized_words)  # Join the capitalized words back into a string

# Example usage:
input_string = "hello world"
result_string = capitalize_words(input_string)

print("Original String:", input_string)
print("Capitalized String:", result_string)
