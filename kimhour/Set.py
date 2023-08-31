mySet = {70,21,45,23,24,55}
# To add elements
mySet.add(555)
print(mySet)

# to delete elemets
mySet.discard(21)
print(mySet)

print("*"* 50)


googleAccHolder = {"a","b","c","d","e","f"}
fbAccHolder = {"c","d","t","y","q","z"}
msAccHolder = {"a","b","c","q","f","e"}

print(googleAccHolder.intersection(fbAccHolder).intersection(msAccHolder))
