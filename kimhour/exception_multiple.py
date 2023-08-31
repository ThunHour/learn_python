a = int(input("number :"))
b = int(input("number 2 :"))
try :
    c=a/b
    f = open("testing file","r")
except ZeroDivisionError as e :
    print(e)
except FileNotFoundError as e:
    print(e)
finally:
    print("file closed Successful")
