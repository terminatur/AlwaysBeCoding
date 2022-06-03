# Runtime: O(n log(n))
# Space: O(n)


from typing import List


def merge(a: List[int], b: List[int]) -> List[int]:
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a

    if a[0] <= b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])


def sort(data: List[int]) -> List[int]:
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    data_left = data[:mid]
    data_right = data[mid:]

    left_sorted = sort(data_left)
    right_sorted = sort(data_right)

    merged = merge(left_sorted, right_sorted)

    return merged


data = [4, 2, 5, 1, 6, 2, 3, 6, 8]
print(sort(data))