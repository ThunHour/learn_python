my_first_list = [40, 50, 60, 70, 80]
my_second_list = ["Rith", "Zass", "Pisey", "sreyling", "GG","TT"]

print(my_first_list)

print(my_first_list[0:])
print(my_first_list[0:-1])

#combine two lists
combine_list = my_first_list, my_second_list
print(combine_list)

print(combine_list[0][0:4])
print(combine_list[1][-3][0:-1:2])

#reverse
print(combine_list[1][-3][::-1])
