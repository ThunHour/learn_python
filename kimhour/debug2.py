#Homework_1
def merge(l1, l2):
    #"""Merge the sorted lists into a new, single list."""
    i = j = 0
    out = []
    while True:
        if i == len(l1):
            out.extend(l2[j:])
            break
        elif j == len(l2):
            out.extend(l1[i:])
            break
        elif l1[i] <= l2[j]:
            out.append(l1[i])
            i += 1
        else:
            out.append(l2[j])
            j += 1
    return out

print(merge([5,12,13,18],[7,11,14,18,19,20,21]))
print(merge([5,7,13,18,21,23,24],[7,11,14,18,19]))
print(merge([5,12,13,18,20],[7,11,14,18,21]))

#5,7,11,12,13,14,18,21,23,24


