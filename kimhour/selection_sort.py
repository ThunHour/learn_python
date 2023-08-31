def selection_sort(arr):

    for i in range(len(arr)):

        min_position = i

        for j in range(i, len(arr)):

            if arr[j] < arr[i]:

                min_position = j

        arr[i], arr[min_position] = arr[min_position], arr[i]
    print(arr)


selection_sort([21, 33, 11, 44, 1, 53, 2, 4, 62, 52, 74, 63, 23, 42, 3, 5, 90, 7])


# def selectionSort(array):
#   for i in range(0,len(array)-1):
#       minimum = i
#       for j in range(i+1, len(array)):
#       if array[j] < array[minimum]:
#         minimum = j
#     array[i],array[minimum]= array[minimum],array[i]
#   return array
#
#
# array = [21,33,11,44,1,53,2,4,62,52,74,63,23,42,3,5,90,7]
# print(selectionSort(array))
