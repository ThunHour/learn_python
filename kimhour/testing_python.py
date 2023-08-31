def selection_sort(list_sort):
    for i in range(0, len(list_sort)-1):
        mini = i
        for j in range(i+1, len(list_sort)):
            if list_sort[j] < list_sort[mini]:
                mini = j
        list_sort[i], list_sort[mini] = list_sort[mini], list_sort[i]
    return list_sort


list = [21, 33, 11, 44, 1, 53, 2, 4, 62, 52, 74, 63, 23, 42, 3, 5, 90, 7]
print(f"Selection{selection_sort(list)}")
