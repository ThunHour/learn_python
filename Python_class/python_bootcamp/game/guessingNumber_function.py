from random import randint


def name():
    userInputName = input("Please input your name before start the game: ")
    return userInputName


def start():
    print(f"Hey {name()} are you ready to take the challenge? Press y/Y to start and press n/N to quit: ")
    gameStart = input()
    return gameStart


def main():
    while True:
        maximunCount = 6
        count = 1
        if start() == "Y" or start() == "y":
            print('I have a number in mind (1 to 10000) you have maximum 6 attempts to guess the number')
            numberRandom = randint(1, 10000)

            while count < maximunCount:
                userGuess = int(input(f'Attempt {count}: '))

                if userGuess == numberRandom:
                    print(f'Brilliant! {start()}, you have guessed it in {count} attempets')
                    break
                elif userGuess > numberRandom:
                    print(f'Attempt {count} failed, guess a number lower than that')
                else:
                    print(f'Attempt {count} failed, guess a number higher than that')
                count += 1

            if count == maximunCount:
                userGuess = int(input(f"Your last chance Attempt {6}: "))
                if userGuess == numberRandom:
                    print(f"Brilliant! {start()}, you have guessed it in {count} attempets")
                    break
                else:
                    print(f"Attempt 6 failed, The number I have guessed was {numberRandom}")
                    print("You have lost all your chances Better luck next time :(")
                    break
            elif start() == "N" or start() == "n":
                print(f"Thank you {name()}")
                break

    print("Do you want to continue? [Y/N]")
    answer = input()

    if answer == "n" or answer == "N":
        print(f"Thank you {name()}")
        exit()
    else:
        main()


main()
