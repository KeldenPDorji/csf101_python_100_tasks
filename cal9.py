# Read the contents of "output1.txt" and calculate the sum of all numbers
with open("output1.txt", "r") as input_file:
    lines = input_file.readlines()
    numbers = [int(line.strip()) for line in lines]
    total_sum = sum(numbers)

# Write the sum to "output3.txt"
with open("output3.txt", "w") as output_file:
    output_file.write(str(total_sum))

print(f"The sum of numbers in 'output1.txt' is {total_sum} and has been written to 'output3.txt'.")

