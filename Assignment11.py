q1>def sqrt(x):
    if x == 0:
        return 0

    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

    return left - 1
q2>def findPeakElement(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid

    return left
q3>def missingNumber(nums):
    n = len(nums)
    missing = n

    for i, num in enumerate(nums):
        missing ^= i ^ num

    return missing
q4>def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    # Find the meeting point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Reset the slow pointer to the start
    slow = nums[0]

    # Find the entry point of the cycle
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
q5>def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return list(set1.intersection(set2))
q6>def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1

    return nums[left]
q7>def searchRange(nums, target):
    left = findLeft(nums, target)
    right = findRight(nums, target)
    return [left, right]


def findLeft(nums, target):
    left = -1
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
        if nums[mid] == target:
            left = mid

    return left


def findRight(nums, target):
    right = -1
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
        if nums[mid] == target:
            right = mid

    return right
q8>from collections import defaultdict

def intersect(nums1, nums2):
    freq_map = defaultdict(int)
    for num in nums1:
        freq_map[num] += 1

    result = []
    for num in nums2:
        if freq_map[num] > 0:
            result.append(num)
            freq_map[num] -= 1

    return result
