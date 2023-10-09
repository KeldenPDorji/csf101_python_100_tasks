# Task 53
# Do the same task as task 52 but USE FOR LOOP to achieve the same task
# Get a number from the user
user_number = int(input("Enter a number: "))

# Use a for loop to display the multiplication table
for counter in range(1, 21):
    result = user_number * counter
    print(f"{user_number} x {counter} = {result}")
