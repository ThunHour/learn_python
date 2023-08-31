try:
    with open('C:/Users/user/PycharmProjects/pythonProject3/project_hour/text1.txt', "r") as file1:

        with open('C:/Users/user/PycharmProjects/pythonProject3/project_hour/text2.txt', "r+") as file2:
            position = int(input("Enter position:"))
            file2.seek(position,1)
            text = file1.read()
            file2.write(text)
except Exception as e:
    print("Exception", e)
finally:
    file1.close()
    file2.close()
    print('File closed Successfully')

