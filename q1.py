import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

random_numbers = [random.randint(1, 10000) for _ in range(1000)]

start_time = time.time()
bubble_sorted = bubble_sort(random_numbers.copy())
bubble_time = time.time() - start_time

start_time = time.time()
selection_sorted = selection_sort(random_numbers.copy())
selection_time = time.time() - start_time

start_time = time.time()
quick_sorted = quick_sort(random_numbers.copy())
quick_time = time.time() - start_time

start_time = time.time()
merge_sorted = merge_sort(random_numbers.copy())
merge_time = time.time() - start_time

labels = ['Bubble Sort', 'Selection Sort', 'Quick Sort', 'Merge Sort']
times = [bubble_time, selection_time, quick_time, merge_time]

plt.bar(labels, times)
plt.ylabel('Time (s)')
plt.title('Time taken by sorting algorithms')
plt.show()
