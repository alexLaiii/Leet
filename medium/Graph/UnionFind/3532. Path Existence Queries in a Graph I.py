"""
Since nums is sorted, two adjacent indices belong to the same connected
component if their difference is at most maxDiff. Any valid path between
non-adjacent indices can be formed through a chain of adjacent indices,
so it is sufficient to union only neighboring elements that satisfy the
condition.

Build the connected components using Union Find (Disjoint Set Union) with
path compression and union by size. For each query, the two indices have
a path between them if and only if they share the same representative.

Time: O((n + q) * α(n))
Space: O(n)
"""
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parents = [x for x in range(n)]
        set_count = [1 for x in range(n)]
        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]
        def union(v1,v2):
            p1,p2 = find(v1), find(v2)
            if p1 == p2:
                return
            if set_count[p1] >= set_count[p2]:
                set_count[p1] += set_count[p2]
                parents[p2] = p1
            else:
                set_count[p2] += set_count[p1]
                parents[p1] = p2
        
        
        for r in range(1, n):
            if nums[r] - nums[r-1] <= maxDiff:
                union(r-1,r)
        res = [False] * len(queries)
        for i in range(len(queries)):
            n1,n2 = queries[i]
            if find(n1) == find(n2):
                res[i] = True
        return res
