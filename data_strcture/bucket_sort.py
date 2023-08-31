def insertionSort(b):
	for i in range(1, len(b)):
		up = b[i]
		j = i - 1
		while j >= 0 and b[j] > up:
			b[j + 1] = b[j]
			j -= 1
		b[j + 1] = up	
	return b	
			
def bucketSort(x):
	arr = []
	slot_num = 10 # 10 means 10 slots, each
				# slot's size is 0.1
	for i in range(slot_num):
		arr.append([])
		
	# Put array elements in different buckets
	for j in x:
		index_b = int(slot_num * j)
		arr[index_b].append(j)
	
	# Sort individual buckets
	for i in range(slot_num):
		arr[i] = insertionSort(arr[i])
		
	# concatenate the result
	k = 0
	for i in range(slot_num):
		for j in range(len(arr[i])):
			x[k] = arr[i][j]
			k += 1
	return x

# Driver Code
x = [0.13,0.25,0.12,0.35,0.67,0.33,0.69,0.47,0.92,0.31]
print("Sorted Array is")
print(bucketSort(x))

