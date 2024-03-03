def write_list_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"Data has been written to '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


filename = input("Enter the filename to write the list to: ")


data_list = ['apple', 'banana', 'orange', 'grape']

write_list_to_file(filename, data_list)
