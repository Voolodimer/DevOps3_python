
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
find_steps(int(input()))
print(n)
