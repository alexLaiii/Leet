  """
  Leetcode 128: Longest Consecutive Sequence

  Idea:
  Use Union-Find (Disjoint Set Union) with path compression and union by size
  to dynamically group consecutive numbers into connected components.
  The size of each component corresponds to the length of a consecutive sequence.

  Key Concepts:
  - Each unique number is treated as a node in the Union-Find structure.
  - If `n + 1` exists in the dataset, then `n` and `n + 1` belong to the same consecutive sequence.
  - By unioning `n` and `n + 1` for all such pairs, we form disjoint sets representing sequences.
  - The `ranks` dictionary tracks the size of each set (sequence length), allowing us to find the maximum.

  Why this works:
  - We don't need to sort the array (which is O(n log n)); instead, we use Union-Find operations which run in amortized O(α(n)).
  - Duplicates are automatically handled via overwriting in the initialization step.
  - The final answer is the largest size among all connected components.

  Time Complexity:
  - O(n α(n)) ≈ O(n), where α is the inverse Ackermann function (nearly constant in practice)

  Space Complexity:
  - O(n) for the Union-Find maps (parents and ranks)

  Parameters:
  nums (List[int]): List of integers that may include duplicates and be unsorted.

  Returns:
  int: Length of the longest consecutive sequence.
  """


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        parents = {}
        ranks = {}
        for n in nums:
            parents[n] = n
            ranks[n] = 1

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return
            if ranks[p1] > ranks[p2]:
                ranks[p1] += ranks[p2]
                parents[p2] = p1
            else:
                ranks[p2] += ranks[p1]
                parents[p1] = p2
        
        max_count = 1
        for n in nums:
            if n + 1 in parents:
                union(n, n + 1)    
                max_count = max(max_count, ranks[find(n)])
        
        return max_count
