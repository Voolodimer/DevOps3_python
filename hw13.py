def celsium_farenheit_conv(temp, scale):
    if scale.lower() == 'f':
        return "%.2f C" % ((temp - 32) * 5/9)
        # f'{(temp - 32) * 5/9} C'
    elif scale.lower() == 'c':
        return "%.2f F" % ((temp * 9/5) + 32)
        # f'{(temp * 9/5) + 32} F'
    else:
        return 'Введите корректные данные'


# для каждого 10-го числа от 1 до 100
for i in range(1, 100, 10):
    print(celsium_farenheit_conv(i, 'f'))

# для каждого 10-го числа от 1 до 100
for i in range(1, 100, 10):
    print(celsium_farenheit_conv(i, 'c'))
