"""
Return the total sum of divisors for all numbers in `nums` that have exactly 4 distinct positive divisors.

Approach
--------
For each n, enumerate divisors in pairs by scanning `divider` from 1 up to sqrt(n).
Whenever `divider` divides n, we add both `divider` and its paired divisor `n // divider` into a set.
We stop early once the set grows to 5+ elements, because then n cannot have exactly 4 divisors.

Key details
-----------
- Using a set avoids double-counting when `divider == n // divider` (i.e., n is a perfect square).
- The loop condition `divider <= sqrt(n)` ensures we find all divisor pairs.
- Early stopping (`len(divisors) < 5`) improves average runtime.

Correctness
-----------
- If `len(divisors) == 4`, then n has exactly four distinct divisors, so we add their sum to `res`.
- Otherwise, n is ignored.

Complexity
----------
Let m = len(nums). For each n, we scan up to floor(sqrt(n)) divisors in the worst case.
Time:  O(m * sqrt(max(nums))) worst-case, often less due to early stopping.
Space: O(1) extra per n (the set holds at most 5 divisors before we break).

Notes / Potential improvement
-----------------------------
Comparing `divider <= math.sqrt(n)` recomputes sqrt each loop and uses floats.
A safer/faster pattern is `divider * divider <= n` (integer arithmetic) or precompute `limit = int(sqrt(n))`.
"""

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            divisors = set()
            divider = 1
         
            while len(divisors) < 5 and divider <= math.sqrt(n):
                if n % divider == 0:
                    divisors.add(divider)
                    divisors.add(n // divider)
                divider += 1

            if len(divisors) == 4:
                res += sum(divisors)
        return res
                    
            
        
