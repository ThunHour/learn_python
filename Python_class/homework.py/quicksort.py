def quicksort(arr,left,right):

    if left < right:
        swaping_pos = swaping(arr,left,right)
        quicksort(arr,left,swaping_pos-1)
        quicksort(arr,swaping_pos+1,right)


def swaping(arr,left,right):
    i = left
    j = right -1
    p = arr[right]

    while i < j:
        while i < right and arr[i] < p:
            i+=1
        
        while j > left and arr[j]>p:
            j -=1

        
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]

    if arr[i] > p:
        arr[i], arr[right] = arr[right],arr[i]

    return i 

arr = [15,60,9,51,75,12,36,85,90]
quicksort(arr,0,len(arr)-1)
print(arr)