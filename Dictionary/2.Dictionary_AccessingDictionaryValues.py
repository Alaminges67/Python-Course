# Example 2: Accessing Dictionary Values
# Values in a dictionary are accessed using their keys.
# If a key is not found, a KeyError will be raised unless you use the get() method, which returns None.

# Example dictionary
my_dict = {'name': 'Al_Amin', 'age': 24, 'city': 'Rajshahi'}

# Accessing values using keys
name = my_dict['name']
age = my_dict.get('age')

# Printing accessed values
print('Name:', name)
print('Age:', age)