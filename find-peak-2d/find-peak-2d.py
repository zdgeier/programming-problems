import sys

def findpeak2d(arr):
    first = 0
    last = len(arr[0])
    while True:
        col = (first + last) // 2

        max_col_val = -sys.maxsize - 1
        max_index = -1
        for row in range(len(arr)):
            if arr[row][col] > max_col_val:
                max_col_val = arr[row][col]
                max_index = row
        
        if max_col_val < arr[max_index][col - 1]:
            last = col - 1
        elif col + 1 < len(arr[0]) and max_col_val < arr[max_index][col + 1]:
            first = col + 1
        else:
            return "[{}][{}]: {}".format(max_index, col, arr[max_index][col])


def findpeak(arr):
    first = 0
    last = len(arr)

    while True:
        mid = (first + last) // 2
        if mid + 1 < len(arr) and arr[mid] < arr[mid + 1]:
            first = mid + 1
        elif arr[mid] < arr[mid - 1]:
            last = mid - 1
        else:
            return mid

arr = []
for line in sys.stdin:
    subarr = list(map(int, line.split()))
    arr.append(subarr)

print(findpeak2d(arr))
