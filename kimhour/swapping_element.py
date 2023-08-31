def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
print(arr)

def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        print(i)
        for j in range(i):
            print(j)
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
            print(list)
        print('*'*10)

list = [50,65,8,12,65,7]
bubble_sort(list)
print(list)
