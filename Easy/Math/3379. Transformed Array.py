"""
Constructs a transformed array where each index i maps to the value at
position (i + nums[i]) modulo N.

The transformation treats the array as circular, so positive and negative
shifts wrap around using modulo arithmetic.

Args:
    nums (List[int]): Input integer array representing index shifts.

Returns:
    List[int]: The transformed array after applying all index shifts.

Time Complexity:
    O(N), where N is the length of nums.

Space Complexity:
    O(N) for the result array.
"""
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        N = len(nums)
        for i in range(N):
            idx = (nums[i] + i) % N 
            res.append(nums[idx])

        return res
