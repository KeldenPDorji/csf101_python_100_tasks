# Task 44
# Define a variable called "user_name" and get the name from user
# Count the number of vowels occuring in the name
# Display the amount of vowels in the output
# NOTE: USE WHILE LOOP
# Get the user's name as input
user_name = input("Please enter your name: ")

# Initialize a counter for vowels
vowel_count = 0

# Define a set of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}

# Initialize a counter for the character position
count = 0

# Use a while loop to count the vowels in the user_name
while count < len(user_name):
    if user_name[count].lower() in vowels:
        vowel_count += 1
    count += 1

# Display the number of vowels
print("Number of vowels in the name:", vowel_count)
