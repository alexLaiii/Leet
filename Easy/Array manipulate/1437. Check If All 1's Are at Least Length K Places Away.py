  """
  Check if all 1's in a binary array are at least k places apart.

  A pair of 1's at indices i and j (with j > i) is valid only if
  there are at least k zeros between them. Equivalently:
      j - i - 1 >= k  <=>  j - i > k

  This method scans the array once, keeping track of the index of
  the most recent 1. When a new 1 is found, we check the distance
  to the previous one:
      - If last_one_index != -1 and (i - last_one_index) <= k,
        then the two 1's are too close, so we return False.

  If no violations are found after scanning the entire list,
  all 1's satisfy the spacing requirement and we return True.

  Args:
      nums: List[int] - binary array (only 0s and 1s).
      k: int - required minimum number of zeros between any two 1's.

  Returns:
      bool: True if every pair of 1's is at least k places apart,
            False otherwise.

  Time Complexity:
      O(n), where n is the length of nums. We traverse the list once.

  Space Complexity:
      O(1), using only a constant amount of extra space
      (to store the index of the last seen 1).
  """

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lastone = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if lastone != -1 and i - k <= lastone:
                    return False
                lastone = i
        return True
            
        
