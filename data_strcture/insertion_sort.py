import array
def insertion(arr):
    for i in range(0,len(arr)-1):
        while arr[i]>arr[i+1] and i>=0:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            i-=1
    print(arr)

array=array.array("i",[2, 10, 9, 6, 5, 1, 4, 3])
insertion(array)

