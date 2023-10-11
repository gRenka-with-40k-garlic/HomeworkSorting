import random

array = [random.randint(1, 100) for _ in range(100)]


def sort_values(arr):
    even_values = [value for value in arr if value % 2 == 0]
    odd_values = [value for value in arr if value % 2 != 0]

    even_values.sort()
    odd_values.sort(reverse=True)

    sorted_values = even_values + odd_values

    return sorted_values


def sort_indices(arr):
    indices = list(range(len(arr)))

    even_indices = [i for i in indices if i % 2 == 0]
    odd_indices = [i for i in indices if i % 2 != 0]

    even_indices.sort()
    odd_indices.sort(reverse=True)

    sorted_indices = even_indices + odd_indices

    return sorted_indices


sorted_values = sort_values(array)
print("Отсортированные значения:", sorted_values)

sorted_indices = sort_indices(array)
print("Отсортированные индексы:", sorted_indices)
