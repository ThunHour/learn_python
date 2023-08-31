def text(name,time_of_loops):
    print(f'{time_of_loops} {name}')
    
    if time_of_loops == 1:
        return #to end when time of loop == 1 
    text(name,time_of_loops-1)
    

text("Monirith",10)
