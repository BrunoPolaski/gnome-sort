import random


def generate_array(amount: int, array_size: int):
    for __ in range(amount):
        yield [random.randint(-100, 100) for _ in range(array_size)]


def generate_ordered_array(amount: int, array_size: int):
    for __ in range(amount):
        yield list(range(array_size))


def generate_reversed_array(amount: int, array_size: int):
    for __ in range(amount):
        yield list(range(array_size, 0, -1))


def generate_almost_ordered_array(amount: int, array_size: int):
    for __ in range(amount):
        array = list(range(array_size))
        array[-1], array[-2] = array[-2], array[-1]
        yield array
