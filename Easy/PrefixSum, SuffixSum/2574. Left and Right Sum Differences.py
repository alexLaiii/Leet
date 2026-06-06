"""
Return an array where each index contains the absolute difference between
the sum of all elements to its left and the sum of all elements to its right.

The idea is to maintain two running sums:
- leftSum stores the sum of elements before the current index.
- rightSum stores the sum of elements after the current index.

For index 0, leftSum is 0 and rightSum is the total sum excluding nums[0].
Then, as we move from left to right, we update leftSum by adding the
previous element and update rightSum by removing the current element.

Args:
    nums: A list of integers.

Returns:
    A list where ans[i] = abs(leftSum[i] - rightSum[i]).

Time Complexity:
    O(n), where n is the length of nums.

Space Complexity:
    O(1) extra space, not counting the output array.
"""
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rightSum = sum(nums) - nums[0]
        leftSum = 0
        ans = [abs(leftSum - rightSum)]
        for i in range(1, len(nums)):
            leftSum += nums[i - 1]
            rightSum -= nums[i]
            ans.append(abs(leftSum - rightSum))
        return ans
