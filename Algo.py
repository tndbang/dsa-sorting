import time, os

# Code QuickSort
def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1


def QuickSort(arr, l, r):
    # Chia để trị
    if l < r:
        p = partition(arr, l, r)
        QuickSort(arr, l, p - 1)
        QuickSort(arr, p + 1, r)

# Code HeapSort
def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def HeapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Code MergeSort
def merge(left, right):
    res = []
    i = j = 0

    # thao tác trên 2 phần
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])
    return res

def MergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])

    return merge(left, right)

print("Lựa chọn khảo soát:\n"
      "1/ QuickSort       \n"
      "2/ HeapSort        \n"
      "3/ MergeSort       \n"
      "4/ Sort(Numpy)")
type = input("Lựa chọn: ")
base = os.path.dirname(__file__) # đường dẫn hiện t

for i in range(1, 11):
    start = time.time()                                 # thời gian bắt đầu
    f = open(os.path.join(base, "test", f"test{i}.txt"), "r")
    arr = [float(x) for x in f.read().split()]
    if (type == 1): QuickSort(arr, 0, len(arr))  
    if (type == 2): HeapSort(arr)
    if (type == 3): MergeSort(arr)
    if (type == 4): arr.sort()
    end = time.time()                                   # thời gian kết thúc
    print("test ", i, "chạy hết ", int((end - start) * 1000), "ms")




