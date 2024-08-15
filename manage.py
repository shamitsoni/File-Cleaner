import os
import shutil


# Will move files from source to destination
def move_files(directory, extension, destination):
    print('(INFO) Files will be moved to the specified destination.')
    confirm = input('Enter (y) to continue or any key to exit: ')

    if confirm.strip().lower() == 'y':
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(root, file)
                    dest_path = os.path.join(destination, file)
                    print(f"Moving file to: {dest_path}")
                    shutil.move(file_path, dest_path)
    return
