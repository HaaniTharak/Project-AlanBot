from collections import Counter

def append_most_common(lst):
    counter = Counter(lst)
    
    # Get the most common element
    most_common_element = counter.most_common(1)[0][0]

    new_list = []
    new_list.append(most_common_element)

    return new_list

# Test case
input_list = [3, 7, 11, 15, 3, 7, 3, 11, 3]
result = append_most_common(input_list)
print("Most common element appended to a new list:", result)