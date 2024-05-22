# count the number of inversions in an array

NUM_INV = 0

def merge(arr, left, mid, right):
    global NUM_INV
    n1 = mid - left
    n2 = right - mid
    left_arr = [arr[i] for i in range(left, mid)]
    right_arr = [arr[i] for i in range(mid, right)]
    left_arr.append(float('inf'))
    right_arr.append(float('inf'))
    i, j = 0, 0
    for k in range(left, right):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            NUM_INV += mid - left - i
            arr[k] = right_arr[j]
            j += 1

def merge_sort(arr, left, right):
    if len(arr) <= 1:
        return arr
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)

with open("100k_integers.txt", 'r') as file:
    file_content = file.read()
    arr = [int(num) for num in file_content.split()]
merge_sort(arr, 0, len(arr))
print(NUM_INV)