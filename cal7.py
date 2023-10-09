# Open the file in write mode and create it if it doesn't exist
with open("output.txt", "w") as file:
    # Write values from 1 to 100 to the file, each on a new line
    for i in range(1, 101):
        file.write(str(i) + "\n")

print("Values from 1 to 100 have been written to 'output.txt'.")
