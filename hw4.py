# Встроенная функция input позволяет ожидать и возвращать данные из стандартного
# ввода ввиде строк (весь введенный пользователем текст до нажатия им enter).
# Используя данную функцию, напишите программу, которая:
#
# 1. После запуска предлагает пользователю ввести целые неотрицательные числа,
# разделенные любым не цифровым литералом (пробел, запятая, %, буква и т.д.).
# 2. Получив вводные данные, выделяет полученные числа, суммирует их,
# и печатает полученную сумму.

input_list = input()

len_str = len(input_list)
integ = []
is_negative = False
i = 0
while i < len_str:
    s_int = ''
    a = input_list[i]
    if a == '-' and (i + 1) < len_str and '0' <= input_list[i + 1] <= '9':
        is_negative = True
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < len_str:
            a = input_list[i]
        else:
            break
    i += 1
    if s_int != '':
        if is_negative:
            integ.append(int(s_int) * -1)
            is_negative = False
        else:
            integ.append(int(s_int))

print(sum(integ))