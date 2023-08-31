#First method 
f = open('/Users/rithyp/Documents/KIT_folder/Python_class/GG.txt','r')


# print(f.read(2)) #It will only read first 2 letters of the file
# print(f.readline(5)) #It will read a line and choose first 5 character
# print(f.read()) #Read the whole things in a text

#Same as read() but this will give a space between each line
for i in f:
    print(i) 


#second method 
with open('/Users/rithyp/Documents/KIT_folder/Python_class/GG.txt','r') as f:
    print(f.read())