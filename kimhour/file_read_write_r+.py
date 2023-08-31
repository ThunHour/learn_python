try:
    f = open('/Users/rithyp/Documents/KIT_folder/Python_class/GG1.txt','r+')
    message = input("Input some text: ")
    f.seek(2) #It will start your cursor at the end of the file
    f.write(message)
    f.seek(0,0) #It will change your cursor to the started point of the file
    message = f.read()
    print(message)

except Exception as e :
    print("Exception:",e)

finally:
    f.close()
    print("File closed sucessfully")

#0 
#1
#2

#seek(offset,whence= 0)