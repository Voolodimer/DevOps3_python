def celsium_farenheit_conv(temp, scale):
    if scale.lower() == 'f':
        return f'{(temp - 32) * 5/9} C'
    if scale.lower() == 'c':
        return f'{(temp * 9/5) + 32} F'


# print(celsium_farenheit_conv(1000, 'f'))
# print(celsium_farenheit_conv(1000, 'c'))
