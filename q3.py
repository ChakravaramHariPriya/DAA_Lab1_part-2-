import heapq

def find_k_largest(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)

    for i in range(k, len(arr)):
        if arr[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, arr[i])

    return heap

arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
k = int(input("Enter the value of K: "))

k_largest = find_k_largest(arr, k)
print("K largest elements:", k_largest)
