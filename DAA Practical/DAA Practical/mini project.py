import threading
import time
import random

# ----------- Standard Merge Sort -----------

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# ----------- Multithreaded Merge Sort -----------

def threaded_merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        t1 = threading.Thread(target=threaded_merge_sort, args=(left,))
        t2 = threading.Thread(target=threaded_merge_sort, args=(right,))

        t1.start()
        t2.start()
        t1.join()
        t2.join()

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# ----------- Time Measurement Function -----------

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# ----------- Main Program -----------

size = int(input("Enter number of elements to sort: "))

# Create Best Case (already sorted)
best_case = list(range(size))

# Create Worst Case (reverse sorted)
worst_case = list(range(size, 0, -1))

# Create Average Case (random)
average_case = [random.randint(1, 1000000) for _ in range(size)]


print("\n--- Merge Sort Timing ---")

# Best Case
array1 = best_case.copy()
time_best = measure_time(merge_sort, array1)
print(f"Normal Merge Sort - Best Case: {time_best:.4f} seconds")

# Worst Case
array1 = worst_case.copy()
time_worst = measure_time(merge_sort, array1)
print(f"Normal Merge Sort - Worst Case: {time_worst:.4f} seconds")

# Average Case
array1 = average_case.copy()
time_avg = measure_time(merge_sort, array1)
print(f"Normal Merge Sort - Average Case: {time_avg:.4f} seconds")


print("\n--- Multithreaded Merge Sort Timing ---")

# Best Case
array2 = best_case.copy()
time_best_mt = measure_time(threaded_merge_sort, array2)
print(f"Multithreaded Merge Sort - Best Case: {time_best_mt:.4f} seconds")

# Worst Case
array2 = worst_case.copy()
time_worst_mt = measure_time(threaded_merge_sort, array2)
print(f"Multithreaded Merge Sort - Worst Case: {time_worst_mt:.4f} seconds")

# Average Case
array2 = average_case.copy()
time_avg_mt = measure_time(threaded_merge_sort, array2)
print(f"Multithreaded Merge Sort - Average Case: {time_avg_mt:.4f} seconds")
