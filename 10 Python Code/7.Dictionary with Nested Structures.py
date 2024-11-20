# Example 7: Dictionary with Nested Structures
# Accessing and modifying elements in a dictionary with nested structures.

# Example dictionary with nested structures
nested_dict = {
    'person': {
        'name': 'John',
        'details': {
            'age': 25,
            'city': 'New York',
            'skills': ['Python', 'Data Analysis']
        }
    }
}

# Accessing nested elements
city = nested_dict['person']['details']['city']

# Modifying a nested element
nested_dict['person']['details']['skills'].append('Machine Learning')

print('City:', city)
print('Updated Nested Dictionary:', nested_dict)