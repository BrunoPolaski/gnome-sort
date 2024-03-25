
def gnome_sort(arr:list) -> list:
    i = 0
    while i < len(arr):
        if i == 0:
            i += 1
        elif(arr[i] >= arr[i - 1]):
            i += 1
        elif(arr[i] < arr[i -1]):
            arr[i], arr[i -1] = arr[i -1], arr[i]
            i -= 1

    return arr


