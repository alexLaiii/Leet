"""
Side Note:
Solving this problem with the hash set approach is very easy.
But the difficulties jump to MEDIUM if solve with O(1) space complexity

As the following "+n" marking method:
O(n) time complexity
O(1) extra space
"""
"""
Return the two duplicated values in an array of length n whose elements lie in [0, n-1],
using O(1) extra space and O(n) time by in-place "+n" marking.

idea:
    Treat the array itself as a frequency bucket. For each value v, look at index v.
    On the first visit to v, add n to nums[v] to mark it. On a later visit to v, nums[v]
    will be >= n, which signals that v has already been seen once → v is a duplicate.
    The `% n` guards against the fact that entries grow by multiples of n as we mark.

algorithm:
    - Let n = len(nums).
    - For each i in 0..n-1:
        idx = abs(nums[i]) % n
        If nums[idx] >= n: record idx as a duplicate
        Else: nums[idx] += n
    - Return the list of recorded duplicates.

correctness sketch:
    Initially, for every index j, nums[j] < n. After we process value v for the first time,
    nums[v] ∈ [n, 2n-1]. When we encounter v again, nums[v] ≥ n holds, so we detect the duplicate.
    Using `% n` recovers the original value regardless of how many n’s were added.

constraints/assumptions:
    - Values must be within [0, n-1].
    - The array may contain exactly two duplicates (problem guarantee); the function returns
      all duplicates it detects in encounter order.
    - The array is modified in-place (marks remain). To restore, do: for j in range(n): nums[j] %= n.

complexity:
    Time  : O(n) single pass
    Space : O(1) auxiliary (ignoring the output list)

edge cases:
    - Duplicate value 0 is handled because nums[0] < n initially; after first hit it becomes ≥ n.
    - Works even if the duplicates are adjacent or far apart.

"""


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        repeat = []
        for i in range(n):
            idx = abs(nums[i]) % n
            if nums[idx] >= n:
                repeat.append(idx)
            else:
                nums[idx] += n
        
        return repeat
                
