  """
  Goal:
    At each step, decide whether the left or right subarray would be ODD in length
    after accounting for the duplicate next to mid. Always shrink to the ODD subarray,
    since the single element must reside in an odd-length segment.
  """


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] == nums[mid - 1]:
                """
                Here the duplicate sits on the LEFT side: pair = (mid-1, mid).
                Consider the left subarray [l..mid], whose length is (mid - l + 1).

                - If (mid - l + 1) is ODD:
                    The single must be in the left subarray (odd length), so keep left:
                    r = mid
                - If it is EVEN:
                    Then the right subarray must be ODD (total is odd), so keep right:
                    l = mid + 1
                """
                if (mid - l + 1) % 2 != 0:
                    r = mid
                else:
                    l = mid + 1

            elif nums[mid] == nums[mid + 1]:
                """
                Here the duplicate sits on the RIGHT side: pair = (mid, mid+1).
                Consider the right subarray [mid..r], whose length is (r - mid + 1).

                - If (r - mid + 1) is ODD:
                    The single must be in the right subarray (odd length), so keep right:
                    l = mid
                - If it is EVEN:
                    Then the left subarray must be ODD, so keep left:
                    r = mid - 1
                """
                if (r - mid + 1) % 2 != 0:
                    l = mid 
                else:
                    r = mid - 1
            else:
                """
                Neither neighbor equals nums[mid], so nums[mid] itself is the single.
                """
                return nums[mid]

        """
        If we never returned inside the loop, the window shrank to size 1 (l == r),
        so nums[l] == nums[r] is the single.
        Example:
          nums = [10, 11, 11]
          -> nums[mid] matches the right neighbor, we move r = mid - 1
          -> while l < r is False now, loop ends with l == r
          -> then nums[r] (or nums[l]) is the answer.
        """
        return nums[l]
