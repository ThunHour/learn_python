text1 = input("Input a string :")
text2 = text1[::-1]

half = len(text1) // 2
t_first, t_second = text2[:half], text1[half:]

if not text1:
  print("The string is empty")

else :
  print(t_first, t_second)
