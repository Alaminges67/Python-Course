# Example 1: Nested Lists Operations
# Working with nested lists by accessing elements, modifying values, and flattening the list.

# Example nested list
nested_list = [[1, 2, 3], [4, 5, [6, 7]], [8, 9]]

# Accessing a nested element
nested_element = nested_list[1][2][1]  # Accessing 7

# Modifying a nested element
nested_list[2][1] = 10  # Changing 9 to 10

# Flattening the nested list
flattened_list = [element for sublist in nested_list for item in sublist for element in (item if isinstance(item, list) else [item])]

print('Nested Element:', nested_element)
print('Modified Nested List:', nested_list)
print('Flattened List:', flattened_list)