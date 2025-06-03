"""
Idea:
Use a DP array to track the length of the longest increasing subsequence ending at each index.
Also use a global variable `longest` to keep track of the maximum subsequence length encountered so far.

Implementation:
- Initialize a DP array of the same length as the input `nums`, filled with 1s.
  - This is because the minimum LIS ending at any index is at least 1 (the element itself).
- Loop through each index `i` of `nums`.
  - For each `i`, loop through all previous indices `j < i`.
  - If `nums[i] > nums[j]`, it means `nums[i]` can extend the increasing subsequence ending at `j`.
    - In that case, update `dp[i] = max(dp[i], dp[j] + 1)`
  - After the inner loop, update `longest = max(longest, dp[i])`

At the end, `longest` will contain the length of the longest increasing subsequence.

Example walkthrough:
nums = [4, 10, 4, 3, 8, 9]
DP    = [1,  1,  1, 1, 1, 1]

Step-by-step updates:
- i = 0 → 4 → no previous values → dp[0] = 1
- i = 1 → 10 > 4 → dp[1] = dp[0] + 1 = 2 → DP = [1, 2, 1, 1, 1, 1]
- i = 2 → 4 is not > any previous valid increasing → DP = [1, 2, 1, 1, 1, 1]
- i = 3 → 3 is not > any previous valid increasing → DP = [1, 2, 1, 1, 1, 1]
- i = 4 → 8 > 4 (i=0,2,3) → best is dp[3] + 1 = 2 → DP = [1, 2, 1, 1, 2, 1]
- i = 5 → 9 > 8 → dp[5] = dp[4] + 1 = 3 → DP = [1, 2, 1, 1, 2, 3]

Final result: max(dp) = 3 → return 3

Time Complexity:
- O(n²): For each element, you potentially compare to all previous elements.

Space Complexity:
- O(n): One DP array of size equal to the input.
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [1] * len(nums)
        longest = 1
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            longest = max(dp[i], longest)
        return longest
            
            
            
            
            
                

        

   
        
        
