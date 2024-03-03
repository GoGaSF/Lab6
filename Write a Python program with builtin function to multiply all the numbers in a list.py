from functools import reduce

def multiply_list(numbers):
    if not numbers:
        return None
    return reduce(lambda x, y: x * y, numbers)

numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print("Результат умножения всех чисел в списке:", result)
