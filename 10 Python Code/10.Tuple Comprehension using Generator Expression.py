# Example 10: Tuple Comprehension using Generator Expression
# Creating a tuple using a generator expression for elements that meet a condition.

# Example range of numbers
numbers = range(1, 11)

# Creating a tuple of squares of even numbers
even_squares = tuple(x**2 for x in numbers if x % 2 == 0)

print('Tuple of Even Squares:', even_squares)