# Task 42
# Define a variable called "user_name" and get the name from user
# Check if there is a vowel in “user_name”; vowels: ‘a, e, i, o, u”
# If yes display True, else display False
# NOTE: USE WHILE LOOP

# Get the user's name as input
user_name = input("Please enter your name: ")

# Initialize a flag variable to check for vowels
has_vowel = False

# Define a set of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}

# Initialize a counter
count = 0

# Use a while loop to check for vowels in the user_name
while count < len(user_name):
    if user_name[count].lower() in vowels:
        has_vowel = True
        break  # Exit the loop as soon as a vowel is found
    count += 1

# Display the result
print(has_vowel)
