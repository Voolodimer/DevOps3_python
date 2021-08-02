# https://projecteuler.net/problem=36
#
# The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2. (Please note that the palindromic number,
# in either base, may not include leading zeros.)
#
# Напишите программу, которая решает описанную выше задачу и печатает ответ.

def find_base10_palindrom(number):
    number = str(number)
    return number == number[::-1]
    # number = str(number)
    # i = 0
    # j = len(number) - 1
    # while i <= j:
    #     if number[i] != number[j]:
    #         return False
    #     i += 1
    #     j -= 1
    # return True


def find_base2_palindrom(number):
    number = str(bin(number)[2:])
    return number == number[::-1]
    # number = bin(number)[2:]
    # i = 0
    # j = len(number) - 1
    # if number[0] == '1' and number.count('1') == 1:
    #     return True
    #
    # while i <= j:
    #     if number[i] != number[j]:
    #         return False
    #     i += 1
    #     j -= 1
    # return True


i = 0
res_sum = 0

while i < 1000000:
    if find_base10_palindrom(i) and find_base2_palindrom(i):
        res_sum += i
        # print(i)
    i += 1

print(res_sum)
