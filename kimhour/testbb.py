# def bubble_short(list):
#     for i in range (0,len(list)-1):
#         for j in range(i):
#             if list[j] > list[j+1]:
#                 tem = list[j]
#                 list[j]=list[j+1]
#                 list[j+1]=tem
#     print(list)
#
#
#
# bubble_short([12,13,45,23,1,3,5,18,43])

def bubble_short(list):
    for i in range (len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                tem = list[j]
                list[j]=list[j+1]
                list[j+1]=tem


    print(list)

bubble_short([12,13,45,23,1,3,5,18,43])
