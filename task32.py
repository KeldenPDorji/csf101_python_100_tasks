# Task 32
# Define a variable called age and get it’s value from user input()
# Remember: the input() function returns a string, you need to convert it to an int
# Check if the age is above 18.
# If the age is above 22 (inclusive), display the output as: “I dont care”
# Or if the age is 18, display the output as “You pass”
# If the age is below 17, display the output as “you cannot touch beer”

# Get age as input from the user
user_input = input("Please enter your age: ")

# Convert the user input to an integer
age = int(user_input)

# Check the age and display the appropriate message
if age >= 22:
    print("I don't care")
elif age == 18:
    print("You pass")
else:
    print("You cannot touch beer")
