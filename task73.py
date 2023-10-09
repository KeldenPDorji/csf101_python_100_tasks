# Task 73
# Write a function called "calculate_hypotenuse" that takes the lengths of two sides of a right triangle as arguments and returns the length of the hypotenuse.
# Write another function called "triangle_info" that takes the lengths of two sides and calls the "calculate_hypotenuse" function to calculate and print the length of the hypotenuse.
# Display the output

# Test the function using:
# triangle_info(4, 5)
import math

# Function to calculate the hypotenuse of a right triangle
def calculate_hypotenuse(side1, side2):
    hypotenuse = math.sqrt(side1**2 + side2**2)
    return hypotenuse

# Function to calculate and print the length of the hypotenuse without f-strings
def triangle_info(side1, side2):
    hypotenuse = calculate_hypotenuse(side1, side2)
    print("The length of the hypotenuse is: {:.2f}".format(hypotenuse))

# Test the function with triangle_info(4, 5)
triangle_info(4, 5)
