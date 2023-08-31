# import timeit
#
# timeTakenForList = timeit.timeit(stmt='[35,23,43,76,58,67]',number = 5000000)
# timeTakenForSet = timeit.timeit(stmt='{35,23,43,76,58,67}',number = 5000000)
#
# print(timeTakenForSet)
# print(timeTakenForList)
# print(timeTakenForList - timeTakenForSet)
# if (timeTakenForList - timeTakenForSet > 0):
#     print("GG")
#
# elif (timeTakenForList - timeTakenForSet < 0):
#     print("FF")
#
# else:
#     print("123")
#


# import math
# my_list =[50,55,7,85,9,10]
#
# print(math.sqrt(my_list[-7]))


# list1 = [50,55,7,85,9,10]
# del list1[2:-1]
# print(list1)

# my_list = [50,55,7,85,9,10]
# my_list.extend([1,2,4,5,6])
# print(my_list)


# from random import randint
#
# for i in range(1,4):
#     random = randint(1,10)
#     print(random)

# import random
# num = 2
# i = 0
# while i < num:
#     num = random.randint(5,10)
#     print('Random number is: ', num)
#     i+=1
#     totalofSum = 0
#     for i in userInput:
#         if len(i) % 2 == 0:
#             # evenNumber = int(i)*3
#             # print(evenNumber)
#             # totalofSum += int(evenNumber)
#             print("GG")
#         else:
#             # oddNumber = int(i) *1
#             # print(oddNumber)
#             # totalofSum += int(oddNumber)
#             print("GGOO")
#
#     # print(totalofSum)
#
# 978101002389
#
#         sumOddLen = int(i)*1
#         totalSum += sumOddLen
#     # for i in range(1,int(userInput),2):
#     #     sumEvenLen = i*3
#     #     totalSum += sumEvenLen
#
#     print(totalSum)


#
# def stu (id,name):
#
#     print(id,name)
#
# stu("Sovan",id = 120)



# def ran(num):
#     list_num = []
#     for i in range(num):

#         list_num.append(i)

#     return '\n'.join(map(str, list_num))

# print(ran(5))


# a = ['Hello', 'World', 'This', 'Is', 'Python', 'Lmao']
# print(' '.join(a))


#
# def find_all(lsit,value):
#     ls1 = []
#
#     for i in lsit :
#         newValue = lsit.index(value)
#
#         ls1.append(newValue)
#     print(ls1)
#
#
# find_all(['A','B','C','C','D','E','F','C'],'C')

# list1 = [0,1,2]
#
# total = 0
# for i in list1:
#     total += i
#
# if total % 2 == 0:
#     print("even")
# else:
#     print("odd")

#
# def multi_table(number):
#     for i in range (1,11):
#         total = 0
#         total = i * number
#         print(f'{i} * {number} = {total}\n')
#
# print(multi_table(5))

# a = "1234english ;k"
#
# print(a.find('english'))

#
# numbers = [2,3,3,5]
# print(numbers[::2])

# numbers = [2,3,4,5]
# total = 0
# for i in numbers:
#     if i % 2 == 0:
#         total += i
# print(total)
# r = 20
# g = 255
# b = 255
# colorcode = {10:"A",11:"B",12: "C",13: "D",14: "E",15: "F"}
# results = ""
# #r
# if r // 16 in colorcode:
#     results+= colorcode[r // 16]
#     print(results)
# else:
#     results += str(r)
# #g
# results+=colorcode[g//16]
# #b
# results+=colorcode[b//16]
# print(results)


# def rgb(r, g, b):
#     if r == 0 and g ==0 and b ==0:
#         return "000000"
#     else:
#         #red color
#         results = ""
#         rcolor = hex(r)[2:].upper()
#         results += rcolor
#         print(re)
#         #green color
#         gcolor = hex(g)[2:].upper()
#         results += gcolor
#
#         #blue color
#         bcolor = hex(b)[2:].upper()
#         results += bcolor
#         return results
# print(rgb(1,2,3))
# a = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
# list1 = a.split()
#
# listOfInt = map(int,list1)
#
#
# integer_list = list(listOfInt)
# print(integer_list)
# print(max(integer_list))
#
# def find_short(s):
#     sortedWords = s.split()
#
#
#     return len(min(sortedWords, key=len))
# print(find_short("bitcoin take over the world maybe who knows perhaps"))

# a = 12345
# aNew = list(map(int, str(a)))
# print(sorted(aNew,reverse=True))

# a = 'one two three'
# b = a.split()

# mix = 0
# for i in b:
#     length = len(i)
#     mix = length
#     if mix < length:
#         mix = length

# print(mix[i])

# a = [1,2,3,4,5]
# # b = [1, 3, 6, 10, 15]
# res = []
# start = 0
# for num in a:
#     number = num + start
#     start += num

#     res.append(number)

# print(res)

x=[5,6,5,6,8,6,5,5,6]
t=sum(x)/8
print(t)


