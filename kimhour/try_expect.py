# a = int(input("Input a number: "))
# b = int(input("Input a number: "))


# try:
#     c = a/b 
# #if b == 0, you can use except to run continue run your code 
# except:
#     print("Divide by zero, issue, Your inpyt is wrong")
# # print(f"Results: {c}")
# print("success....")

#If no except : we will give us error 

a = int(input("Input a number"))
b = int(input("Input a number"))

print("Input success")
try:
    print("Before the probematic code")
    c = a/b
    print("After the probematic code")

#This line of code will you give a detail about why your code is error 
except Exception as errorDetail:
    print("The Error is: ",errorDetail)
else:
    print("No Exceptions")
print("Success...")


#Finally is if specified, will be executed regardless if the try block raises an error or not.

try:
    f = open("test1.txt", "r")
    print("Reading from the file")
except IOError as error:
    print("Unable to work with the file", error)
finally: # We use finally to release / close the resources
    print("File closed Successully")

print("Success...")



try:
    a = int(input("Input a number"))
    b = int(input("Input a number"))
    c = a/b
    print("No Problem in code")
except ZeroDivisionError as e:
    print("Problem in code",e)
finally:
    print("Be happy")


