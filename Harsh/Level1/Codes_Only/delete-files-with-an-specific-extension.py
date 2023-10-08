import os

folder_path = "Level1-data"
extension_to_delete = ".pub.nc.gz"

# Get a list of all files in the folder
files_in_folder = os.listdir(folder_path)

# Iterate through the files and delete files with the specified extension
for file_name in files_in_folder:
    if file_name.endswith(extension_to_delete):
        file_path = os.path.join(folder_path, file_name)
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except OSError as e:
            print(f"Error: {file_path} - {e}")

print("Deletion completed.")
