from random import randint

userInputName = input("Please input your name before start the game: ")
print(f"Hey {userInputName} are you ready to take the challenge? Press y/Y to start and press n/N to quit: ")
startGameButton = input()
while True:
    maximunCount = 6
    count = 1
    if startGameButton == "Y" or startGameButton == "y":
        print('I have a number in mind (1 to 10000) you have maximum 6 attempts to guess the number')
        numberRandom = randint(1,10000)
        print(numberRandom)
        while count < maximunCount:
            userGuess = int(input(f'Attempt {count}: '))

            if userGuess == numberRandom:
                print(f"Brilliant! {userInputName}, you have guessed it in {count} attempets")
                break
            elif userGuess > numberRandom:
                print(f'Attempt {count} failed, guess a number lower than that')
            else:
                print(f'Attempt {count} failed, guess a number higher than that')
            count +=1
            if count == maximunCount:
                userGuess = int(input(f"Your last chance Attempt {6}: "))
                if userGuess == numberRandom:
                    print(f"Brilliant! {userInputName}, you have guessed it in {count} attempets")
                    break
                else:
                    print(f"Attempt 6 failed, The number I have guessed was {numberRandom}")
                    print("You have lost all your chances Better luck next time :(")
                    break
    elif startGameButton == "N" or startGameButton == "n":
        print(f"Thank you {userInputName}")
        break

    print("Do you want to continue? [Y/N]")
    answer = input()

    if answer == "n" or answer == "N":
        print(f"Thank you {userInputName}")
        break
    else:
        continue
