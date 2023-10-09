# Task 37
# Define a variable called "month" and get its value from user input.
# Check if the month is "January", "February", "March", "April", or "May", display "Spring".
# If the month is "June", "July", "August", display "Summer".
# If the month is "September", "October", "November", display "Fall".
# If the month is "December", display "Winter".
# For any other input, display "Invalid month".
# Get the month as input from the user
month = input("Please enter the month: ")

# Check the month and display the appropriate season or "Invalid month"
if month in ["January", "February", "March", "April", "May"]:
    print("Spring")
elif month in ["June", "July", "August"]:
    print("Summer")
elif month in ["September", "October", "November"]:
    print("Fall")
elif month == "December":
    print("Winter")
else:
    print("Invalid month")
