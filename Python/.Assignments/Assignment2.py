def merge_and_sort(list1, list2):
    merged = list1 + list2
    no_duplicates = set(merged)
    return sorted(no_duplicates)

# Example usage:
print(merge_and_sort([3, 1, 4], [4, 2, 3]))
# Output: [1, 2, 3, 4]