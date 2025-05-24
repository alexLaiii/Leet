"""
Celebrate the first Medium I solved in 30 mins without a hint!

Idea:
Keep track of the "maximum jump" you can make at each index. 
If at any point, your maximum jump can reach or pass the end (i.e., 
max_jump >= len(nums) - current_index - 1), you can exit early.

Alternatively, you can iterate to the second-last index and check 
if the max jump there is at least 1 (i.e., max_jump >= 1).

Implementation:
- dp[0] represents the max jump from the previous index.
- dp[1] represents the max jump at the current index.
- Initialize dp[0] = nums[0]
- Initialize dp[1] = max(dp[0] - 1, nums[1])
  (because it takes 1 jump to get here from dp[0])

In the loop:
- Shift dp[1] into dp[0]
- Recompute dp[1] = max(nums[i], dp[1] - 1)

Edge case handling:
- If len(nums) == 1: No jump needed → return True
- If len(nums) > 1 and nums[0] == 0: Can't move → return False
- If len(nums) == 2: Only need one jump from index 0 → return nums[0] >= 1
- If len(nums) == 3: You can win if either:
    - nums[0] >= 2 (jump straight to the end), or
    - nums[1] >= 1 (jump from index 1 to the end)

Note: Without proper edge checks, initializing 
dp[1] = max(nums[0] - 1, nums[1]) can be invalid if nums[0] == 0, 
because nums[1] may be unreachable.

Time Complexity: O(n), where n = len(nums)
Space Complexity: O(1)
"""

class Solution(object):
    def canJump(self, nums):
        # Idea: find the best you can move at each index
        # dp[0] represent maxmimum jump on previous index, dp[1] represent maximum jump on current index
        # You dont need to jump
        if len(nums) == 1:
            return True
        # You can't jump anywhere
        if nums[0] == 0:
            return False
        # You only need length 1 jump, since jump != 0 is confirmed, you always reach
        if len(nums) == 2:
            return nums[0] >= 1
        # You need at least length 2 jump in first index, or 1 jump in second index
        if len(nums) == 3:
            return nums[0] >= 2 or nums[1] >= 1
        
        # The best of each position
        dp = [nums[0], max(nums[0] - 1, nums[1])]

        for i in range(2, len(nums) - 1):
            if dp[1] == 0:
                return False
            dp[0],dp[1] = dp[1], max(nums[i], dp[1] - 1)
            # early exit if the current jump can get to the last index
            if dp[1] >= len(nums) - i - 1:
                return True
        return False

        
