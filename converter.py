import os
from PIL import Image

def convert_images_to_png(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpeg', '.jpg', '.JPG')):
            old_file = os.path.join(folder_path, filename)
            with Image.open(old_file) as img:
                new_file = os.path.join(folder_path, os.path.splitext(filename)[0] + '.png')
                img.save(new_file, 'PNG')
                print(f'Converted: {old_file} to {new_file}')
            # Optional
            # os.remove(old_file)

def delete_jpeg_jpg_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpeg', '.jpg', '.jpg')):
            # Construct full file path
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            print(f'Deleted: {file_path}')

# change the folder path
folder_path = './for_ai'

convert_images_to_png(folder_path)
# delete_jpeg_jpg_files(folder_path)