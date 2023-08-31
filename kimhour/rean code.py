# def letter(letter):
#     for i in range(0,len(letter),2):
#         print(letter[i:i+2])
#
# letter("abcdefghijklmnopqrstuvwxyz")

# list="abcdefghijklmnopqrstuvwxyz"
# for i in list:
#     with open(f"E:/IT ClaSS/[FreeCourseSite.com] Udemy - 100 Python Exercises I Evaluate and Improve Your Skills/{i}.txt","w") as file:
#         file.write("{}".format(i))

# with open("E:/IT ClaSS/[FreeCourseSite.com] Udemy - 100 Python Exercises I Evaluate and Improve Your Skills/hour_zin_mg.txt",'r') as file:
#     list_letter=[]
#     for letter in file.read():
#         list_letter.append(letter)
#     print(list_letter)

# list ='abcdefghijklmnopqrstuvwxyz'
# list_word=[]
# for letter in list:
#     with open(f'E:/IT ClaSS/[FreeCourseSite.com] Udemy - 100 Python Exercises I Evaluate and Improve Your Skills/{letter}.txt',"r") as file:
#         list_word.append(file.read())
#
# print(list_word)

# list_word='supercalifragilisticexpialidocious'
# list_index=[]
# for letter in range(0,len(list_word)):
#     if list_word[letter] == "a" or list_word[letter] == "e" or list_word[letter] == 'i' or list_word[letter] == 'o' or list_word[letter] == 'u' or list_word[letter] == 'y':
#         list_index.append(letter+1)
# print(list_index)


# def pow_num(number):
#     return [2**i for i in range(number+1)]
#
#
# print(pow_num(0))
# print(pow_num(1))
# print(pow_num(2))

# def sort_letter(word):
#     print(''.join(sorted(word)))
#
#
# sort_letter('abcdsaferas')

# def remove(list):
#     print(list[::2])
#
#
# array= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# remove(array)

# list=[[2,5],[3,4],[8,7]]
# pow=1
# for i in list:
#     pow=pow*(i[0]-i[1])
# print(pow)


# list ='abcdefghijklmnopqrstuvwxyz'
# list_word=[]
# for letter in list:
#     with open(f'E:/IT ClaSS/[FreeCourseSite.com] Udemy - 100 Python Exercises I Evaluate and Improve Your Skills/{letter}.txt',"r") as file:
#         if letter in "python":
#             list_word.append(file.read())
#         else:
#             continue
# print(list_word)





# def last(n):
#     return n[1]
#
#
# def sort_list_last(tuple):
#     return sorted(tuple,key=last)
#
#
# tuple_sort=[(2, 'c',2), (1, 'b',4), (4,'a',5), (2, 'e',6), (2, 'd',7)]
# print(sort_list_last(tuple_sort))


# def sum(num):
#     sum=0
#     for i in range(1,num+1):
#         if i %3==0 or i %5==0:
#             sum+=i
#     return sum
#
#
# print(sum(5))
# print(sum(10))


# def replat_string(string):
#     string_new=""
#     for i in string:
#         if i == 'a':
#             string_new+='b'
#         elif i == 'b':
#             string_new+='a'
#         else:
#             string_new+=i
#     return string_new
#
#
# print(replat_string('acb'))
# print(replat_string('abababababababab'))
# print(replat_string('aaabcccbaaa'))


# def kata(x):
#     x_count=0
#     for i in x:
#         if i == 'good':
#             x_count+=1
#     if x_count <=2:
#         return 'Publish!'
#     elif x_count >2:
#         return  'I smell a series!'
#     else:
#         return 'Fail!'
#
#
# print(kata(['bad', 'bad', 'bad']))
# print(kata(['good', 'bad', 'bad', 'bad', 'bad']))
# print(kata(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']))


# def kata(x):
#     count_good = x.count("good")
#
#     if count_good == 0:
#         return "Fail!"
#     elif count_good <=2:
#         return "Publish!"
#     else:
#         return "I smell a series!"
#
#
# print(kata(['bad', 'bad', 'bad']))
# print(kata(['good', 'bad', 'bad', 'bad', 'bad']))
# print(kata(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']))


# def digit_change(number):
#     sting_new=''
#     for i in number:
#         if i >= '5':
#             sting_new+="1"
#         else:
#             sting_new +='0'
#     return sting_new
#
#
# print(digit_change('45385593107843568'))
# print(digit_change("509321967506747" ))
# print(digit_change("366058562030849490134388085" ))
# print(digit_change("800857237867"))


# def fake_bin(x):
#     return ''.join('0' if c < '5' else '1' for c in x)
#
#
# print(fake_bin('45385593107843568'))
# print(fake_bin("509321967506747" ))
# print(fake_bin("366058562030849490134388085" ))
# print(fake_bin("800857237867"))


# firstname = input("Enter first name: ")
# secondname = input("Enter second name: ")
# print("Your first name is %s and your second name is %s" %(firstname, secondname))


# def insertion_sort(arr):
#
#      for i in range(0,len(arr)-1):
#          while arr[i][1] > arr[i+1][1] and i >=0 :
#              arr[i],arr[i+1] = arr[i+1],arr[i]
#              i -= 1
#      print(arr)
#
#
# insertion_sort([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
#
#
# def flatten(*list):
#     new_list=[]
#     for i in list:
#         for j in i:
#             new_list.append(j)
#
#     return new_list
#
#
# print(flatten([2,4,3],[1,5,6], [9], [7,9,0]))
#
#
# import itertools
# original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
# new_merged_list = list(itertools.chain(*original_list))
# print(new_merged_list)


# def last(n):
#     return n[1]
#
#
# def sorted1(tuples):
#     return sorted(tuples, key=last,reverse=True)
#
#
# print(sorted1([(2, 5,4), (1, 2,5), (4, 4,1), (2, 3,2), (2, 1,3)]))


# def duble(num):
#     list_new=[]
#     for i in num:
#        list_new.append(i*2)
#     return list_new
#
#
# def duble_2(num):
#     return [x*2 for x in num]
#
#
# list=[1, 2, 3]
# print(duble_2(list))
#
# def revese(num):
#     return int(''.join(sorted([x for x in str(num)], reverse=True)))
#
# def revese(num):
#     list_new=[]
#     for i in str(num):
#         list_new.append(i)
#     return int(''.join(sorted(list_new,reverse=True)))
# print(revese(15))
# print(revese(123456789))
# print(revese(42145))
# print(revese(145263))

# def sum_arry(*list):
#     list_new=[]
#     for i in list:
#         list_new+=i
#     return sum(list_new)
#
#
# print(sum_arry([1, 2, 3], [4, 5, 6]))
# print(sum_arry([-1, -2, -3], [-4, -5, -6]))
# print(sum_arry([0, 0, 0], [4, 5, 6]))
#
#
# def array_plus_array(arr1,arr2):
#     return sum(arr1) + sum(arr2)

# def list_name(list):
#     new_list=[]
#     for i in list:
#         if len(i)==4:
#             new_list.append(i)
#     return new_list
#     return [x for x in list if len(x)==4]
#
#
# print(list_name(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))
# print(list_name(["Ryan", "Jimmy", "123", "4", "Cool Man"] ))
# print(list_name(["Ryan", "Kieran", "Mark"]))

#
# def swap(a, b):
#     return b,a
#
#
# print(swap(20,10))
# def test_array(array):
#     new_list=[]
#     new_Zero=[]
#     for i in array:
#         if i !=0:
#             new_list.append(i)
#         else:
#             new_Zero.append(i)
#     return new_list+new_Zero
#
#
# print(test_array([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
# print(test_array([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))


# def list_like(array):
#     if len(array) >3:
#         print(f"{array[0]},{array[1]} and {len(array)-2} other like this")
#     elif len(array) ==3:
#         print(f"{array[0]},{array[1]} and {array[2]} like this")
#     elif len(array) ==2:
#         print(f"{array[0]} and {array[1]} like this")
#     elif len(array)==1:
#         print(f"{array[0]} like this")
#     else:
#         print("no one like this")
#
#
# list_like([])
# list_like(["Peter"])
# list_like(["Jacob", "Alex"])
# list_like(["Max", "John", "Mark"])
# list_like(["Alex", "Jacob", "Mark", "Max"])


# from collections import Counter
# text = 'hi! hello# hi! wow!! wow!! hello hello!! good good'
# words= text.lower().split()
# most_common_words = [word for word, word_count in Counter(words).most_common(3)]
# list=[]
# list_new=[]
# for i in most_common_words:
#     word=""
#     for j in i:
#         if j.isalnum():
#             word+=j
#     list.append(word)
# for x in list:
#     if x not in list_new:
#         list_new.append(x)
# print(list_new)


# import re
# from collections import Counter
#
# def top_word(text):
#     text = text.lower().split()
#     new = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in text]
#     if len(new) > 3:
#         most_common_words = [word for word, word_count in Counter(new).most_common(3)]
#         return most_common_words
#     return list(set(new))
#
# print(top_word('Hello, hello, Hello!'))


# def sort_last(array):
    # new_list=[]
    # new=array[::-1]
    # for i in new:
    #     if i not in new_list:
    #         new_list.insert(len(array),i)
    # return new_list[::-1]
#     return (sorted(set(array), key=array[::-1].index)[::-1])
#
# print(sort_last([1,2,4,3,4,3,1,3]))
# print(sort_last([3, 4, 4, 3, 6, 3]))


# import psycopg2
# print("="*30, "Insert Value", "="*30, "\n") ###########################
#
# db_conn = None            # can use this or not, it still work in python but if u don't use this in Java it will not work
# cursor = None
#
# # I have created database "kit_b9" and now i want to create table in DB "kit_b9"
# try:
#     db_conn = psycopg2.connect(host = "localhost", port = "5432", database = "kit_b9", user = "postgres", password = "seak1812002" )
#     print("Connection successful.")     # if it connected it will print "connection success"
#     cursor = db_conn.cursor()
#     print("Cursor received")
#
#     s_name = "Seanghor99"
#     marks = 99
#
#     # Insert the record value
#     cursor.execute("INSERT INTO student_mark (s_name, mark) VALUES(%s, %s);", (s_name, marks))
#     db_conn.commit()                              # use this to commit, when you don't use auto commit
#     print("Record inserted successfully")
#
# except Exception as e:
#     print("Issue: ", e)
# finally:
#     db_conn.close()              # when done all task, don't forgot to close file
#     print("File is closed.")
#     cursor.close()
#     print("Cursor closed")


import datetime

e = datetime.datetime.now()

print ("Current date and time = %s" % e)

print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))

print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))
