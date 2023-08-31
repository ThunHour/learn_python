marks = int(input("Enter your mark: "))

try:
    if marks > 100:
        raise ArithmeticError #create your own error (your own error which you can trow expection)
        
except ArithmeticError:
    print("Your score must be lower or equal to 100")