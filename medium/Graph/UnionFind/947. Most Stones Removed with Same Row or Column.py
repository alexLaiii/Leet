  """
  LeetCode 947 — Most Stones Removed with Same Row or Column

  Build an undirected graph on stone indices: connect i <-> j iff stones i and j share
  the same row or the same column. In each connected component of size k, we can
  remove k - 1 stones (leave one as the anchor), so the total removals equal
  sum_over_components(k - 1) = n - (#components).

  Implementation details:
    • Construct `adj_list` by pairwise scanning stones (i > j) and adding edges when
      rows or columns match.
    • Depth-first search `dfs(node, fromn, count)` visits a component, counting its
      size. The `visited` set prevents revisits; `fromn` is used to skip the immediate
      parent in the adjacency walk (redundant but harmless given `visited`).
    • For each unvisited index i, run DFS to get the component size; add (size - 1)
      to the answer.

  Correctness sketch:
    Each move removes a stone that still shares a row or column with another stone,
    which is always possible until one per component remains. Therefore the maximum
    number of removals equals the total stones minus the number of connected components.

  Args:
      stones: List of [x, y] integer coordinates for each stone.

  Returns:
      The maximum number of stones that can be removed while keeping the “same row or
      column” constraint satisfied.

  Complexity:
      Time  : O(n^2) to build edges (pairwise row/col checks) + O(n + m) DFS,
              which is O(n^2) in the worst case (dense connections).
      Space : O(n^2) for the adjacency list in the worst case, plus O(n) for `visited`
              and recursion/stack overhead.

  Notes:
      • Isolated stones (no shared row/col) form components of size 1 and contribute 0.
      • For larger inputs, a Union-Find approach on row/column nodes can reduce the
        memory footprint and avoid O(n^2) edge construction.
  """

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for i in range(len(stones)):
            for j in range(0, i):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adj_list[j].append(i)
                    adj_list[i].append(j)
     
        visited = set()
        self.count = 0
        def dfs(node, fromn):
            if node in visited:
                return 0
            visited.add(node)
            size = 1
            for next_node in adj_list[node]:
                if next_node == fromn:
                    continue
                size += dfs(next_node, node)
            return size

        res = 0
        for i in range(len(stones)):
           if i not in visited:
                res += dfs(i, -1) - 1
            
        return res
