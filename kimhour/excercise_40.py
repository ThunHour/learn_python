import itertools

def all_passwords(chars,length):

    passwords = [''.join(i) for i in itertools.product(chars, repeat=length)]

    new_passwords=(sorted(passwords))

    return new_passwords

print(all_passwords("AAAABC6789", 3));