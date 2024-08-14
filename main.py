import os
import argparse
from send2trash import send2trash

# Example: 'python main.py C:\Users\{User}\Desktop\ .txt delete' ----> Will permanently delete all text files on the Desktop


# Will recycle files
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


# Will permanently delete files
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


def main():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description="Handle files with a specific extension from a directory.")
    parser.add_argument("directory", type=str, help="Directory to clean")
    parser.add_argument("extension", type=str, help="File extension to handle (e.g., .txt)")
    parser.add_argument("action", type=str, choices=['delete', 'recycle'], help="Action to perform on the files (delete or recycle)")
    args = parser.parse_args()

    # Map each action argument to the respective function
    map_actions = {'delete': delete_files, 'recycle': recycle_files}

    # Call the function based on the input
    map_actions[args.action](args.directory, args.extension)


if __name__ == "__main__":
    main()
