import os
import glob

# Define the folder to process
folder = "generated_functions"

# Find all .py files in the folder and subfolders
py_files = glob.glob(os.path.join(folder, "**", "*.py"), recursive=True)

# Loop through each file
for file_path in py_files:
    print(f"Processing {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace "null" with "None"
    new_content = content.replace("null", "None")
    
    # Write back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Replacement completed.")