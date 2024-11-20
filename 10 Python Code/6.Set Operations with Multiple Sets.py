# Example 6: Set Operations with Multiple Sets
# Performing union, intersection, and symmetric difference with three sets.

# Example sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 6, 7, 8}

# Performing set operations
union_result = set1 | set2 | set3
intersection_result = set1 & set2 & set3
symmetric_difference_result = set1 ^ set2 ^ set3

print('Union of Sets:', union_result)
print('Intersection of Sets:', intersection_result)
print('Symmetric Difference of Sets:', symmetric_difference_result)