  """
  *** Hint: Heap queue structure ***
  *** Hint2: 23. Merge k Sorted Lists ***

  Core idea:
    Maintain one pointer per list and a min-heap of those k current values.
    The heap top gives the current minimum; a running variable tracks the
    current maximum across the k picks. This forms a valid covering window
    [min, max] at each step.

  Why it works:
    To possibly shrink the window, you must advance the list contributing
    the current minimum (anything else keeps the same min and can’t help).
    Replacing that min with its next element “slides” the window forward in
    merged order; once a list is exhausted, no full cover remains, and the
    best window seen is optimal.

  Complexity: O(N log k) time, O(k) space.
  """


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minHeap = []
        currMax = float("-inf")
        res = []
        k = len(nums)
        for i in range(k):
            heapq.heappush(minHeap, (nums[i][0], i, 0))
            currMax = max(currMax, nums[i][0])
        
        while len(minHeap) == k:
            mins, arr_num, arr_idx = heapq.heappop(minHeap)
            if not res or res[1] - res[0] > currMax - mins:
                res = [mins, currMax]
            if arr_idx + 1 >= len(nums[arr_num]):
                continue
            currMax = max(currMax, nums[arr_num][arr_idx + 1])
            heapq.heappush(minHeap, (nums[arr_num][arr_idx + 1], arr_num, arr_idx + 1))
        
        return res
            
            
            
            
            
