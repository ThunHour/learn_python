import random
print('Welcome to the dices game!')
while True:
    player=input('Enter the number of dices you want to roll:')
    if player.isdecimal():
        player=int(player)
        if player >0 and player<9:
            result=0
            for i in range(1,int(player)+1):
                randomDice = random.randint(1,6)
                result +=randomDice
                print(f'Doce{i}:{randomDice}')
            print("="*10)
            print(f'RESULT: {result}')
            print("="*10)
            break

    else:
        print('USAGE: The number must be between 1 and 8')

