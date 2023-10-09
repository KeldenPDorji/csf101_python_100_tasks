# Task 72
# Write a function called "calculate_discounted_price" that takes the original price and discount percentage as arguments and returns the discounted price.
# Write another function called "apply_discount" that takes the original price and a discount percentage as arguments and returns a string that states the discounted price.
# Then, write a third function called "shopping_cart" that calls the "apply_discount" function and prints the message with the discounted price.

# Test the function using:
# shopping_cart(50, 20)

# Function to calculate the discounted price
def calculate_discounted_price(original_price, discount_percentage):
    discount_amount = original_price * (discount_percentage / 100)
    discounted_price = original_price - discount_amount
    return discounted_price

# Function to apply discount and return a message without f-strings
def apply_discount(original_price, discount_percentage):
    discounted_price = calculate_discounted_price(original_price, discount_percentage)
    return "The discounted price is ${:.2f}".format(discounted_price)

# Function to print the message with the discounted price
def shopping_cart(original_price, discount_percentage):
    message = apply_discount(original_price, discount_percentage)
    print(message)

# Test the function with shopping_cart(50, 20)
shopping_cart(50, 20)
