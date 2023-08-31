a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

try:
    c = a/b
    f = open("test.txt","r")

except Exception as error:
    print(error) #give you what is your code is error ==> example 10, 0 ==> erorr cant division by zero



#second method 
try:
    c = a/b
    f = open("text.txt","r")
except ( ValueError, FileNotFoundError ) as error:
    print(error)


finally: #this will run after try or except is excusted
    print("Program is finish ")