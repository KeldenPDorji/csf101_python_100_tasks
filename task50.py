# Task 50
# Get two numbers as user inputs from a user
# Store each of them in variable num1 and num2
# Calculate the sum of all numbers between num1 and num2
# Display the final sum as the output
# NOTE: USE WHILE LOOP

# Get two numbers as user inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Ensure num1 is smaller than num2
if num1 > num2:
    num1, num2 = num2, num1

# Initialize variables
current_number = num1
sum_of_numbers = 0

# Use a while loop to calculate the sum of numbers
while current_number <= num2:
    sum_of_numbers += current_number
    current_number += 1

# Display the final sum
print(f"The sum of numbers between {num1} and {num2} is {sum_of_numbers}.")
