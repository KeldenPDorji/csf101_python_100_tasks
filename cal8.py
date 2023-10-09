# Read the contents of "output.txt" and filter even numbers
with open("output.txt", "r") as input_file:
    lines = input_file.readlines()
    even_numbers = [line.strip() for line in lines if int(line.strip()) % 2 == 0]

# Write even numbers to "output1.txt"
with open("output1.txt", "w") as output_file:
    for even_number in even_numbers:
        output_file.write(even_number + "\n")

print("Even numbers from 'output.txt' have been written to 'output1.txt'.")

