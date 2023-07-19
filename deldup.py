import os
import hashlib

def hash_file(file_path):
    # Generate a SHA-1 hash of the file's contents
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)  # Read file in 64kb chunks
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

def find_duplicate_files(root_folder):
    file_hashes = {}
    duplicate_files = []

    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = hash_file(file_path)

            if file_hash in file_hashes:
                duplicate_files.append(file_path)
            else:
                file_hashes[file_hash] = file_path

    return duplicate_files

def delete_duplicate_files(duplicate_files):
    for duplicate_file in duplicate_files:
        try:
            os.remove(duplicate_file)
            print(f"Deleted: {duplicate_file}")
        except Exception as e:
            print(f"Failed to delete {duplicate_file}: {e}")

if __name__ == "__main__":
    # Set the root folder where you want to search for duplicate files
    root_folder = "/home/red_x/test" # change this to the path to the folder where you want to delete duplicate files

    duplicate_files = find_duplicate_files(root_folder)

    if duplicate_files:
        print("Duplicate files found:")
        for file_path in duplicate_files:
            print(file_path)

        confirm_deletion = input("Do you want to delete these duplicate files? (yes/no): ").strip().lower()
        if confirm_deletion == "yes":
            delete_duplicate_files(duplicate_files)
        else:
            print("Duplicate files were not deleted.")
    else:
        print("No duplicate files found.")

