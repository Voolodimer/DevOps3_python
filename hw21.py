"""
hw21 A generator
"""
#!/usr/bin/python3

# Написать функцию-генератор, которая объединяет два отсортированных итератора.
# Результирующий итератор должен содержать последовательность в которой содержаться
# все элементы из каждой коллекции, в упорядоченном виде.

# list(merge((x for x in range(1,4)),(x for x in range(2,5)))) == [1,2,2,3,3,4]


def merge(nums1, nums2):
    """ A generator that combines two lists """
    nums1 = list(nums1)
    nums2 = list(nums2)

    while nums1 or nums2:
        if nums1 and nums2:
            if nums1[0] >= nums2[0]:
                yield nums2[0]
                nums2.remove(nums2[0])
            elif nums1[0] < nums2[0]:
                yield nums1[0]
                nums1.remove(nums1[0])
        elif nums1 and not nums2:
            while nums1:
                yield nums1[0]
                nums1.remove(nums1[0])
        elif nums2 and not nums1:
            while nums2:
                yield nums2[0]
                nums2.remove(nums2[0])


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
