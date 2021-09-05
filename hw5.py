#!/usr/bin/python3

# 1. После запуска предлагает пользователю ввести неотрицательные целые числа,
# разделенные через пробел и ожидает ввода от пользователя.
# 2. Находит наименьшее положительное число, не входящее в данный пользователем
# список чисел и печатает его.

def hw5():
    print('Введите список чисел: ')
    input_list = sorted((int(x) for x in input().split()))
    i = 0
    # print(input_list)
    min_num = input_list[0]
    if min_num > 1:
        return min_num - 1
    while i <= len(input_list):
        if min_num not in input_list:
            return min_num
        i += 1
        min_num += 1



print(hw5())
