import sys

mylist=[11,22,33,44,55,"hour"]
mytuple=(11,22,33,44,55,"hour")
myset={11,22,33,44,55,"hour"}

if sys.getsizeof(mylist)>sys.getsizeof(mytuple):
    if sys.getsizeof(mylist)>sys.getsizeof(myset):
        print('list is bigger')
    else:
        print('set is bigger')
else:
    if sys.getsizeof(mytuple)>sys.getsizeof(myset):
        print('tuple is bigger')
    else:
        print('set is bigger')
