import os
from PIL import Image

def convert_jpeg_to_jpg(folder_path):
    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        # Check if the file has a .jpeg extension
        if filename.lower().endswith('.jpeg'):
            # Construct full file path
            old_file = os.path.join(folder_path, filename)
            # Open the image file
            with Image.open(old_file) as img:
                # Create new file name with .jpg extension
                new_file = os.path.join(folder_path, filename[:-5] + '.jpg')
                # Save the image with .jpg extension
                img.save(new_file, 'JPEG')
                print(f'Converted: {old_file} to {new_file}')
            # Optionally, remove the old file
            # os.remove(old_file)

# Specify the path to the folder containing the JPEG files
folder_path = './for_ai'

# Call the function to convert files
convert_jpeg_to_jpg(folder_path)
