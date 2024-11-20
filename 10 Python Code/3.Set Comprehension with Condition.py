# Example 3: Set Comprehension with Condition
# Creating a set using comprehension with a condition to filter specific elements.

# Example list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Creating a set of even numbers
even_set = {num for num in numbers if num % 2 == 0}

print('Set of Even Numbers:', even_set)