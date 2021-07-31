def fibo(x):
    # [1, 1, 2, 3, 5, 8, 13]
    if x == 1 or x == 2:
        return 1
    i = 3
    first, second = 1, 1
    res = 0
    while i <= x:
        res = first + second
        first, second = second, res
        i += 1
    return res


print(fibo(6))
