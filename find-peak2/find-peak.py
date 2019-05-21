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


while True:
    arr = list(map(int, input().split()))
    print(findpeak(arr))
