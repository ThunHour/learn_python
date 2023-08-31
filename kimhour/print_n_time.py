
def pint_n_time(name,n):
    print(name,'<==>',n)
    if n==1 :
        quit()
    pint_n_time(name,n-1)

print(pint_n_time('hour',5))
