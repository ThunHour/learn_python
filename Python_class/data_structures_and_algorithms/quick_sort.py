
def quicksort(arr,left,right):

    # left = 0 #index 0
    # right = len(arr)-1 #index n 
    if left < right:
        partition_pos = partition(arr, left, right) #sub array to do all the task
        quicksort(arr, left, partition_pos-1) #divide left side until only 1 element left
        quicksort(arr, partition_pos+1, right) #divide right side until only 1 elements left

def partition(arr,left,right):
    i = left
    j = right -1
    pivot = arr[right] #last elements of arr

    #i move to the right and i looks for bigger elements then P , i > P
    #j move to the left and j look for smaller elements than P , j < P

    while i < j: #condition when i and j cross 
        while i < right and arr[i] < pivot: #move i to the right (while i is not the end of the arry) and arr[i] < pivot
            i += 1
        while j > left and arr[j] >= pivot: #move j to the left and arr[j] > pivot
            j -=1

        #check if elements cross yet
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    #after i and j cross each other
    if arr[i] > pivot:
        arr[i], arr[right]= arr[right],arr[i]

    return i

arr = [15,60,9,51,75,12,36,85,90]
quicksort(arr,0, len(arr)-1)
print(arr)