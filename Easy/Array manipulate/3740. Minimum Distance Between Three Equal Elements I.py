"""
Return the minimum distance among all triples of equal elements.

For any value that appears at least three times, suppose its indices are
a < b < c. The distance for that triple is computed as

    |a - b| + |b - c| + |c - a|

Since the indices are in increasing order, this simplifies to

    (b - a) + (c - b) + (c - a) = 2 * (c - a)

The algorithm stores the indices of each number in a hash table. Whenever
a number has appeared at least three times, it checks the most recent
three occurrences and updates the minimum distance found so far.

Args:
    nums: A list of integers.

Returns:
    The minimum distance between any three equal elements if such a triple
    exists; otherwise, -1.

Time Complexity:
    O(n), where n is the length of nums.

Space Complexity:
    O(n), in the worst case, for storing indices in the hash table.
"""

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        hash_table = defaultdict(list)
        minDistance = float("inf")
        for i in range(len(nums)):
            val = nums[i]
            hash_table[val].append(i)
            if len(hash_table[val]) >= 3:
                minDistance = min(minDistance, abs(hash_table[val][-3] - hash_table[val][-2]) + abs(hash_table[val][-2] - hash_table[val][-1]) + abs(hash_table[val][-1] - hash_table[val][-3]))
                
        
        return minDistance if minDistance != float("inf") else -1
        
