# def bubble_sort(list1):
#     for i in range(len(list1)-1,0,-1): #5,4,3,2,1 #for 
#         for j in range(i):
#             if list[j]>list[j+1]:
#                 temp = list[j]
#                 list1[j] = list[j+1]
#                 list1[j+1] = temp
#             print(list1)
#         print('*'*10)

# list1 = [50,65,8,12,65,7]
# bubble_sort(list1)
# print(list1)

def buble(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

list1 = [50,65,8,12,65,7]
buble(list1)
print(list1)


#5
#0,1,2,3,4 (index)
#4
#0,1,2,3
#arr[4]
#condition use something diffrent from % 
# for i in range(0,5,2): #-1 ==> start > end , 
#     print(i)

# for i in range(1,5,2):
#     print(i)


