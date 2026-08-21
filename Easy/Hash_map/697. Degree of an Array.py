"""
  Find the length of the shortest subarray with the same degree as nums.

  Two-pass sliding window:
  1. First pass computes `deg`, the maximum frequency of any element
     in the full array (the array's "degree").
  2. Second pass slides a window [l, r] over nums, tracking frequency
     of elements within the window only. Whenever the current right
     element's in-window frequency hits `deg`, the window is a valid
     candidate (it can't exceed `deg`, since deg is the global max),
     so its length is recorded and the window is shrunk from the left
     until that frequency drops.

  Note: shrinking isn't tied to the specific element needing `deg`
  occurrences preserved -- it removes from the left one at a time
  until *any* removal drops freq[nums[r]] below deg. This can evict
  an earlier occurrence of a different value as a side effect before
  that value ever reaches deg on its own, causing its true minimal
  window to go unrecorded. This never produces a wrong answer: it
  can be shown that whenever a value's window is missed this way,
  the window that caused the eviction is provably smaller and was
  already recorded, so the minimum found is still guaranteed correct.

  Time:  O(n) -- two linear passes, each pointer moves forward only.
  Space: O(k) -- k = number of distinct values in nums.

  Args:
      nums: List of non-negative integers.

  Returns:
      Length of the shortest subarray of nums having the same degree.
  """

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        deg = max(freq[key] for key in freq) 
        freq = defaultdict(int)
        l = 0
        res = len(nums)
        for r in range(len(nums)):
            freq[nums[r]] += 1

            while freq[nums[r]] == deg:
                res = min(res, r - l + 1)
                freq[nums[l]] -= 1
                l += 1
                
            
        return res
        
