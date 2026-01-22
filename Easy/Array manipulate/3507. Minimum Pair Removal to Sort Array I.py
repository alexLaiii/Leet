"""
Repeatedly merge the adjacent pair with the smallest sum until the array becomes nondecreasing.

Operation:
- Find the adjacent pair (nums[i], nums[i+1]) with minimum sum.
- Replace nums[i] with that sum and remove nums[i+1] (this is a "merge").
- Count how many merges are performed until nums is sorted (nondecreasing).

Approach:
- Loop while the array is not sorted.
- In each pass, scan once to:
    1) detect whether the array is already nondecreasing, and
    2) locate the index of the minimum-sum adjacent pair.
- If not sorted, perform the merge at that index and continue.

Returns:
- The number of merges required to make nums nondecreasing.

Notes:
- This method mutates the input list `nums` in-place.
- Time complexity: O(k * n) scans plus O(k * n) total shifting from pop,
  where k is the number of merges (k <= n-1). Worst case O(n^2).
- Space complexity: O(1) extra space (in-place), ignoring Python list resizing.
"""

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0
        isSort = False
        while not isSort:
            minSum, idx = float("inf"), 0
            isSort = True
            for i in range(len(nums) - 1):     
                if minSum > nums[i] + nums[i + 1]:
                    minSum = nums[i] + nums[i + 1]
                    idx = i
                if nums[i + 1] < nums[i]:
                    isSort = False
            if not isSort:
                nums[idx] = minSum
                nums.pop(idx + 1)
                res += 1
                
            
        return res
