# try:
#     f = open('/Users/rithyp/Documents/KIT_folder/Python_class/GG1.txt','a')
#     message = input("Enter something: ") #This will give you no space if you input 2 time
#     #example
#         #First time Hello my name is Rith
#         #Second time Welcome to KIT
#         #==> Results Hello my name is RithWelcome to KIT

#     f.write(message) #YOu can see in the file but it will errase what we was writing before before starting the new one
    
# except: #If there anything wrong with location of the file it will give expection
#     print("Unable to open the file")


# finally:
#     f.close() #You need to close your file after writing something
#     print("File close successfully")



#If you want to have a new line in your text you need to use "\n" + 
try :
    f = open('/Users/rithyp/Documents/KIT_folder/Python_class/file_handling/GG1.txt','a')
    message = "\n" + input("Enter something: ")
    f.write(message)
except:
    print("Unable to open the file")

finally:
    f.close()
    print("File close successfully")