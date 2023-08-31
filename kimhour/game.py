import random

name = input('Please input your name before start the game:')
print(f'Hey {name} are you ready to take the challenge?')
press=input('Press y/Y to start any other key to stop:')
while True:
    counter=1
    chance=6
    if press=='y' or press =='Y':
            print('I have a number in mind (1 to 10000) you have maximum 6 attempts to guess the number')
            number=random.randint(1,10000)
            while counter < chance:
                    answer =int(input(f'Attempt {counter}:'))
                    if answer == number:
                        print(f'Brilliant! {name} , you have guessed it in {counter} attempts')
                        break
                    elif answer < number:
                          print(f'Attempt {counter}  failed, guess a number lesser than that')
                          counter+=1
                    else:
                         print(f'Attempt {counter} failed, guess a number higher than that')
                         counter+=1
                    if counter == chance:
                        answer = int(input(f"Your last chance Attempt {6}: "))

                        if answer == number:
                            print(f"Brilliant! {name}, you have guessed it in {counter} attempets")
                            break
                        else:
                             print(f"Attempt 6 failed, The number I have guessed was {number}")
                             print("You have lost all your chances Better luck next time :(")
                             break
    else:
        print(f'if you try {name} . you may win this game ')
        break

    print('Press y/Y if you want to restart the game n/N to quit:' )
    choice=input('')

    if choice == 'n'or choice== 'N':
        print(f'if you try {name} . you may win this game ')
        break
    else:
        continue


