a = [100, 10, 90, 20, 80, 30, 70, 40, 60, 50]
k = int(input("Enter the kth element: "))

def kthSmallestElement(arr, k):
    max_heap = []
    for num in arr:
        max_heap.append(-num)
        if len(max_heap)>k:
            max_heap.pop()
    return -(max_heap[-1])

print(kthSmallestElement(a,k))