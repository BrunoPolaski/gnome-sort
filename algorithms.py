import json
import time
import threading
from mock import (
    generate_ordered_array,
    generate_reversed_array,
    generate_almost_ordered_array,
    generate_array,
)


def gnome_sort(arr: list[int]) -> list:
    i = 0
    while i < len(arr):
        if i == 0:
            i += 1
        elif arr[i] >= arr[i - 1]:
            i += 1
        elif arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

    return arr


def yield_gnome_sort(arr: list[int]):

    indexes = {}
    i = 0
    while i < len(arr):
        if i == 0:
            i += 1
        elif arr[i] >= arr[i - 1]:
            i += 1
        elif arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

        for index, item in enumerate(arr):
            indexes[str(index)] = item
        indexes["i"] = i
        yield indexes
        indexes = {}


def reverse_gnome_sort(arr: list[int]) -> list:
    i = 0
    while i < len(arr):
        if i == 0:
            i += 1
        elif arr[i] <= arr[i - 1]:
            i += 1
        elif arr[i] > arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

    return arr


def yield_reverse_gnome_sort(arr: list[int]):
    indexes = {}
    i = 0
    while i < len(arr):
        if i == 0:
            i += 1
        elif arr[i] <= arr[i - 1]:
            i += 1
        elif arr[i] > arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

        for index, item in enumerate(arr):
            indexes[str(index)] = item
        indexes["i"] = i
        yield indexes
        indexes = {}


def generate_mesures():
    random_unsorted_mesures = []
    ordered_asc_mesures = []
    ordered_desc_mesures = []
    almost_ordered_mesures = []

    array_sizes = [100, 1000, 10_000, 100_000, 1_000_000]

    def random_unsorted_mesure():
        print("random_unsorted_mesure -> started")
        for index, size in enumerate(array_sizes):
            for array in generate_array(1, size):
                start = time.time()
                gnome_sort(array)
                end = time.time()

                random_unsorted_mesures.append(
                    {
                        "size": size,
                        "time_in_seconds": (end - start),
                    }
                )

                print("random_unsorted_mesure -> done for size", size)

            with open("mesures/random_unsorted_mesures.json", "w+") as file:

                file.write(
                    json.dumps(
                        random_unsorted_mesures,
                        indent=4,
                    )
                )

    def ordered_asc_mesure():
        print("ordered_asc_mesure -> started")
        for index, size in enumerate(array_sizes):
            for array in generate_ordered_array(1, size):
                start = time.time()
                gnome_sort(array)
                end = time.time()

                ordered_asc_mesures.append(
                    {
                        "size": size,
                        "time_in_seconds": (end - start),
                    }
                )

                print("ordered_asc_mesure -> done for size", size)

            with open("mesures/ordered_asc_mesures.json", "w+") as file:
                file.write(
                    json.dumps(
                        ordered_asc_mesures,
                        indent=4,
                    )
                )

    def ordered_desc_mesure():
        print("ordered_desc_mesure -> started")
        for index, size in enumerate(array_sizes):
            for array in generate_reversed_array(1, size):
                start = time.time()
                gnome_sort(array)
                end = time.time()

                ordered_desc_mesures.append(
                    {
                        "size": size,
                        "time_in_seconds": (end - start),
                    }
                )

                print("ordered_desc_mesure -> done for size", size)

            with open("mesures/ordered_desc_mesures.json", "w+") as file:
                file.write(
                    json.dumps(
                        ordered_desc_mesures,
                        indent=4,
                    )
                )

    def almost_ordered_mesure():
        print("almost_ordered_mesure -> started")
        for index, size in enumerate(array_sizes):
            for array in generate_almost_ordered_array(1, size):
                start = time.time()
                gnome_sort(array)
                end = time.time()

                almost_ordered_mesures.append(
                    {
                        "size": size,
                        "time_in_seconds": (end - start),
                    }
                )

                print("almost_ordered_mesure -> done for size", size)

            with open("mesures/almost_ordered_mesures.json", "w+") as file:
                file.write(
                    json.dumps(
                        almost_ordered_mesures,
                        indent=4,
                    )
                )

    threads = [
        threading.Thread(target=random_unsorted_mesure),
        threading.Thread(target=ordered_asc_mesure),
        threading.Thread(target=ordered_desc_mesure),
        threading.Thread(target=almost_ordered_mesure),
    ]

    for thread in threads:
        thread.start()


if __name__ == "__main__":
    generate_mesures()
