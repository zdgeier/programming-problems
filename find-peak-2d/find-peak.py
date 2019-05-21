try: 
    while True:
        nums = list(map(int, input().split()))
        first = 0
        last = len(nums) - 1
        while True:
            mid = (first + last) // 2
            if mid != 0 and nums[mid] < nums[mid - 1]:
                # left
                last = mid - 1
            elif mid != len(nums) - 1 and nums[mid] < nums[mid + 1]:
                # right
                first = mid + 1
            else:
                # found
                print(mid)
                break
except:
    pass
