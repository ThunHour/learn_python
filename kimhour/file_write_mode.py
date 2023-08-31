try:
    f = open('/Users/rithyp/Documents/KIT_folder/Python_class/GG1.txt','w')
    message = input("Enter something: ")

    f.write(message) #YOu can see in the file but it will errase what we was writing before before starting the new one
    
except: #If there anything wrong with location of the file it will give expection
    print("Unable to open the file")


finally:
    f.close() #You need to close your file after writing something
    print("File close successfully")




# #If location of the file is wrong
# try:
#     f = open('/Users/rithyp/Documents/KIT_folder/Pthon_class/GG1.txt','w')
#     message = "Welcome to KIT"

#     f.write(message) 
    
# except: #If there anything wrong with location of the file it will give expection
#     print("Unable to open the file")


# finally:
#     f.close() #You need to close your file after writing something
#     print("File close successfully")

