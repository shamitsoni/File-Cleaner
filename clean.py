import os
from send2trash import send2trash


# Will send files to the recycle bin
def recycle_files(directory, extension):
    print('(INFO) Files will be moved to the recycle bin.')
    confirm = input('Enter (y) to continue or any key to exit: ')

    if confirm.strip().lower() == 'y':
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(root, file)
                    print(f"Moving file to recycle bin: {file_path}")
                    send2trash(file_path)
    return


# Will PERMANENTLY delete files
def delete_files(directory, extension):
    print('(WARNING) Files will NOT be recycled and will be PERMANENTLY deleted! Proceed with caution.')
    confirm = input('Enter (y) to continue or any key to exit: ')

    if confirm.strip().lower() == 'y':
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(root, file)
                    print(f"Removing file: {file_path}")
                    os.remove(file_path)
    return
