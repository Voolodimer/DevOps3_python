# 1. После запуска предлагает пользователю ввести текст.
# 2. Проверяет и, если возможно, преобразовывает полученный текст в число,
# используя рекурсивную функцию.
# Если число четное - делит его на 2 и выводит результат.
# Если число нечетное - умножает на 3 и прибавляет 1.
# После чего ждет следующего ввода.
# 3.При получении в качестве вводных данных 'cancel' завершает свою работу.

def check_sym(test_str, position, str_length):
    if position == str_length:
        print(int(test_str) // 2 if int(test_str) % 2 == 0 else int(test_str) * 3 + 1)
        return
    if '0' <= test_str[position] <= '9':
        position += 1
        check_sym(test_str, position, str_length)
    else:
        if test_str == 'cancel':
            print('Bye!')
            return
        print('Не удалось преобразовать введенный текст в число.')


input_list = input()
check_sym(input_list, 0, len(input_list))
