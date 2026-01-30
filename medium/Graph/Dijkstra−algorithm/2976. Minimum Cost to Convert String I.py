"""
Approach:
- Model character transformations as a directed weighted graph where
  each node is a lowercase letter ('a'–'z') and each edge represents
  a valid conversion with an associated cost.
- Use Dijkstra’s algorithm to compute the minimum cost to convert
  one character into another.
- Precompute the shortest conversion cost for every ordered pair
  of distinct characters (26 × 25 pairs).
- For each index i in source/target:
    - If source[i] == target[i], cost is 0
    - Otherwise, add the precomputed minimum conversion cost
      from source[i] to target[i]
    - If any required conversion is impossible, return -1.

Why this works:
- Conversion costs are non-negative, so Dijkstra guarantees correctness.
- Precomputing all character-to-character costs avoids running
  shortest-path search repeatedly for each position in the string.
- Since the alphabet size is fixed (26), the precomputation cost
  is bounded and small.

Time Complexity:
- Building graph: O(len(original))
- Dijkstra per pair: O(E log V), with V = 26
- Total precomputation: O(26² · E log 26) ≈ constant
- Final pass over strings: O(len(source))
Overall: O(len(source) + constant)

Space Complexity:
- Graph storage: O(E)
- Pair cost table: O(26²)
- Dijkstra heap + visited set: O(26)

Limitations / Possible Improvements:
- Multiple edges between the same (u, v) are stored without pruning;
  storing only the minimum edge weight per pair would reduce work.
- Floyd–Warshall could replace repeated Dijkstra calls and simplify
  the implementation since the graph is very small.
- Using a normal dict instead of defaultdict(int) for `pair` would
  avoid accidental default-zero costs if a key is missing.

Key idea to remember:
- This problem is shortest paths on a *fixed-size* graph; correctness
  matters more than asymptotic scaling.
"""

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj_list = defaultdict(list)
        for i in range(len(original)):
            u,v,c = original[i], changed[i], cost[i]
            adj_list[u].append((v,c))
        
        def shortestChange(ori, dest):
            minHeap = [(0, ori)]
            visited = set()
            while minHeap:
                pathCost, node = heapq.heappop(minHeap)
                if node in visited:
                    continue
                if node == dest:
                    return pathCost
                visited.add(node)
                for neighbour, costs in adj_list[node]:
                    heapq.heappush(minHeap, (pathCost + costs, neighbour))
            return -1
        pair = defaultdict(int)
        for i in range(26):
            for j in range(26):
                if i != j:
                    origin, destin = chr(ord("a") + i), chr(ord("a") + j)
                    pair[(origin, destin)] = shortestChange(origin, destin)
                    
        res = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                costs = pair[(source[i], target[i])]
                if costs < 0:
                    return -1
                res += costs
        return res
                   

        
