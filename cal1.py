# Function to convert Celsius to Fahrenheit
def cel_to_fah(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Function to convert Fahrenheit to Celsius
def fah_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Main function to run the temperature converter program
def main():
    while True:
        print("Select an option:")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("E. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            result = cel_to_fah(celsius)
            print(f"The converted value is {result} Fahrenheit")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            result = fah_to_cel(fahrenheit)
            print(f"The converted value is {result} Celsius")
        elif choice.upper() == 'E':
            break
        else:
            print("Invalid input. Option is only 1, 2, or E. Please try again")

if __name__ == "__main__":
    main()
