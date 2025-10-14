  """
  Determine whether there exist two consecutive length-k subarrays in `nums`
  that are each strictly increasing.

  Definition
  ----------
  Two subarrays are "consecutive" if the second starts immediately after the first
  ends (i.e., windows [i-k+1, i] and [i+1, i+k] for some i). A subarray is
  "strictly increasing" if nums[j] < nums[j+1] for all indices inside the window.

  Approach
  --------
  Single pass with a running length of the current strictly increasing run:
    1) If the current run length ever reaches 2k, it already contains two adjacent
       strictly increasing windows of length k → return True.
    2) When a run breaks, if its length ≥ k we record the end index. While building
       the next run, as soon as it reaches length ≥ k we check whether the previously
       recorded qualifying run ends exactly at the position just before this run starts
       (i.e., back-to-back). If yes → return True.

  Edge Case
  ---------
  If k == 1, any two adjacent elements form consecutive length-1 windows, so return True.

  Complexity
  ----------
  Time: O(n)
  Space: O(1) auxiliary (the list of candidate ends remains tiny; it only keeps the
         most recent qualifying run end).

  Parameters
  ----------
  nums : List[int]
      Input array.
  k : int
      Target window length.

  Returns
  -------
  bool
      True if two consecutive strictly increasing length-k subarrays exist; else False.
  """

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True

        length = 1
        count = 0
        idx = []
        for i in range(len(nums)):
            if i > 0 and nums[i] > nums[i-1]:
                length += 1
                if length >= k * 2:
                    return True
            else:
                if length >= k:
                    idx.append(i - 1)
                length = 1
            if idx and length >= k:
                if idx[-1] == i - length:
                    return True

        return False
                    
                    
            
