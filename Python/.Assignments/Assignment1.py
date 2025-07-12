def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage:
print(remove_duplicates([1, 2, 2, 3, 1, 4]))
# Output: [1, 2, 3, 4]