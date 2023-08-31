#If you use append mode everything in the file is not errase it, before writing the new one like write mode
#But it will give you no space between each other
with open('/Users/rithyp/Documents/KIT_folder/Python_class/file_handling/testing.txt','a') as fp:

    message = input("Enter something: ")
    fp.write(message) 


    fp.close()


#You need to + " \n " to make it 

# with open("/Users/rithyp/Documents/KIT_folder/Python_class/file_handling/testing.txt","a") as fp:
#     message = "\n" + input("Enter something: ")
#     fp.write(message)

#     fp.close()

    