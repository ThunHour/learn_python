def binary_search(arr, key):
    l_bound = 0
    u_bound = len(arr)-1
    count = 0
    while u_bound >= l_bound:
        mid = (l_bound+u_bound)//2
        if list[mid] == key:
            print("It took ", count, " Executions to check the entire list")
            return mid
        elif list[mid] < key:
            l_bound = mid + 1
        else:
            u_bound = mid - 1
        count += 1
    print("It took ", count, " Executions to check the entire list")
    return -1


list = [14, 12, 16, 18, 20, 22, 24, 26, 28]
list.sort()
key = 26
pos = binary_search(list, key)
if pos == -1:
    print("Element not found")
else:
    print("Element found at index: ", pos)
