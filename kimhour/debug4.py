def merge(list):

    mid = len(list)//2
    left_side = list[:mid]
    right_side = list[mid:]
    i = j= k = 0
    while i < len(left_side) and j < len(right_side):
        if left_side[i] < right_side[j]:
            list[k] = left_side[i]
            i += 1
        else:
            list[k] = right_side[j]
            j += 1
        k += 1
    # Checking if any element was left
    while i < len(left_side):
        list[k] = left_side[i]
        i += 1
        k += 1

    while j < len(right_side):
        list[k] = right_side[j]
        j += 1
        k += 1
    return list

print(merge([55,12,10,64,85,25,63]))

