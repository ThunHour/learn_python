try :
    with open("C:/Users/user/PycharmProjects/pythonProject3/project_hour/hour.txt","w+") as file:
        message = "\n"+input("please enter your text:")
        file.write(message)
        message= file.read()
        print(message)
except Exception as e:
    print("Exception"+e)
finally:
    print("File closed successfully")



