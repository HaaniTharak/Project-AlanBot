from collections import Counter

def removeDuplicates(lst, numCards):
    unique_values = []
    i = 0
    while i < len(lst):
        current_value = lst[i]
        if current_value not in unique_values:
            unique_values.append(current_value)
            lst.remove(current_value)
        else:
            i += 1
    
    while len(unique_values) < int(numCards):
        counter = Counter(lst)
        # Get the most common element
        most_common_element = counter.most_common(1)[0][0]

        unique_values.append(most_common_element)
        lst.remove(most_common_element)


    return unique_values