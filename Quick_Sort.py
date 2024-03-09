def qs(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        qs(arr, low, pi - 1)
        qs(arr, pi + 1, high)
def partition(arr, low, high):
    i = low
    j = high
    pivot = arr[low]
    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j
arr = [3, 56, 1, 54, 12, 4]
qs(arr, 0, len(arr) - 1)
print(arr)

