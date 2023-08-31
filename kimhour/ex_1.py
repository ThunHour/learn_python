def text(name,n):
    if n == 1:
        print(f'{1} : {name}')
    else: 
        text(name,n-1)
        print(f'{n} : {name}')
    
text("kimhour",5)
