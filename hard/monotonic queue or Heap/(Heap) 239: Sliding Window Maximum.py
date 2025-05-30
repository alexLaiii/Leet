"""
Idea:
Use a Max Heap (via negated values) to ensure the maximum is always accessible at the top in O(1) time.
The heap does not strictly track which elements are in the current window — it may contain stale elements.
So we use **lazy deletion**: only check if the top element is valid (i.e., its index is within the current window)
*when* we actually need the max.

If the top element’s index is outside the current window (i.e., index ≤ i - k), we pop it.
Once a valid max is found, we append its value (negated back to positive) to the result.

Example: nums = [5,4,8,3,9,5,8,4,3,2,1], k = 3
Heap stores (-value, index) for max-heap simulation.

i = 0, window = [5], heap = [(-5, 0)]
i = 1, window = [5,4], heap = [(-5,0), (-4,1)]
i = 2, window = [5,4,8], heap = [(-8,2), (-5,0), (-4,1)]
        → Top is (-8,2): 2 ≥ 2 - 3 → valid → append 8

i = 3, window = [4,8,3], heap = [(-8,2), (-5,0), (-4,1), (-3,3)]
        → Top is (-8,2): 2 ≥ 3 - 3 → valid → append 8

i = 4, window = [8,3,9], heap = [(-9,4), (-8,2), (-5,0), (-4,1), (-3,3)]
        → Top is (-9,4): 4 ≥ 4 - 3 → valid → append 9

i = 5, window = [3,9,5], heap = [(-9,4), (-8,2), (-5,0), (-5,5), (-4,1), (-3,3)]
        → Top is (-9,4): 4 ≥ 5 - 3 → valid → append 9

i = 6, window = [9,5,8], heap = [(-9,4), (-8,2), (-8,6), (-5,0), (-5,5), (-4,1), (-3,3)]
        → Top is (-9,4): 4 ≥ 6 - 3 → valid → append 9

i = 7, window = [5,8,4], heap = [(-9,4), (-8,2), (-8,6), (-5,0), (-5,5), (-4,1), (-4,7), (-3,3)]
        → (-9,4): 4 < 7 - 3 → pop
        → (-8,2): 2 < 7 - 3 → pop
        → (-8,6): 6 ≥ 7 - 3 → valid → append 8

i = 8, window = [8,4,3], heap = [(-8,6), (-5,0), (-5,5), (-4,1), (-4,7), (-3,3), (-3,8)]
        → (-8,6): 6 ≥ 8 - 3 → valid → append 8

i = 9, window = [4,3,2], heap = [(-8,6), (-5,0), (-5,5), (-4,1), (-4,7), (-3,3), (-3,8), (-2,9)]
        → (-8,6): 6 < 9 - 3 → pop
        → (-5,0): 0 < 9 - 3 → pop
        → (-5,5): 5 < 9 - 3 → pop
        → (-4,1): 1 < 9 - 3 → pop
        → (-4,7): 7 ≥ 9 - 3 → valid → append 4

i = 10, window = [3,2,1], heap = [(-4,7), (-3,3), (-3,8), (-2,9), (-1,10)]
        → (-4,7): 7 < 10 - 3 → pop
        → (-3,3): 3 < 10 - 3 → pop
        → (-3,8): 8 ≥ 10 - 3 → valid → append 3

**Important Note:**
The heap structure is not fully sorted; only the first element (top of the heap) is guaranteed to be the max.
We maintain the heap lazily, only purging stale elements when a maximum is actually required.

Time Complexity: O(n log k)
    - Each push and pop is O(log k), and each element is pushed once and popped at most once.
Space Complexity: O(k)
    - The heap stores up to k elements at a time.
"""


from heapq import heappush, heappop

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        maxHeap, res = [], []
        for i in range(len(nums)):
            heappush(maxHeap, (-nums[i], i))
            if i >= k - 1:
                # This indicate this max is not in the current window, we need to pop it
                while not maxHeap[0][1] > i - k:
                    heappop(maxHeap)
                res.append(-maxHeap[0][0])
        return res

