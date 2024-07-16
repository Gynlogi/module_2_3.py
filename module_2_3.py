my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    List = my_list[i]
    if List < 0:
        break
    if List == 0:
        i = i + 1
        continue
    if List > 0:
        print(List)
        i += 1





