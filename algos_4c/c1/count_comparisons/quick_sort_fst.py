

def quicksort(arr, left, right, pivot_type):
    if left >= right:
        return 0
    comp = right - left
    pivot_idx = choose_pivot(arr, left, right, pivot_type)
    arr[left], arr[pivot_idx] = arr[pivot_idx], arr[left]
    pivot_final_index = partition(arr, left, right)
    comp += quicksort(arr, left, pivot_final_index - 1, pivot_type)
    comp += quicksort(arr, pivot_final_index + 1, right, pivot_type)
    return comp

def choose_pivot(arr, left, right, pivot_type):
    if pivot_type == 'first':
        return left
    elif pivot_type == 'last':
        return right
    elif pivot_type == 'median':
        mid = (left + right) // 2
        candidates = [(arr[left], left), (arr[mid], mid), (arr[right], right)]
        candidates.sort(key=lambda x: x[0])
        return candidates[1][1]

def partition(arr, left, right):
    pivot = arr[left]
    i = left + 1
    for j in range(left + 1, right + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[left], arr[i - 1] = arr[i - 1], arr[left]
    return i - 1

# read numbers from the file
with open('10k_unsorted_int.txt') as f:
    array = list(map(int, f.readlines()))

# quicksort with different pivot types
comp_first = quicksort(array.copy(), 0, len(array) - 1, 'first')
comp_last = quicksort(array.copy(), 0, len(array) - 1, 'last')
comp_median = quicksort(array.copy(), 0, len(array) - 1, 'median')

print(f"Sort with first element as pivot: {comp_first}")
print(f"Sort with last element as pivot: {comp_last}")
print(f"Sort with the median as pivot: {comp_median}")
