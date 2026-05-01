"""
Find the length of the longest subarray where:
- All elements are UNIQUE within the subarray
- The number of EVEN and ODD elements is equal

Key Idea:
We brute-force all possible subarrays using a starting index i,
and expand the window to the right.

While expanding:
- Use a set `windows` to ensure all elements in the current subarray are unique
- Only count parity (odd/even) the FIRST time we see an element
  (duplicates are ignored completely)
- Maintain:
    odd_count  → number of distinct odd numbers
    even_count → number of distinct even numbers

Important Observation:
A subarray is "balanced" when:
    odd_count == even_count

At each step:
- If the current element is new (not in the set), update counts
- Check if the subarray is balanced
- Update the maximum length accordingly

Complexity:
- Time: O(n^2), since we check all subarrays
- Space: O(n), for the set storing unique elements

Notes:
- Duplicates do NOT affect the counts, since only distinct elements matter
- However, duplicates still contribute to the length of the subarray
"""

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            odd_count = even_count = 0
            windows = set()
            for j in range(i, len(nums)):
                if nums[j] not in windows:
                    windows.add(nums[j])
                    if nums[j] % 2 != 0:
                        odd_count += 1
                    else:
                        even_count += 1
                if odd_count == even_count:
                    res = max(res, (j - i) + 1)
            
        return res
