def all_elements_true(tuple_data):
    return all(tuple_data)


tuple1 = (True, True, True)
tuple2 = (True, False, True)

print(all_elements_true(tuple1))
print(all_elements_true(tuple2))
