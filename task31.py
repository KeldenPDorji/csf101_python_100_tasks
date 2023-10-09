# Task 31
# Define a variable called age and get it’s value from user input()
# Remember: the input() function returns a string, you need to convert it to an int
# Check if the age is above 18.
# If the age is above 18 (inclusive), display the output as: “You can drink”
# If the age is below 18, display the output as “Please grow older”

# Get age as input from the user
user_input = input("Please enter your age: ")

# Convert the user input to an integer
age = int(user_input)

# Check if the age is above 18
if age >= 18:
    print("You can drink")
else:
    print("Please grow older")
