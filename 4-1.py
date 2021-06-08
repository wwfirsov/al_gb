"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""

import timeit

def func_1(nums):
    # O(n) - линейная сложность
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    # O(n) - линейная сложность
    return [i for i, el in enumerate(nums) if el % 2 == 0]


#1000

nums = [el for el in range(1000)]

print(
    timeit.timeit(
        "func_1(nums[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_2(nums[:])",
        globals=globals(),
        number=1000))

#10000

nums = [el for el in range(10000)]

print(
    timeit.timeit(
        "func_1(nums)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_2(nums)",
        globals=globals(),
        number=1000))

#100000

nums = [el for el in range(100000)]

print(
    timeit.timeit(
        "func_1(nums)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_2(nums)",
        globals=globals(),
        number=1000))