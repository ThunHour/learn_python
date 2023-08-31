#first method
import array as arr
from collections import Counter
a = arr.array('i',[12,32,41,42,11])
print(a)

#second method
import array
a=array.array('i',[12,32,41,42,11])
print(a)

#third method
from array import *   
number = array('i', [1, 2, 3, 3, 4])
new_array=array(number.typecode,(a for a in number))
number.append(12) #add element into array
number.pop(1)#delete a element of array
number.remove(12)#delete a element of array
del number[-1] #delete a element of array
# del number #how to remove a array
number[0]=100
print(number)
print(f'new array : {new_array}')
