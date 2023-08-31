# with open('/Users/rithyp/Documents/KIT_folder/Python_class/file_handling/testing.txt','r') as fp:

#     #Method1
#     # read_from_text = fp.read()
#     # print(read_from_text)

    
#     #Method2
#     # print(fp.read())


#     #Method3
#     for text in fp:
#         print(text)



#formal
try:
    with open('/Users/rithyp/Documents/KIT_folder/Python_class/file_handling/testing.txt','r') as fp:
        print(fp.read())


except Exception as error:
    print(error)

finally:
    fp.close()
    print("File close successfully")

