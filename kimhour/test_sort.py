def bubble_sort(list_sort):
    for i in range(len(list_sort)-1, 0, -1):
        for j in range(i):
            if list_sort[j] > list_sort[j+1]:
                list_sort[j], list_sort[j+1] = list_sort[j+1], list_sort[j]
    return list_sort


arr = [21, 33, 11, 44, 1, 53, 2, 4, 62, 52, 74, 63, 23, 42, 3, 5, 90, 7]
print(f"Bubble_sort{bubble_sort(arr)}")


def selection_sort(list_sort):
    for i in range(0,len(list_sort)-1):
        mini = i
        for j in range(i+1, len(list_sort)):
            if list_sort[mini] > list_sort[j]:
                mini = j
        list_sort[mini], list_sort[i] = list_sort[i], list_sort[mini]
    return list_sort


list = [21, 33, 11, 44, 1, 53, 2, 4, 62, 52, 74, 63, 23, 42, 3, 5, 90, 7]
print(f"Selection_sort{selection_sort(list)}")


def merge_sort(list_sort):
    if len(list_sort) == 1:
        return list_sort
    mid = len(list_sort)//2
    left = merge_sort(list_sort[:mid])
    right = merge_sort(list_sort[mid:])
    return merged(left, right)


def merged(left, right):
    i = j = 0
    merged_list = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged_list.append(right[j])
            j += 1
        elif left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
    merged_list.extend(left[i:])
    merged_list.extend(right[j:])
    return merged_list


list = [21, 33, 11, 44, 1, 53, 2, 4, 62, 52, 74, 63, 23, 42, 3, 5, 90, 7]
print(f"Merged_sort{merge_sort(list)}")


def quick_sort(list_sort, start, end):
    if start < end:
        p = pos(list_sort, start, end)
        quick_sort(list_sort, start, p-1)
        quick_sort(list_sort, p+1, end)


def pos(list_sort, start, end):
    pivot = list_sort[end]
    i = start
    j = end-1
    while i < j:
        while i < end and list_sort[i] < pivot:
            i += 1
        while j > start and list_sort[j] >= pivot:
            j -= 1
        if i < j:
            list_sort[i], list_sort[j] = list_sort[j], list_sort[i]

    if list_sort[i] > pivot:
        list_sort[i], list_sort[end] = list_sort[end], list_sort[i]
    return i


list = [21, 33, 11, 44, 1, 53, 2, 4, 62, 52, 74, 63, 23, 42, 3, 5, 90, 7]
quick_sort(list, 0, len(list)-1)
print(f"Quicksort{list}")


def insertion_sort(list_sort):
    for i in range(1, len(list_sort)):
        while list_sort[i-1] > list_sort[i] and i > 0:
            list_sort[i], list_sort[i-1] = list_sort[i-1], list_sort[i]
            i -= 1
    return list_sort


list = [21, 33, 11, 44, 1, 53, 2, 4, 62, 52, 74, 63, 23, 42, 3, 5, 90, 77]
print(f"Insertion_sort{insertion_sort(list)}")





