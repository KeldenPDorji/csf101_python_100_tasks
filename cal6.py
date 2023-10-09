import os

# Function to search for a file named "secret.txt" in a directory and its subdirectories
def find_secret_file(directory):
    for root, dirs, files in os.walk(directory):
        if "secret.txt" in files:
            secret_file_path = os.path.join(root, "secret.txt")
            with open(secret_file_path, "r") as secret_file:
                contents = secret_file.read()
            return contents
    return None

# Main function
def main():
    folder_path = input("Enter the folder path to search: ")
    secret_contents = find_secret_file(folder_path)

    if secret_contents is not None:
        print("Contents of secret.txt:")
        print(secret_contents)
    else:
        print("File 'secret.txt' not found in the specified folder and its subfolders.")

if __name__ == "__main__":
    main()

