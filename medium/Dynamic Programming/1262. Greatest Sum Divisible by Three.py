"""
Solution 1

DP on remainders (mod 3).

dp[r] = maximum sum achievable so far with total % 3 == r.
We start with dp = [0, 0, 0] (sum 0 has remainder 0, and the other
entries will grow as we add numbers).

For each number n, we take a snapshot of the current dp (prev) and try
to add n on top of every existing remainder bucket prev[i]. This forms
a candidate sum prev[i] + n, which has new remainder:
    new_r = (prev[i] + n) % 3
We update dp[new_r] with the maximum of its current value and this
candidate. The "do not pick n" case is implicitly handled because dp
already contains the old best values, and max(...) will keep them if
adding n does not help.

At the end, dp[0] is the largest sum we can get that is divisible by 3.

Time complexity: O(n * 3) = O(n)
Space complexity: O(1)  (dp has constant size 3)
"""

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0,0,0]
        
        for n in nums:
            prev = dp.copy()
            for i in range(3):
                remainder = (n + prev[i]) % 3
                dp[remainder] = max(dp[remainder], n + prev[i])
        
        return dp[0]

"""
Solution 2:

Greedy: start from the total sum and remove the smallest possible value(s)
so that the remaining sum becomes divisible by 3.

1. Compute total sum and its remainder r = sum % 3.
 - If r == 0, we can take all numbers.
2. Otherwise, collect the two smallest numbers for each non-zero remainder:
 - dp[0] stores the two smallest numbers with remainder 1 (mod 3).
 - dp[1] stores the two smallest numbers with remainder 2 (mod 3).
 We maintain these with simple "two-min" updates while scanning nums.
3. If r == 1, we can fix the sum in two ways:
 - Remove one remainder-1 number (smallest in dp[0][0]), or
 - Remove two remainder-2 numbers (dp[1][0] + dp[1][1]).
 Pick the smaller removal (if it exists).
4. If r == 2, do the symmetric choices:
 - Remove one remainder-2 number, or
 - Remove two remainder-1 numbers.
5. Sentinel value 0 in dp means "no candidate stored yet", so the
 final if-block handles cases where some options are impossible
 (e.g., not enough numbers of a certain remainder).

Time complexity: O(n), since we scan nums once.
Space complexity: O(1), only a small fixed dp array is used.
"""
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        sums = sum(nums)
        sumRemainder = sums % 3
        if sumRemainder == 0:
            return sums
        dp = [[0, 0] for i in range(2)]
        for n in nums:
            remainder = n % 3
            if remainder != 0:
                if dp[remainder - 1][0] == 0:
                    dp[remainder - 1][0] = n
                elif n <= dp[remainder - 1][0]:
                    dp[remainder - 1][1] = dp[remainder - 1][0]
                    dp[remainder - 1][0] = n
                elif dp[remainder - 1][1] == 0:
                    dp[remainder - 1][1] = n
                elif n <= dp[remainder - 1][1]:
                    dp[remainder - 1][1] = n
       
        if sumRemainder == 1:
            if dp[0][0] == 0 and dp[1][1] == 0:
                return 0
            if dp[1][1] == 0:
                return sums - dp[0][0]
            if dp[0][0] == 0:
                return sums - (dp[1][0] + dp[1][1])
            return sums - min(dp[0][0], dp[1][0] + dp[1][1])
        else:
            if dp[1][0] == 0 and dp[0][1] == 0:
                return 0
            if dp[0][1] == 0:
                return sums - dp[1][0]
            if dp[1][0] == 0:
                return sums - (dp[0][0] + dp[0][1])
          
            return sums - min(dp[1][0], dp[0][0] + dp[0][1])
