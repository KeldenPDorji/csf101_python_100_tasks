# Task 40
# Define a variable called "no_of_times" and get the number from user
# Display “hi I am at Gedu” that many times as the user mentioned.
# NOTE: USE WHILE LOOP
# Get the number of times from the user
user_input = input("Please enter the number of times to display the message: ")

# Convert the user input to an integer
no_of_times = int(user_input)

# Initialize a counter
count = 0

# Use a while loop to display the message that many times
while count < no_of_times:
    print("hi I am at Gedu")
    count += 1
