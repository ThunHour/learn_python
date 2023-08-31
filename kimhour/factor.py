def print_factor (n):
    if n==0 or n==1 :
        return 1
    else:
        return n*(print_factor(n-1))

print(print_factor(5))
