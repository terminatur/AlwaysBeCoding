# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:

# Input: nums = [1], target = 0
# Output: -1


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int, left, right) -> int:
        mid = (left + right) // 2
        midValue = nums[mid]
        print(f'left: {left}, right: {right}, mid: {mid}, midValue: {midValue}')
        
        if target == midValue:
            # found it
            return mid
        
        if left >= right:
            # does not exist
            return -1
        
        leftValue = nums[left]
        rightValue = nums[right]
        
        if midValue > rightValue:
            if target > midValue and target <= rightValue:
                return self.searchRange(nums, target, mid + 1, right)
            else:
                return self.searchRange(nums, target, left, mid - 1)
        else:
            if target < midValue and target >= leftValue:
                return self.searchRange(nums, target, left, mid - 1)
            else:
                return self.searchRange(nums, target, mid + 1, right)
        
        # if target <= midValue and target >= nums[left]:
        #     return self.searchRange(nums, target, left, mid)
        # elif target > midValue and target <= nums[right]:
        #     return self.searchRange(nums, target, mid, right)
        # else:
        #     return self.searchRange(nums, target, mid + 1, right)
    
    def search(self, nums: List[int], target: int) -> int:
        
        return self.searchRange(nums, target, 0, len(nums) - 1)
    
    
        # mid
        # if target < mid and target > left: search between these intervals
        # if target > mid and target < right: search between intervals


print(Solution().search([4,5,6,7,0,1,2], 0))