#If you use 'w' you cant read the message but if you use 'w+' to read and write a file

try:
    f = open('/Users/rithyp/Documents/KIT_folder/Python_class/GG1.txt','w+')
    message = "\n" + input("Input some text: ")
    f.write(message)
    f.seek(0,0)
    message = f.read() #You cant see anything in this because your current position is at the last point of the file 

    #instead you can use this to help you 
    print(message)
except Exception as error:
    print("Exception:",error)

finally:
    f.close()
    print("File closed successfully")