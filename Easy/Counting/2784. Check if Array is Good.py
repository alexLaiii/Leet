"""
Idea:
A "good" array must look exactly like:

    [1, 2, 3, ..., n-1, n, n]

where:
- every number from 1 to n-1 appears exactly once
- the maximum number n appears exactly twice
- total length must therefore be n + 1

Approach:
1. Let max_int = max(nums). This represents n.
2. Check if the array length equals max_int + 1.
   If not, it cannot match the required structure.
3. Count occurrences of every number using a hashmap.
4. Verify:
   - every integer from 1 to max_int - 1 appears exactly once
   - max_int appears exactly twice

Key Observation:
The largest value determines what the entire array
should contain. Once n is known, the structure of a
valid "good" array becomes fully fixed.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        max_int = max(nums)
        if len(nums) != max_int + 1:
            return False
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        for i in range(1, max_int):
            if i not in counts or counts[i] >= 2:
                return False
        
        return counts[max_int] == 2
        
