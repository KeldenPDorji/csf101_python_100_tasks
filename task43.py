# Task 43
# Do the same task as task 42 but USE FOR LOOP to achieve the same task
# Get the user's name as input
user_name = input("Please enter your name: ")

# Initialize a flag variable to check for vowels
has_vowel = False

# Define a set of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}

# Use a for loop to check for vowels in the user_name
for char in user_name:
    if char.lower() in vowels:
        has_vowel = True
        break  # Exit the loop as soon as a vowel is found

# Display the result
print(has_vowel)
