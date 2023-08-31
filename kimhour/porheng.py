# user_input =input("Input a sentence:")
# change=''.join(user_input.split(' '))
# print(change)
# count_up=0
# count_lo=0
# for i in range(0,len(change)):
#     if change[i] == change[i].upper():
#         count_up+=1
#     elif change[i] == change[i].lower():
#         count_lo+=1
# print(f"UPPER CASE : {count_up}")
# print(f'LOWER CASE : {count_lo}')
# list=[6,9,1,2,3]
# print(sorted(list,reverse=True))

# list=[]
# while True:
#     n =input("Enter number: ")
#     print("Enter q or quit to stop")
#     if n =='q' or n=='quit':
#         break
#     else:
#         list.append(int(n))
# print(f'Average :{sum(list)/len(list)}')
# even=[]
# odd=[]
# for i in list:
#     if i %2==0:
#         even.append(i)
#     elif i %2==1:
#         odd.append(i)
# print(f'Number of even value: {len(even)} : {even}')
# print(f'Number of Odd value: {len(odd)} : {odd}')
# list_1=[1,3,6,78,35,55]
# list_2=[12,24,35,24,88,120,155]
# print(list(set(list_1+list_2)))