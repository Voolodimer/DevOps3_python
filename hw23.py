#!/usr/bin/python3

# Надо написать функцию которая возвращает N-мерный массив с ширинами заданными в аргументе списком из N элементов:
# n_arr([2,2])
# >> [[“”,“”],[“”,“”]]
# n_arr([2,2,2])
# >> [[[“”,“”],[“”,“”]], [[“”,“”],[“”,“”]]]


def n_arr(cond_list):
    """
    Recursive method for creating multidimensional arrays
    pos - position in condition list:
    :return: multidimensional array
    """
    def add_arr(pos):
        if pos < len(cond_list) - 1:
            return [add_arr(pos + 1) for x in range(cond_list[pos])]
        else:
            res_str = []
            i = 0
            while i < cond_list[pos]:
                res_str.append('\"\"')
                i += 1
            return res_str

    cond_list.reverse()
    if len(cond_list) == 1:
        return add_arr(0)
    else:
        res = [add_arr(1) for j in range(cond_list[0])] if len(cond_list) > 1 else []
    return res


print(n_arr([]))
print(n_arr([4]))
print(n_arr([2, 3, 4]))
print(n_arr([2, 2]))
print(n_arr([2, 3, 4]))
print(n_arr([2, 3, 4, 5]))

x = n_arr([2, 3, 4])
print(x[2][2])
print(x[3][2][0])
x[3][2][1] = 22
x[2][1][0] = 13
print(x)








