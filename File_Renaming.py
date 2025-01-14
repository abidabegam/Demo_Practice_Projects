import os

def rename_files(folder_path, prefix):
    try:
        # Ensure the provided path is a folder
        if not os.path.isdir(folder_path):
            raise ValueError(f"The path provided is not a folder: {folder_path}")

        # List files in the directory
        files = os.listdir(folder_path)

        for count, filename in enumerate(files, start=1):
            ext = os.path.splitext(filename)[-1]  # Get the file extension
            new_name = f"{prefix}_{count}{ext}"
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
            print(f"Renamed: {filename} -> {new_name}")

        print("All files renamed successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Provide folder path and prefix
rename_files(r'C:\Users\abida\Downloads', 'Renamed_File')
