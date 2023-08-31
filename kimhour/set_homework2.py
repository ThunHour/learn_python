googleAccHolder = {"Somphors", "Kimhour", "Sothea", "Sovann", "Kimsours"}
fbAccHolder = {"Vatana", "Kimhour", "Sothea", "Ratana", "Hinayo", "Ryuto"}
msAccHolder = {"Ryuto", "Kimhour", "Piseth", "Ratana", "Hinayo"}


#People who only use google
googleAccHolderOnly = googleAccHolder - fbAccHolder
print(f"People who have only google acc: {googleAccHolderOnly}")

#People who only use fb

fbAccHolderOnly = fbAccHolder - googleAccHolder
print(f"People who have only Fb acc: {fbAccHolderOnly}")


# #people who have both google and facebook acc
# googleAndFbAccHolder = googleAccHolder.intersection(fbAccHolder)
# print(googleAndFbAccHolder)
#
# #People who only have Acc in google not in fb
# googleAccHolderOnly = googleAccHolder.difference(googleAndFbAccHolder)
# print(f"People who have google acc and don't have Fb acc:  {googleAccHolderOnly}")
#
#
# FbAccHolderOnly =fbAccHolder.difference(googleAccHolder)
# print(f"People who have Fb acc and don't have Google acc: {FbAccHolderOnly}")


