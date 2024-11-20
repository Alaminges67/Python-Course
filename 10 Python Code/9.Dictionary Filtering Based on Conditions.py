# Example 9: Dictionary Filtering Based on Conditions
# Filtering a dictionary to retain only key-value pairs that satisfy a condition.

# Example dictionary
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 95, 'David': 60}

# Filtering to retain scores >= 80
filtered_scores = {name: score for name, score in scores.items() if score >= 80}

print('Filtered Scores:', filtered_scores)