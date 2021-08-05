#!/usr/bin/python3
from functools import reduce

# # Problem 6 Разница между квадратом суммы и суммы квадратов чисел от 1 до 100
print('Problem 6:', sum([x for x in range(1, 101)]) ** 2 - sum([x*x for x in range(1, 101)]))
# # Problem 9 There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
print('Problem 9:', [(a * b * c) for a in range(0, 1001, 5) for b in range(0, 1001, 5) for c in range(0, 1001, 5) if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2 and a > 0 and b > 0][0])
# # Problem 40 If dn represents the nth digit of the fractional part, find the value of the following expression.
# # d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
print('Problem 40:', reduce(lambda x, y: int(x) * int(y), [''.join([str(a) for a in range(1, 200001)])[b - 1] for b in (1, 10, 100, 1000, 10000, 100000, 1000000)]))
# # Problem 48
print('Problem 48:', sum(pow(i, i) for i in range(1, 1001)) % 10000000000)



# Problem 9
# print([(a * b * c) for a in range(1, 1001) for b in range(1, 1001) for c in range(1, 1001) if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2][0])



