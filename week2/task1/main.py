def sort_by_last_element(tuples):
    return sorted(tuples, key=lambda x: x[-1])


sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

result = sort_by_last_element(sample_list)

print("Original List:", sample_list)
print("Sorted List:", result)