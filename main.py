import random

array = [random.randint(1, 100) for _ in range(100)]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def inverse_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def sort_values(arr):
    even_values = [value for value in arr if value % 2 == 0]
    odd_values = [value for value in arr if value % 2 != 0]

    new_even_values = insertion_sort(even_values)
    new_odd_values = inverse_insertion_sort(odd_values)

    sorted_values = new_even_values + new_odd_values

    return sorted_values


def sort_indices(arr):
    indices = list(range(len(arr)))

    even_indices = [i for i in indices if i % 2 == 0]
    odd_indices = [i for i in indices if i % 2 != 0]

    new_even_indices = insertion_sort(even_indices)
    new_odd_indices = inverse_insertion_sort(odd_indices)

    sorted_indices = new_even_indices + new_odd_indices

    return sorted_indices

print("Сгенерированный массив:", array)

sorted_arr = insertion_sort(array)
print("Отсортированный массив:", sorted_arr)

sorted_val = sort_values(array)
print("Отсортированные значения:", sorted_val)

sorted_indices = sort_indices(array)
print("Отсортированные индексы:", sorted_indices)
