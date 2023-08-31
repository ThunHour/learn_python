while True:
    print('Press 1 to encode')
    print('Press 2 to decode')
    press=int(input(''))
    if press == 1:
        word1=input('Enter the string to encode: ')
        deword=''
        for word1 in word1:
            word1=ord(word1)
            if word1 >=65 and word1 <=77 or word1>=97 and word1<=109:
                word1+=13
                word1=chr(word1)
                deword+=word1
            elif word1 >=78 and word1 <=90 or word1>=110 and word1<=122:
                word1-=13
                word1=chr(word1)
                deword+=word1
        print(f'The decoded text is:{deword}')
    else:
         word1=input('Enter the string to encode: ')
         deword=''
         for word1 in word1:
            word1=ord(word1)
            if word1 >=65 and word1 <=77 or word1>=97 and word1<=109:
                word1+=13
                word1=chr(word1)
                deword+=word1
            elif word1 >=78 and word1 <=90 or word1>=110 and word1<=122:
                word1-=13
                word1=chr(word1)
                deword+=word1
         print(f'The decoded text is:{deword}')
    print('Do you want to continue? [Y/N] ')
    next=input('')
    if next=='N':
        break


















