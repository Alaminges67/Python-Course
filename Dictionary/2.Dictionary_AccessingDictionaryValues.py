# Example 2: Accessing Dictionary Values
# Values in a dictionary are accessed using their keys.
# If a key is not found, a KeyError will be raised unless you use the get() method, which returns None.

# Example dictionary
my_dict = {'student_name': 'Al_Amin', 'age': 24, 'roll': 102}

# Accessing values using keys
name = my_dict['student_name']
age = my_dict.get('age')

# Printing accessed values
print('Name:', name)
print('Age:', age)