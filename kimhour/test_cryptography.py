from cryptography.fernet import Fernet
while True:
    print("1 for encrypt text")
    print("2 for decrypt text")
    user_en_de= input("Drop your choice here:")
    if user_en_de.isdecimal():
        user_en_de= int(user_en_de)
        if user_en_de==1:
            key = Fernet.generate_key()
            f = Fernet(key)
            print("the secret key generated is: ")
            print(key)
            msg = bytes(input("Enter the secret message: "), 'utf-8')
            print("the encrypted message is: ")
            secret = f.encrypt(msg)
            print(secret)
        elif user_en_de==2:
            key_user=input("Drop your key here:")
            text_to_de=bytes(input("Drop your text that you want to decrypt:"),'ASCII')
            f=Fernet(key_user)
            print("the decrypted message is: ")
            print(f.decrypt(text_to_de))
        user_anser=input("Do you want to continue?[Y/N] : ")
        if user_anser=="Y" or user_anser=="y":
            continue
        elif user_anser=="N" or user_anser=="n":
            print("Thanks you!!")
            break
    else:
        print("Please choose 1 or 2")
        print("="*100+'>')
        continue






