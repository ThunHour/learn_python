while True:
    print('Please input a paragraph:')
    text=input()
    print("Please input a Search String: ")
    check=input()
    if check in text:
        countter=text.count(check)
        print(f'There are {countter} occurrences. ')
        print('Do you want to replace the text [Y/N]? ')
        answer=input()
        if answer=='Y' or answer=='y':
            print('Please input a replacement string:')
            reputtext=input()
            print(f'{countter} words has been replaced from the paragraph')
            replacetext = text.replace(countter,reputtext)
            print(replacetext)
            break
        elif answer == "N" or answer == "n":
            print("Oh! you don’t like to replace, Do you want to check again [Y/N]?")
            newanswet = input()
            if newanswet == "Y" or newanswet==  "y":
                continue
            elif newanswet == "N" or newanswet == "n":
                break
            else:
                print("Please give proper input")



