# Example 5: List of Tuples to Dictionary
# Converting a list of tuples into a dictionary using a loop.

# Example list of tuples
tuple_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

# Converting to a dictionary
result_dict = {key: value for key, value in tuple_list}

print('Dictionary from List of Tuples:', result_dict)