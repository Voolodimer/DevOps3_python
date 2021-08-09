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
    def add_arr(mass, pos):
        if pos < len(cond_list):
            return add_arr([mass for x in range(cond_list[pos])], pos + 1)
        else:
            return mass
    position = 0
    res = add_arr(['\"\"' for j in range(cond_list[position])], position + 1) if len(cond_list) > 0 else []
    return res


print(n_arr([]))
print(n_arr([4]))
print(n_arr([2, 2]))
print(n_arr([2, 3, 4]))
print(n_arr([2, 3, 4, 5]))

