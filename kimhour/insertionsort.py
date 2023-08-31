# def insertion_sort(list):
#     for i in range(len(list)):
#         j=i
#         while list[j] < list[j-1] and j >0:
#             list[j],list[j-1]=list[j-1],list[j]
#             j-=1
#     print(list)
#
# inssertion_sort([12,33,14,53,65,1,4,5,42,7,21,2])

def insertion_sort(arr):
     for i in range(0,len(arr)-1):
         while arr[i] > arr[i+1] and i >=0 :
             arr[i],arr[i+1] = arr[i+1],arr[i]
             i-=1
     print(arr)


insertion_sort([12,33,14,53,65,1,4,5,42,7,21,2])
