def gnome_sort(arr: list) -> list:
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


def yield_gnome_sort(arr: list):

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
        indexes['i'] = i
        yield indexes
        indexes = {}
