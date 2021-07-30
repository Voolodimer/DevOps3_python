input_list = [x.lower() for x in input().split()]
res_dict = {}
max_el = 0

for el in input_list:
    if input_list.count(el) >= max_el:
        max_el = input_list.count(el)
        res_dict[el] = input_list.count(el)

for key in res_dict:
    if res_dict[key] == max_el:
        print(str(max_el) + ' ' + key)



