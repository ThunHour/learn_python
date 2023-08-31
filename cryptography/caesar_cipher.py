def encrypt():
    userInput=input("Enter text you want to encrypt:")
    user_shift=int(input("Enter your shift(1 to 25):"))
    if user_shift >25:
        print(userInput)
    elif user_shift<26: 
        new_word=""
        for i in userInput:
            if i.isdigit():
                x=0
                x=int(i)
                new_word+=(str((x+user_shift)%10))
            else:
                ascii_word=ord(i) #65
                if ascii_word >96 and ascii_word <123:
                    new_value=chr((ascii_word+user_shift-97)%26+97) 
                    new_word+=new_value
                elif ascii_word >64 and ascii_word <91:
                    new_value=chr((ascii_word+user_shift-65)%26+65) 
                    new_word+=new_value
                elif ascii_word ==32:
                    new_word+=ascii_word
        print(new_word)

def decrypt():
    userInput=input("Enter text you want to decrypt:")
    user_shift=int(input("Enter your shift(1 to 25):"))
    if user_shift >25:
        print(userInput)
    elif user_shift<26: 
        new_word=""
        for i in userInput:
            if i.isdigit():
                x=0
                x=int(i)
                new_word+=(str(((10-user_shift)+x)%10))
            else:
                ascii_word=ord(i) #65
                if ascii_word >96 and ascii_word <123:
                    new_value=chr((ascii_word-user_shift-97)%26+97) 
                    new_word+=new_value
                elif ascii_word >64 and ascii_word <91:
                    new_value=chr((ascii_word-user_shift-65)%26+65) 
                    new_word+=new_value
                elif ascii_word ==32:
                    new_word+=ascii_word
        print(new_word)

choise =int(input(" 1 for encrypt \n 2 for decrypt  \n :"))
if choise==1:
    encrypt()
elif choise==2:
    decrypt()
        
