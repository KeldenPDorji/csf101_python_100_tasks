# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Main function for the calculator program
def main():
    while True:
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("E. Exit")

        choice = input("Enter choice (1/2/3/4/E): ")

        if choice.upper() == 'E':
            break
        elif choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                print("Result: {:.2f}".format(result))
            elif choice == '2':
                result = subtract(num1, num2)
                print("Result: {:.2f}".format(result))
            elif choice == '3':
                result = multiply(num1, num2)
                print("Result: {:.2f}".format(result))
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print("Result: {:.2f}".format(result))
            else:
                print("Invalid input. Please try again.")
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
