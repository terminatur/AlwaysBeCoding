# Runtime: O(n log(n))
# Space: O(1)


from typing import List


def quicksort(data: List[int], start: int, end: int) -> None:
    if start >= end:
        return

    pivot = end
    pivot_value = data[pivot]

    left = start
    right = end - 1

    while left < right:
        while data[left] < pivot_value and left < right:
            left += 1

        while data[right] >= pivot_value and left < right:
            right -= 1

        if left < right:
            temp = data[right]
            data[right] = data[left]
            data[left] = temp
            left += 1
            right -= 1

    if data[pivot] < data[left]:
        data[pivot] = data[left]
        data[left] = pivot_value

    quicksort(data, start, left - 1)
    quicksort(data, left + 1, end)

data = [2, 54,5, 1, 5, 8, 9, 0, 2]
quicksort(data, 0, len(data) - 1)
print(data)
        
