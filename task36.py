# Task 36
# Define a variable called "score" and get its value from user input.
# Check if the score is greater than or equal to 90, display "A".
# If the score is between 80 and 89 (inclusive), display "B".
# If the score is between 70 and 79 (inclusive), display "C".
# If the score is between 60 and 69 (inclusive), display "D".
# If the score is less than 60, display "F".
# For any other input, display "Invalid score".

# Get the score as input from the user
user_input = input("Please enter your score: ")

# Convert the user input to an integer
score = int(user_input)

# Check the score and display the appropriate letter grade or "Invalid score"
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score < 60:
    print("F")
else:
    print("Invalid score")
