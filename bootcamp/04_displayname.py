name = input('Enter your name: ')
number=int(input('Enter number of times to display:'))
if len(name)>0:
      for number in range(number):
       print(name)
else:
      print('No name entered')
