def text(name,time_of_loops):
    if time_of_loops == 1:
        print(f'{1} : {name}')
    else:
        text(name,time_of_loops-1)
        print(f'{time_of_loops} : {name}')

text("Monirith",5)
