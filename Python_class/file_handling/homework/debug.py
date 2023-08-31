try: 
    with open("/Users/rithyp/Documents/KIT_folder/Python_class/file_handling/test1.txt",'r') as file1:
    # file1 = open("/Users/rithyp/Documents/KIT_folder/Python_class/file_handling/test1.txt",'r')
        with open("/Users/rithyp/Documents/KIT_folder/Python_class/file_handling/test2.txt",'r+') as file2:

            position = int(input("Enter position: "))
    
            file2.seek(position) #



            file2.write(file1.read()) #read file 1 to write file 2 

except Exception as error:
    print(error)

finally:
    print("Program success")