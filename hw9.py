# Problem 6 Разница между квадратом суммы и суммы квадратов чисел от 1 до 100
print(sum([x for x in range(1, 101)]) ** 2 - sum([x*x for x in range(1, 11)]))
# Problem 9
# [print(x, ((x * x) + (x + 1) * (x + 1)), ((x + 2) * (x + 2))) for x in range(1, 10000000000100) if ((x * x) + (x + 1) * (x + 1)) == ((x + 2) * (x + 2))]
# Problem 40

# Problem 48
ans = sum(pow(i, i) for i in range(1, 1001)) % 10000000000
