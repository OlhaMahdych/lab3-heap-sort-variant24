def heapify(arr, n, i, counters):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        counters["comparisons"] += 1
        if arr[left] > arr[largest]:
            largest = left

    if right < n:
        counters["comparisons"] += 1
        if arr[right] > arr[largest]:
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        counters["assignments"] += 3
        heapify(arr, n, largest, counters)

def heap_sort(arr):
    n = len(arr)
    counters = {"comparisons": 0, "assignments": 0}

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, counters)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        counters["assignments"] += 3
        heapify(arr, i, 0, counters)

    return arr, counters

A = [53, 5, 44, 47, 35, 83, 82, 85, 28]
sorted_A, c = heap_sort(A.copy())

print("Відсортований масив:", sorted_A)
print("Порівнянь:", c["comparisons"])
print("Присвоєнь:", c["assignments"])
