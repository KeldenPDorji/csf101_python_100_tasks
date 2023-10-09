# Task 67
# Write a function called "power" that takes two numbers as arguments, base and exponent, and returns base raised to the power of exponent.

# Function to calculate the power of a number
def power(base, exponent):
    result = base ** exponent
    return result

# Example usage:
base_value = 2
exponent_value = 3
result_value = power(base_value, exponent_value)

print(f"{base_value} raised to the power of {exponent_value} is: {result_value}")
