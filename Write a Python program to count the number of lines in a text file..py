def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        return -1
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return -1


filename = input("Enter the path to the text file: ")

line_count = count_lines(filename)
if line_count != -1:
    print(f"The file '{filename}' contains {line_count} lines.")
