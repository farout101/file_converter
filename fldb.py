import os
import shutil

def create_folders_for_batches(folder_path, batch_size=15):
    """Groups files into subfolders with a specified batch size."""
    os.makedirs(folder_path, exist_ok=True)

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    files.sort()

    batch_number = 1
    for i in range(0, len(files), batch_size):
        batch_folder = os.path.join(folder_path, f'batch_{batch_number}')
        os.makedirs(batch_folder, exist_ok=True)

        current_batch = files[i:i + batch_size]

        for file_name in current_batch:
            source_file = os.path.join(folder_path, file_name)
            destination_file = os.path.join(batch_folder, file_name)
            
            shutil.move(source_file, destination_file)
        
        batch_number += 1

    print(f'Files have been grouped into batches of {batch_size}.')

def main():
    folder_path = './for_ai'
    
    batch_size = int(input("Enter the batch size: "))
    
    create_folders_for_batches(folder_path, batch_size=batch_size)

if __name__ == "__main__":
    main()
