import string

def generate_text_files():

    for letter in string.ascii_uppercase:
        filename = letter + '.txt'
        with open(filename, 'w') as file:

            file.write(f"This is file {filename}\n")
        print(f"File {filename} created.")


generate_text_files()
