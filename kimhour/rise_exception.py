
while True:
    mark = int(input("enter mark:"))
    if mark < 100 :
        break
    try:
        if mark > 100:
            raise IndentationError
    except IndentationError:
        print("Please enter below or equal 100 ")


