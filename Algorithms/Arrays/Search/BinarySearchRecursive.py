from typing import List


def binarySearchRecurseRange(nums: List[int], target: int, left: int, right: int) -> int:
    mid = (left + right) // 2
    midValue = nums[mid]

    # print(f'left: {left} right: {right} mid: {mid} midValue: {midValue}')

    if midValue == target:
        return mid

    if left >= right:
        return -1

    

    if target <= midValue:
        return binarySearchRecurseRange(nums, target, left, mid - 1)
    else:
        return binarySearchRecurseRange(nums, target, mid + 1, right)



def binarySearchRecursive(nums: List[int], target: int) -> int:
    return binarySearchRecurseRange(nums, target, 0, len(nums) - 1)

a = [1, 2, 3, 5, 6, 7, 9, 11]
print(binarySearchRecursive(a, 3)) # 2
print(binarySearchRecursive(a, 4)) # -1
print(binarySearchRecursive(a, 5)) # 3
print(binarySearchRecursive(a, 6)) # 4
print(binarySearchRecursive(a, 1)) # 0
print(binarySearchRecursive(a, 11)) # 7



