while True:
    def sum_of_ascii():
          while True:
              name=input('Input your name: ')
              if name.isalpha():

                   if name=='stop' or name=='Stop' or name =='STOP':
                        print('You asked to stop the program... Stopping')
                        quit()
                   else:
                        sum=0
                        for i in name :
                                check=ord(i)
                                sum+=check
                        return f'{name}:{sum}'

              else:
                    print("Invalid String can't be converted")



print(sum_of_ascii())





