from typing import List


def binarySearchPointers(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        midValue = nums[mid]

        if midValue == target:
            return mid

        if target < midValue:
            right = mid - 1
        else:
            left = mid + 1

    return -1


a = [1, 2, 3, 5, 6, 7, 9, 11]
print(binarySearchPointers(a, 3)) # 2
print(binarySearchPointers(a, 4)) # -1
print(binarySearchPointers(a, 5)) # 3
print(binarySearchPointers(a, 6)) # 4
print(binarySearchPointers(a, 1)) # 0
print(binarySearchPointers(a, 11)) # 7