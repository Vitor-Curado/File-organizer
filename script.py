import os

folder_address = input("Enter the folder address: ")

# Get the list of files in the folder
files = os.listdir(folder_address)

# Sort the files in ascending order
files.sort()

# Rename the files with an increment pattern
for i, file_name in enumerate(files):
    # Get the file extension
    file_extension = os.path.splitext(file_name)[1]
    
    # Generate the new file name with an increment pattern
    new_file_name = f"{i+1:03d}{file_extension}"
    
    # Rename the file
    os.rename(os.path.join(folder_address, file_name), os.path.join(folder_address, new_file_name))

print("Files renamed successfully!")