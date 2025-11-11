"""
Algorithm: Dutch National Flag algorithms.

Invariants maintained throughout the loop:
  - nums[0 : l]     == 0
  - nums[l : m]     == 1
  - nums[m : r+1]   == unknown (to process)
  - nums[r+1 : end] == 2

Algorithm:
  - If nums[m] == 0: swap into the 0-zone, advance l and m.
  - If nums[m] == 1: it's already in the middle zone, advance m.
  - Else (== 2): swap into the 2-zone by swapping with r, decrement r
                 (do NOT advance m; re-check the swapped-in value).

Time:  O(n)
Space: O(1)
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,m,r = 0,0, len(nums) - 1
        
        while m <= r:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            elif nums[m] == 2:
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1
  
        
