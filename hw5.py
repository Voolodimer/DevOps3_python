# 1. После запуска предлагает пользователю ввести неотрицательные целые числа,
# разделенные через пробел и ожидает ввода от пользователя.
# 2. Находит наименьшее положительное число, не входящее в данный пользователем
# список чисел и печатает его.

input_list = sorted([int(x) for x in input().split()])
i = 0
min_num = input_list[0]
while i < len(input_list):
    if min_num not in input_list:
        print(min_num)
        break
    min_num += 1