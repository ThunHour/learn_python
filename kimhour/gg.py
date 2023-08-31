import random
userName = input('Please input your name before start the game:')
print(f'Hey {userName} are you ready to take the challenge?')
button = input('Press y/Y to start any other key to stop:')
def main():
    if button == 'y' or button == 'Y':
        print('I have a number in mind (1 to 10000) you have maximum 6 attempts to guess the number')
        guess = random.randint(1,10000)
        i = 1
        while i < 6:
            num = int(input(f'Attemp {i}: '))
            if num > guess :
                    print(f'Attempt {i} failed,guess a number lesser than that')
                    i += 1

            elif num < guess :
                    print(f'Attempt {i} failed,guess a number higher than that')
                    i += 1

            elif num == guess :
                    print(f'Brilliant {userName}, you have guessed it in {i} attempts')
                    restart = input('Press y/Y if you want to restart the game n/N to quit:')
                    if restart == 'y' or restart == 'Y':
                        print(main())
                    elif restart == 'n' or restart == 'N':
                        exit()


        if i == 6:
            print('Your last chance attempt 6:')
            num = int(input(''))
            if num != guess :
                print(f'Attempt 6 failed,The number I guessed was {guess}')
                print('You have lost all your chances.Better luck next time:( ')
                restart = input('Press y/Y if you want to restart the game n/N to quit:')
                if restart == 'y' or restart == 'Y':
                    print(main())
                elif restart == 'n' or restart == 'N':
                    exit()


            elif num == guess:
                print(f'Brilliant {userName}, you have guessed it in 6 attempts')
                restart = input('Press y/Y if you want to restart the game n/N to quit:')
                if restart == 'y' or restart == 'Y':
                    print(main())
                elif restart == 'n' or restart == 'N':
                    exit()
    else:
        exit()

print(main())
