import random
import time

def generate_array(amount: int, array_size: int):
    for __ in range(amount):
        yield [random.randint(-100,100) for _ in range(array_size)]


def test(algoritm):
    for arr in generate_array(100, 100):
        start = time.time()
        assert algoritm(arr) == sorted(arr)
        print(f"Time: {(time.time() - start) * 1000} ms")


