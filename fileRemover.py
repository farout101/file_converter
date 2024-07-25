import os

def delete_jpeg_jpg_files(folder_path):
    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        # Check if the file has a .jpeg, .jpg, or .JPG extension
        if filename.lower().endswith(('.jpeg', '.jpg', '.jpg')):
            # Construct full file path
            file_path = os.path.join(folder_path, filename)
            # Remove the file
            os.remove(file_path)
            print(f'Deleted: {file_path}')

# Specify the path to the folder containing the image files
folder_path = './for_ai'

# Call the function to delete files
delete_jpeg_jpg_files(folder_path)
