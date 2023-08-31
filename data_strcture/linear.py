def LinearSearch(array, n, k):
    for j in range(0, n):
        if (array[j] == k):
            return j

    print(time)
    return -1

 
array = [12,14,16,18,20,22,24,26,28,30]

key =26
n = len(array)

result = LinearSearch(array, n, key)

if(result == -1):

    print("Element not found")

else:

    print("Element found at index: ", result)