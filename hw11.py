# Напишите функцию letters_range, которая ведет себя
# похожим на range образом, однако в качестве start и
# stop принимает не числа, а буквы латинского алфавита
# (в качестве step принимает целое число) и возращает
# не перечисление чисел, а список букв, начиная с
# указанной в качестве start, до указанной в качестве
# stop с шагом step (по умолчанию равным 1).

def letters_range(start, stop, step=None):
    if step is None:
        print([chr(ch) for ch in range(ord(start), ord(stop))])
    else:
        print([chr(char) for char in range(ord(start), ord(stop), step)])


letters_range('a', 'h')


