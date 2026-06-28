
"""
Sort the array first so smaller values are handled before larger values.

To make the array valid:
1. The first element must be 1.
2. Every next element can be at most previous element + 1.

Since we are only allowed to decrease values, for each arr[i],
we keep it as large as possible while still satisfying the rule:

    arr[i] = min(arr[i], arr[i - 1] + 1)

This greedy choice builds the largest possible valid maximum element.

Time: O(n log n), because of sorting.
Space: O(1) extra space, ignoring the sorting implementation.
"""
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i-1] + 1)
        
        return arr[-1]
        
