import os

import argparse


def clean_files(directory, extension):
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
    parser = argparse.ArgumentParser(description="Clean files with a specific extension from a directory.")
    parser.add_argument("directory", type=str, help="Directory to clean")
    parser.add_argument("extension", type=str, help="File extension to remove (e.g., .txt)")

    args = parser.parse_args()

    clean_files(args.directory, args.extension)


if __name__ == "__main__":
    main()
