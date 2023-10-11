import random

arr = [random.randint(1, 100) for _ in range(100)]


def func_sort_array(arr):
    even = [x for x in arr if x % 2 == 0]
    odd = [x for x in arr if x % 2 != 0]

    even.sort()
    odd.sort(reverse=True)

    sorted_arr = even + odd
    return sorted_arr


sorted_arr = func_sort_array(arr)
print(sorted_arr)
