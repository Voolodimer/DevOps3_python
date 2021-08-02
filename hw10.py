
def find_steps(number):
    global n
    if number % 2 == 0:
        number = number // 2
        n += 1
        if number == 1:
            return
        find_steps(number)
    else:
        number = number * 3 + 1
        n += 1
        find_steps(number)


n = 0

# для каждого 10-го числа от 1 до 100
for i in range(1, 100, 10):
    find_steps(i)
    print(n)
    n = 0

