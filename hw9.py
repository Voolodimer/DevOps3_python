#!/usr/bin/python3
from functools import reduce

# Problem 6 Разница между квадратом суммы и суммы квадратов чисел от 1 до 100
print(sum([x for x in range(1, 101)]) ** 2 - sum([x*x for x in range(1, 11)]))
# Problem 9 There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
[print(a, b, c) for a in range(1, 1001) for b in range(1, 1001) for c in range(1, 1001) if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2]
# Problem 40

# Problem 48
print(sum(pow(i, i) for i in range(1, 1001)) % 10000000000)



