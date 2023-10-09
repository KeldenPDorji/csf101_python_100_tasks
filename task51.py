# Task 51
# Do the same task as task 50 but USE FOR LOOP to achieve the same task
# Get two numbers as user inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Ensure num1 is smaller than num2
if num1 > num2:
    num1, num2 = num2, num1

# Initialize a variable to store the sum of numbers
sum_of_numbers = 0

# Use a for loop to calculate the sum of numbers
for current_number in range(num1, num2 + 1):
    sum_of_numbers += current_number

# Display the final sum
print(f"The sum of numbers between {num1} and {num2} is {sum_of_numbers}.")
