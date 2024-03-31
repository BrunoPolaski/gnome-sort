import random
import unittest
import algorithms

def generate_array(amount: int, array_size: int):
    for __ in range(amount):
        yield [random.randint(-100,100) for _ in range(array_size)]


class TestAlgorithm(unittest.TestCase):
    

    def test_gnome_sort(self):
        for array in generate_array(10, 100):
            self.assertEqual(algorithms.gnome_sort(array), sorted(array))


    def test_yield_gnome_sort(self):
        array = [3, 2, 1, 4]
        steps = [
            {
                "0": 3,
                "1": 2,
                "2": 1,
                "3": 4,
                "i": 1
            },
            {
                "0": 2,
                "1": 3,
                "2": 1,
                "3": 4,
                "i": 0
            },
            {
                "0": 2,
                "1": 3,
                "2": 1,
                "3": 4,
                "i": 1
            },
            {
                "0": 2,
                "1": 3,
                "2": 1,
                "3": 4,
                "i": 2
            },
            {
                "0": 2,
                "1": 1,
                "2": 3,
                "3": 4,
                "i": 1
            },
            {
                "0": 1,
                "1": 2,
                "2": 3,
                "3": 4,
                "i": 0
            },
            {
                "0": 1,
                "1": 2,
                "2": 3,
                "3": 4,
                "i": 1
            },
            {
                "0": 1,
                "1": 2,
                "2": 3,
                "3": 4,
                "i": 2
            },
            {
                "0": 1,
                "1": 2,
                "2": 3,
                "3": 4,
                "i": 3
            },
            {
                "0": 1,
                "1": 2,
                "2": 3,
                "3": 4,
                "i": 4
            }
        ]


        self.assertEqual(list(algorithms.yield_gnome_sort(array)), steps)

unittest.main()
