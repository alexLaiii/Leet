"""
Dynamic Programming.

Let dp[i] represent the number of set bits (1s) in the binary
representation of integer i.

For any integer i:
- i // 2 removes the least significant bit.
- i % 2 is 1 if the least significant bit is set; otherwise, it is 0.

Therefore:
    dp[i] = dp[i // 2] + (i % 2)

Since dp[i // 2] has already been computed for all i > 0, we can
build the answer iteratively from 1 to n.

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        curr = 1
        while curr <= n:
            res.append(res[curr // 2] + (curr % 2))
            curr += 1
        return res
            
