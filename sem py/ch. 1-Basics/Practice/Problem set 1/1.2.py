import os

# Specify the directory (use '.' for current directory)
directory_path = '/Users' 

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)
