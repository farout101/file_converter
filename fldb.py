import os
import shutil

def create_folders_for_batches(folder_path, batch_size=15):
    """Groups files into subfolders with a specified batch size."""
    # Ensure the target folder exists
    os.makedirs(folder_path, exist_ok=True)

    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Sort the files to ensure consistent grouping
    files.sort()

    batch_number = 1
    for i in range(0, len(files), batch_size):
        # Create a new subfolder for this batch
        batch_folder = os.path.join(folder_path, f'batch_{batch_number}')
        os.makedirs(batch_folder, exist_ok=True)

        # Get the current batch of files
        current_batch = files[i:i + batch_size]

        for file_name in current_batch:
            source_file = os.path.join(folder_path, file_name)
            destination_file = os.path.join(batch_folder, file_name)
            
            # Move the file to the batch folder
            shutil.move(source_file, destination_file)
        
        batch_number += 1

    print(f'Files have been grouped into batches of {batch_size}.')

def main():
    # Change the folder path to your target directory
    folder_path = './for_ai'
    
    # Get batch size from the user
    batch_size = int(input("Enter the batch size: "))
    
    # Group files into subfolders with the specified number of files each
    create_folders_for_batches(folder_path, batch_size=batch_size)

if __name__ == "__main__":
    main()
