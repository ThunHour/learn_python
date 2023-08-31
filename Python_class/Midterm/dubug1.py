
# while True:
#     print("Please input a paragraph: ")
#     para = input()
#     print("Please input a Search String: ")
#     searchStr = input()

#     wordOfList = para.split()
#     count = 0
#     for i in wordOfList:
#         if i == searchStr:
#             count +=1

#     print(f"There are {count} occureences.")
#     print("Do you want to replace the text [Y/N]")
#     answer = input()
    
#     if answer == "Y"or answer =="y":
#         print("Please input a replacement string: ")
#         replaceString = input()
#         print(f'{count} words has been replaced from the paragraph')
#         newList = []
#         for j in wordOfList:
#             if j == searchStr:
#                 replaceWords = j.replace(j,replaceString)
#                 newList.append(replaceWords)
#             else:
#                 newList.append(j)
#         results = " ".join(map(str,newList)) #covert list into String
#         print(results)
#         break

#     elif answer == "N" or answer == "n":
#         print("Oh! you don’t like to replace, Do you want to check again [Y/N]?")
#         answerAgain = input()
#         if answerAgain == "Y" or answerAgain == "y":
#             continue
#         else: 
#             break   
#     else:
#         print("Please give proper input")
#         print("Do you want to replace the text [Y/N]")
#         answerAgain = input()
#         if answerAgain == "Y" or answerAgain == "y":
#             continue
#         elif answerAgain == "N" or answerAgain == "n":
#             break
#         else:
#             print("Please give proper input")
    

a = 30
res = 0
list_of_num = []
for num in range(0,a+1): #Rag
    print(num)
    # if a % num == 0:
    #     res +=1
    #     list_of_num.append(num)


print(f'a is divide by {res} because {list_of_num}')


a = "5"

a.isdecimal

