age = int(input('Input your age:'))

if age < 0:
    print("Age must  be a positive digit")
else:
    if age >= 18:
        print("You are eligible to  vote")
    else:
          if age < 18:
            print("You aren't adult yet... Sorry can't vote")
