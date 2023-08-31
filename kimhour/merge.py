def merge_sort(list):
    len_list = len(list)
    if len_list == 1:
        return list
    mid = len(list)//2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left, right)


def merge(list1, list2):
    i = j = 0
    merged = []
    len_list1 = len(list1)
    len_list2 = len(list2)
    while i < len_list1 and j < len_list2:
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    print(f'{merged}')
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


list = [5, 12, 13, 18, 32 , 35, 55, 7, 11, 14, 19]
res = merge_sort(list)
print(res)
