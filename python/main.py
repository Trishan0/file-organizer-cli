import shutil
import os
import json

# Define options for path selection
options = {'1': 'Current path - main.py stored path',
           '2': 'Specific Path'}

while True:
    # Display options
    for index, option in options.items():
        print(f"{index}: {option}")

    # Get user choice
    user_choice = input("Enter your choice (1 or 2): ")

    # Handle user choice
    if user_choice == '1':
        my_path = os.getcwd()  # Use the current working directory
        print(f"Using current path: {my_path}")
        break 
    elif user_choice == '2':
        my_path = input("Enter the absolute path you want to organize [/path/to/your/directory]: ")
        # Validate the path
        if os.path.isdir(my_path):
            print(f"Using specified path: {my_path}")
            break 
        else:
            print(f"The path '{my_path}' does not exist or is not a directory. Please try again.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Get all files in directory
print(f"Files in {my_path}: {os.listdir(my_path)}")


try:
    with open('categories.json', 'r') as file:
        categories = json.load(file)
except FileNotFoundError:
    print("The file 'categories.json' was not found.")
except json.JSONDecodeError:
    print("Error decoding JSON from the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
        
# Create folders if needed
for folder in categories.keys():
    folder_path = os.path.join(my_path, folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Created folder: {folder_path}")

# Move files to respective folders
for file in os.listdir(my_path):  # Loop through files in the directory
    file_path = os.path.join(my_path, file)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    file_ext = os.path.splitext(file)[1]

    for folder, extensions in categories.items():
        if file_ext in extensions:
            dest = os.path.join(my_path, folder, file)

            try:
                shutil.move(file_path, dest)
                print(f"Moved {file} → {folder}/")
            except Exception as e:
                print(f"Error moving {file}: {e}")
