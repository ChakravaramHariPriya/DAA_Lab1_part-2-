def merge_sorted_lists(lists):
    # Remove empty lists from the input
    non_empty_lists = [l for l in lists if l]
    if not non_empty_lists:
        return []
    
    merged_list = merge(non_empty_lists[0], non_empty_lists[1])
    
    for i in range(2, len(non_empty_lists)):
        merged_list = merge(merged_list, non_empty_lists[i])
    
    return merged_list

def merge(list1, list2):
    merged_list = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))
    
    merged_list += list1
    merged_list += list2
    return merged_list

sorted_lists = [[10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33]]
result = merge_sorted_lists(sorted_lists)
print(result)