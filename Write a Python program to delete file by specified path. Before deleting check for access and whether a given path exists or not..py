import os


def delete_file(path):
    try:

        if os.path.exists(path):
            print(f"The path '{path}' exists.")


            if os.access(path, os.F_OK):
                os.remove(path)
                print(f"File '{path}' deleted successfully.")
            else:
                print(f"File '{path}' is not accessible.")
        else:
            print(f"The path '{path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")



specified_path = input("Enter the path of the file you want to delete: ")

delete_file(specified_path)
