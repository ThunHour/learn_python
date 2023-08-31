def dict_values (arugment):
    last_element = 1
    for key in arugment:

        res_list = list(map("".join, arugment[key]))
        string_list = " ".join((res_list))
        print(f"{key}: {string_list}")
        if last_element != len(arugment):
            print("*****")
        last_element +=1
dict_values(
    {
            120: ("Visal", "Borey", "Sovann"),
            130: ("Hout","Mouyleng","Pidor"),
            140: ("Nary", "Misora", "Masaaki"),
    })
