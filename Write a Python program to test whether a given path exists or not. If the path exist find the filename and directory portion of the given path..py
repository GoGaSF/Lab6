import os

def analyze_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        directory_name, file_name = os.path.split(path)
        print(f"Directory: {directory_name}")
        print(f"Filename: {file_name}")
    else:
        print(f"The path '{path}' does not exist.")


specified_path = input("Enter the path: ")

analyze_path(specified_path)
