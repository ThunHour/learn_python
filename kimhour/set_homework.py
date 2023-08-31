googleAccHolder = {"Somphors", "Kimhour", "Sothea", "Sovann", "Kimsours"}
fbAccHolder = {"Vatana", "Kimhour", "Sothea", "Ratana", "Hinayo", "Ryuto"}
msAccHolder = {"Ryuto", "Kimhour", "Piseth", "Ratana", "Hinayo"}

#People_who_has_both msAcc and fbAcc
msAndFbAccHolder = fbAccHolder.intersection(msAccHolder)

#Combine of People who has both msAcc and fbAcc with People who has googleAcc
combinePeople = msAndFbAccHolder.union(googleAccHolder)
print(f"Combination of people who have google acc and people who have both Fb and Ms acc: {combinePeople}")



