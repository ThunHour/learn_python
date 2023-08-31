while True:
    print('Press 1 to encode')
    print('Press 2 to decode')
    press=int(input(''))
    if press == 1:
        word1=input('Enter the string to encode: ')
        deword=''
        for word1 in word1:
            word1=ord(word1)
            if word1 < 78:
                word1+=13
                word1=chr(word1)
                deword+=word1
            else:
                word1-=13
                word1=chr(word1)
                deword+=word1

        print(f'The decoded text is:{deword}')
    else:
         word1=input('Enter the string to decode: ')
         deword=''
         for word1 in word1:
             word1=ord(word1)
             if word1 < 78:
                 word1+=13
                 word1=chr(word1)
                 deword+=word1
             else:
                 word1-=13
                 word1=chr(word1)
                 deword+=word1
         print(f'The encoded text is:{deword}')
    print('Do you want to continue? [Y/N] ')
    next=input('')
    if next=='N'or next=='n':
        break


















