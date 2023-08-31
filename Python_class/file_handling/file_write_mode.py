#IF you have something in your text, it will going to delete all of them and write the new one

# with open('/Users/rithyp/Documents/KIT_folder/Python_class/file_handling/testing.txt','w') as fp:

#     message = input("Enter something: ")
    
#     fp.write(message)



#Fomal 
try:
    with open('/Users/rithyp/Documents/KIT_folder/Python_class/file_handling/testing.txt','w') as fp:
        
        message = input("Enter something: ")
        fp.write(message)


except Exception as error:
    print(error)

finally:
    fp.close()
    print("File close successfully")
