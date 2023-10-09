# Task 33
# Define a variable called "grade" and get its value from user input.
# Check if the grade is greater than or equal to 90, display "A".
# If the grade is between 80 and 89 (inclusive), display "B".
# If the grade is between 70 and 79 (inclusive), display "C".
# If the grade is less than 70, display "F".

# Get the grade as input from the user
user_input = input("Please enter your grade: ")

# Convert the user input to an integer
grade = int(user_input)

# Check the grade and display the appropriate letter grade
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")
