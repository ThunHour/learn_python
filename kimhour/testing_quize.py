# def removes_duplicates(list_num):
#
#     return list(dict.fromkeys(list_num))
#
# print(removes_duplicates([1,2,2,3,3,4,4,5,6,7,7,7]))

# def  doubles_every_second_integer(list):
#     new_list=[]
#     for i in range(len(list)):
#         if i %2 !=1:
#             new_list.append(list[i])
#         else:
#             new_list.append(list[i]*2)
#     return new_list
#
#
# list=[1,2,3,4,5]
# print(doubles_every_second_integer(list))
# list=[-1000,1653, 210, 0, 1]
# print(doubles_every_second_integer(list))
#
# def change_sign_num(list):
#     new_list =[]
#     for num in list:
#         num_change=num*-1
#         new_list.append(num_change)
#     return new_list
#
#
# list=[1,2,3,4,5]
# print(change_sign_num(list))
# list=[1,-2,3,-4,5]
# print(change_sign_num(list))

# def reverses_string(list):
#     return list[::-1]
#
#
# list="hello"
# print(reverses_string(list))
# list="world"
# print(reverses_string(list))
#
# def sum_array ( list ) :
#     new_list = []
#     for i in list:
#         chnage = int(i)
#         new_list.append (chnage )
#     return sum ( new_list )
#
#
# list=['5','0', 9, 3, 2, 1, '9', 6, 7]
# print(sum_array ( list ))
# list=[9, 3, '7', '3']
# print(sum_array ( list ))
# list=['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']
# print(sum_array ( list ))

# def count_divisor(num):
#     new_list=[]
#     count=0
#     for element in range(1,num+1):
#         if num % element == 0:
#             new_list.append(element)
#             count+=1
#     return f'{count} because {tuple(new_list)}'
#
#
# num=30
# print(count_divisor(num))
# num=12
# print(count_divisor(num))
#
#
# def list_integer(list):
#     if len(list) != 0:
#         sum_num=sum(list)
#         if sum_num %2 ==0:
#             return "even"
#         else:
#             return 'Odd'
#     else:
#         return "Even"
#
#
# list=[0,-1,-5]
# print(list_integer(list))
# list=[0, 1, 4]
# print(list_integer(list))
# list=[]
# print(list_integer(list))
