#It is the same as r but you dont need to use seek(0,2) 
# because they are aleady the end of the file

try:
    f = open('/Users/rithyp/Documents/KIT_folder/Python_class/file_handling/GG1.txt','r+')
    message = "\n" + input("Input some text: ")
    f.write(message)
    f.seek(0,0) #It will change your cursor to the started point of the file
    message = f.read()
    print(message)

except Exception as e :
    print("Exception:",e)

finally:
    f.close()
    print("File closed sucessfully")