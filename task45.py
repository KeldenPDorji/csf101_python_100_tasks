# Task 45
# Do the same task as task 44 but USE FOR LOOP to achieve the same task
# Get the user's name as input
user_name = input("Please enter your name: ")

# Initialize a counter for vowels
vowel_count = 0

# Define a set of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}

# Use a for loop to count the vowels in the user_name
for char in user_name:
    if char.lower() in vowels:
        vowel_count += 1

# Display the number of vowels
print("Number of vowels in the name:", vowel_count)
