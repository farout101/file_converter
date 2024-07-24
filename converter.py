import os

def rename_jpeg_to_jpg(folder_path):
    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        # Check if the file has a .jpeg extension
        if filename.lower().endswith('.jpeg'):
            # Construct full file path
            old_file = os.path.join(folder_path, filename)
            # Create new file name with .jpg extension
            new_file = os.path.join(folder_path, filename[:-5] + '.jpg')
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} to {new_file}')

# Specify the path to the folder containing the JPEG files
folder_path = './for_ai'

# Call the function to rename files
rename_jpeg_to_jpg(folder_path)