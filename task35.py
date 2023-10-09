# Task 35
# Define a variable called "day" and get its value from user input.
# Check if the day is "Monday", "Tuesday", "Wednesday", or "Thursday", display "Weekday".
# If the day is "Friday", display "TGIF".
# If the day is "Saturday" or "Sunday", display "Weekend".
# For any other input, display "Invalid input".
# Get the day as input from the user
day = input("Please enter the day: ")

# Check the day and display the appropriate status
if day in ["Monday", "Tuesday", "Wednesday", "Thursday"]:
    print("Weekday")
elif day == "Friday":
    print("TGIF")
elif day in ["Saturday", "Sunday"]:
    print("Weekend")
else:
    print("Invalid input")
