# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


from typing import List
import heapq

class MaxHeap():
    def __init__(self, initialData = []) -> None:
        self.data = initialData
        heapq.heapify(self.data)

    def add(self, item, index):
        heapq.heappush(self.data, (-item, index))

    def popMax(self):
        item, index = heapq.heappop(self.data)
        return (-item, index)

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    heap = MaxHeap()

    for i in range(k):
        heap.add(nums[i], i)

    windowMaxes = [0] * (len(nums) - k + 1)
    left = 1

    windowMax, windowMaxIndex = heap.popMax()
    windowMaxes[0] = windowMax

    for i in range(k, len(nums)):
        while windowMaxIndex < left:
            windowMax, windowMaxIndex = heap.popMax()

        if nums[i] >= windowMax:
            windowMax = nums[i]
            windowMaxIndex = i
        else:
            heap.add(nums[i], i)
        
        windowMaxes[left] = windowMax
        left += 1

    
    print(windowMaxes)

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))