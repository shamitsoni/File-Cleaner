import os
import shutil


# Will move files from source to destination
def move_files(directory, extensions, destination):
    print('(INFO) Files will be moved to the specified destination.')
    confirm = input('Enter (y) to continue or any key to exit: ')

    if confirm.strip().lower() == 'y':
        for root, dirs, files in os.walk(directory):
            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    file_path = os.path.join(root, file)
                    dest_path = os.path.join(destination, file)
                    print(f"Moving file to: {dest_path}")
                    shutil.move(str(file_path), str(dest_path))
    return


# Will copy files from source to destination
def copy_files(directory, extensions, destination):
    print('(INFO) Files will be copied to the specified destination.')
    confirm = input('Enter (y) to continue or any key to exit: ')

    if confirm.strip().lower() == 'y':
        for root, dirs, files in os.walk(directory):
            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    file_path = os.path.join(root, file)
                    dest_path = os.path.join(destination, file)
                    print(f"Copying file to: {dest_path}")
                    shutil.copy(str(file_path), str(dest_path))
    return
