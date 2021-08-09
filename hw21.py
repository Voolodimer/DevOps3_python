#!/usr/bin/python3

# Написать функцию-генератор, которая объединяет два отсортированных итератора.
# Результирующий итератор должен содержать последовательность в которой содержаться
# все элементы из каждой коллекции, в упорядоченном виде.

# list(merge((x for x in range(1,4)),(x for x in range(2,5)))) == [1,2,2,3,3,4]

def merge(nums1, nums2):
    nums1 = list(nums1)
    nums2 = list(nums2)
    nums1.extend(nums2)
    nums1.sort()
    for el in nums1:
        yield el


# Test
a = merge((x for x in range(1, 4)), (x for x in range(2, 5)))
print(a)
print(next(a))
print(next(a))
print(next(a))
print(list(a))
a = merge((x for x in range(1, 4)), (x for x in range(2, 5)))
print(list(a))
