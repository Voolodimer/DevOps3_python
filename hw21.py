"""
hw21 A generator
"""
#!/usr/bin/python3

# Написать функцию-генератор, которая объединяет два отсортированных итератора.
# Результирующий итератор должен содержать последовательность в которой содержаться
# все элементы из каждой коллекции, в упорядоченном виде.

# list(merge((x for x in range(1,4)),(x for x in range(2,5)))) == [1,2,2,3,3,4]


def merge(nums1, nums2):
    """ Generator combining two variable length lists """
    def check_iter(iter_obj):
        """ res = next(iter_obj) or None """
        try:
            res = next(iter_obj)
        except StopIteration:
            res = None
        return res

    first_iter, second_iter = next(nums1), next(nums2)

    while first_iter or second_iter:
        # Если оба итератора не None - работаем
        if first_iter and second_iter:
            if first_iter >= second_iter:
                yield second_iter
                second_iter = check_iter(nums2)

            elif first_iter < second_iter:
                yield first_iter
                first_iter = check_iter(nums1)

        # Если первый итератор не пуст, а второй пуст
        elif first_iter and not second_iter:
            while first_iter:
                yield first_iter
                first_iter = check_iter(nums1)

        # Если второй итератор не пуст, а первый пуст
        elif second_iter and not first_iter:
            while second_iter:
                yield second_iter
                second_iter = check_iter(nums2)


# Test
a = merge((x for x in range(1, 4)), (x for x in range(2, 5)))
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(list(a))
a = merge((x for x in range(11, 25, 3)), (x for x in range(13, 24, 2)))
print(list(a))
