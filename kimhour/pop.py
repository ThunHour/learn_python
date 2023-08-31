def QuickSort(list):
    elements = len(list)
    if elements < 2:
        return list
    current_position = 0
    for i in range(1, elements):
         if list[i] <= list[0]:
              current_position += 1
              list[i],list[current_position]=list[current_position],list[i]

    list[0],list[current_position]=list[current_position],list[0]
    left = QuickSort(list[0:current_position])
    right = QuickSort(list[current_position+1:elements])
    arr = left + [list[current_position]] + right
    return arr


array_to_be_sorted = [15,60,9,51,75,12,36,85,90]
print(QuickSort(array_to_be_sorted))
