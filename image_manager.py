import os
from PIL import Image

def convert_images(folder_path, current_format, destination_format):
    """Converts images from current_format to destination_format in the specified folder."""
    current_format = current_format.lower()
    destination_format = destination_format.lower()
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(f'.{current_format}'):
            old_file = os.path.join(folder_path, filename)
            with Image.open(old_file) as img:
                new_file = os.path.join(folder_path, os.path.splitext(filename)[0] + f'.{destination_format}')
                img.save(new_file, destination_format.upper())
                print(f'Converted: {old_file} to {new_file}')
            # Optional: Remove the old file after conversion
            # os.remove(old_file)

def remove_files(folder_path, *file_formats):
    """Removes files with specified formats in the folder."""
    file_formats = tuple(fmt.lower() for fmt in file_formats)
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(tuple(f'.{fmt}' for fmt in file_formats)):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            print(f'Deleted: {file_path}')

def main():
    # Change the folder path to your target directory
    folder_path = './for_ai'
    
    # Display menu for user choice
    print("Choose an action:")
    print("1. Convert images")
    print("2. Remove files")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == '1':
        # Convert images
        current_format = input("Enter the current file format (e.g., png, jpg, jpeg): ").strip()
        destination_format = input("Enter the destination file format (e.g., png, jpg, jpeg): ").strip()
        convert_images(folder_path, current_format, destination_format)
        
    elif choice == '2':
        # Remove files
        remove_formats = input("Enter the file formats to remove (comma separated, e.g., jpg,jpeg,png): ").strip()
        if remove_formats:
            remove_files(folder_path, *remove_formats.split(','))
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
