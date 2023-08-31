def quicksort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        quicksort(arr, left, p - 1)
        quicksort(arr, p + 1, right)


def partition(arr, left, right):
    i = left
    j = right-1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1

        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i


arr = [15,60,9,51,75,12,36,85,90,6,8,65,54]
quicksort(arr, 0, len(arr) - 1)
print(arr)
