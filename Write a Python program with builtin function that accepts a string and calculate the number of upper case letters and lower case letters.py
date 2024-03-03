def count_case_letters(string):
    uppercase_count = 0
    lowercase_count = 0

    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count

input_string = input("Enter a string: ")
uppercase, lowercase = count_case_letters(input_string)

print("Number of uppercase letters:", uppercase)
print("Number of lowercase letters:", lowercase)
