# uer_input_first=int(input("Enter first number: "))
# uer_input_last=int(input("Enter last number:"))
# for i in range(uer_input_first,uer_input_last+1):
#     for x in range(1,11):
#         print(f"{i} x {x} = {i*x}")
#     print("*"*50)

# user_input_cube=int(input("Enter number (n value):"))
# sum_series=0
# for i in range(1,user_input_cube):
#     sum_series+=(i**3)
# print(f"The sum series of cube value of n = {user_input_cube} is {sum_series}")

# list_khmer=["","ក","ខ","គ","ឃ","ង","ច","ឆ","ជ","ឈ","ញ","ដ","ឋ","ឌ","ឍ","ណ","ត","ថ","ទ","ធ","ន","ប","ផ","ព","ភ","ម","យ","រ","ល","វ","ស","ហ","ឡ","អ"]
# list_second=["","ក","ខ","គ","ឃ","ង","ច","ឆ","ជ","ឈ","ញ","ដ","ឋ","ឌ","ឍ","ណ","ត","ថ","ទ","ធ","ន","ប","ផ","ព","ភ","ម","យ","រ","ល","វ","ស","ហ","ឡ","អ"]
# row_input=int(input("Enter the row:"))
# khmer_letter=input("សូម​ បញ្ចូល អក្សរ ខ្មែរ :")
# row_input=row_input+1
# for i in range(1,row_input):
#     for k in range(1,row_input-i):
#         print(" ",end="")
#     check=i
#     counter=2
#     check_letter=list_khmer.index(khmer_letter)
#     for j in range(1,(2*i-1)+1):
#         if j == check+1 and i!=1:
#             print(f" {list_second[(j-counter)+check_letter-1]}",end="")
#             check+=1
#             counter+=2
#         else:
#             print(f" {list_khmer[j+check_letter-1]}",end="")
#     print("\n")
