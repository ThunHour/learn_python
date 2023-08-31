a = "Hello Hello HelloKimi" 
b = "Hello" #words you want to replace
c = "Hi" #replace words

# print(a.replace(b,c))

# newList = []
# for i in a.split(): #["Hello", "Hello","HelloKimi"]
#     if i == b:
#         replaceWord = i.replace(i,c)
#         newList.append(replaceWord) #newList = ["Hi","Hi"]
#     else:
#         newList.append(i) #newList = ["HelloKimi"]

# print(newList) #["Hi","Hi","HelloKimi"]
newList = ["Hello", "Hello","HelloKimi"]
results = " ".join(map(str,newList)) #covert list into String
print(results)


a = ["1","2","3","4"]

