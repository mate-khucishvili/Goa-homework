def remove_duplicates(input_list):
    saboloo_list = []

    for i in input_list:
        if i not in saboloo_list:
            saboloo_list.append(i)

    return saboloo_list

my_list = [10, 43, 12, 11, 94, 10, 55, 7, 11]
result = remove_duplicates(my_list)
print(result)