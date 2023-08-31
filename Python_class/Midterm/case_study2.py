from random import randint

print("Welcome to the dices game! ")
while True :
    dict_num = input("Enter the number of dics you wnat to roll: ")
    if dict_num.isdecimal():
        dict_num = int(dict_num)
        if dict_num in range(1,9):
            totalSum = 0
            if dict_num == 1:
                print(f'RESULT: {randint(1,6)}')
                break
            else:
                for i in range(1,int(dict_num)+1):
                    randomNum = randint(1,6)
                    totalSum += randomNum
                    print(f'Dice {i}: {randomNum}')
                print("="*10)
                print(f'RESULT: {totalSum}')
                print("="*10)
                break

        else:
            print("The number must be between 1 and 8")
    # else:
    #     print("The number must be between 1 and 8")





# import random
# print('Welcome to the dices game!')
# while True:
#     player=input('Enter the number of dices you want to roll:')
#     if player.isdecimal():
#         player=int(player)
#         if player >0 and player<9:
#             result=0
#             for i in range(1,int(player)+1):
#                 randomDice = random.randint(1,7)
#                 result +=randomDice
#                 print(f'Doce{i}:{randomDice}')
#             print("="*10)
#             print(f'RESULT: {result}')
#             print("="*10)
#             break
#
#
#
#     else:
#         print('USAGE: The number must be between 1 and 8')
