while True:
    print("Please input a paragraph: ")
    para =input()
    print("Please input a Searching String: ")
    searchStr = input()

    if searchStr in para:
        count = para.count(searchStr)
        print(f'There are {count} occurrences.')
        print("Do you want to replace the text [Y/N]")
        ans = input()

        if ans == "Y" or ans==  "y":
            print("Please input a replacement string: ")
            replaceWord = input()

            print(f'{count} words has been replaced from the paragraph')
            print(para)
            break

        elif ans == "N" or ans == "n":
            print("Oh! you don’t like to replace, Do you want to check again [Y/N]?")
            ansAgain = input()
            if ansAgain == "Y" or ansAgain==  "y":
                continue
            elif ansAgain == "N" or ansAgain == "n":
                break
            else:
                print("Please give proper input")
        else:
            print("Please give proper input")
            print("Do you want to replace the text [Y/N]?")
            ansAgain = input()
            if ansAgain == "Y" or ansAgain == "y":
                continue
            elif ansAgain == "N" or ansAgain =="n":
                break
            else:
                print("Please give proper input")
