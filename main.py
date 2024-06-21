import os
import sys
import argparse


def find_duplicates_by_name_and_size(folder):
    # Initialize empty lists to store file information and duplicates
    files = []
    duplicates = []

    # Walk through the folder and gather file names, sizes, and paths
    for root, _, filenames in os.walk(folder):
        for filename in filenames:
            # Remove the extension from the filename
            new_filename = os.path.splitext(filename)[0]
            # Create the full file path
            filepath = os.path.join(root, filename)
            # Get the size of the file
            size = os.path.getsize(filepath)
            # Append the file details to the files list
            files.append((new_filename, size, filepath))

    # Check for duplicates by comparing file names and sizes
    for name1, size1, path1 in files:
        for name2, size2, path2 in files:
            # Compare file sizes and names to find duplicates
            if size1 == size2 and (name1 in name2) and (name1 != name2):
                # Print a message when a duplicate is found
                print(f'Duplicate found: {name1} and {name2}')
                # Add the duplicate file path to the duplicates list
                duplicates.append(path2)

    # Return the list of duplicate file paths
    return duplicates
def delete_duplicates(duplicates):
    for file in duplicates:
        os.remove(file)
        print(f'Deleted: {file}')
        #print(file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find and delete duplicate files in a folder.')
    parser.add_argument('folder', type=str, help='Path to the folder to check for duplicates.')
    parser.add_argument('--delete', action='store_true', help='Delete duplicate files.')

    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(f'Error: {args.folder} is not a valid directory.')
        sys.exit(1)

    duplicates = find_duplicates_by_name_and_size(args.folder)

    #Turn Duplicates into a set and back into a list in order to remove duplicates

    duplicates = list(set(duplicates))
    print(duplicates)
    if args.delete:
        delete_duplicates(duplicates)
