"""
Determine if people can be split into two groups such that no "dislike" pair ends up
in the same group. This implements a classic **bipartite graph** check via **BFS 2-coloring**.

Core idea:
- Model people as nodes and each dislike pair as an **undirected** edge (mutual constraint).
- Try to 2-color each connected component using colors {0, 1} (your `group` array).
  For every edge (u, v), we enforce group[u] != group[v].
- Use BFS: pick an uncolored node, color it 0, then traverse neighbors; each uncolored
  neighbor gets the opposite color (1 - current). If you ever see a neighbor already
  colored with the same color, the graph is not bipartite → return False.
  
**** Important ****
Why the graph must be **undirected** (important insight):
- A dislike pair is a symmetric constraint: if a dislikes b, b also cannot be grouped with a.
  Therefore each pair must be represented as an **undirected** edge.
- If you build a **directed** graph instead, traversal may fail to visit all nodes that are
  logically in the same connected component (because you can’t necessarily travel “back”).
  This can lead to inconsistent coloring depending on start order. For example:
      n = 4, dislikes = [[1,2],[2,4],[3,4]]
    Undirected: {1–2, 2–4, 3–4} is bipartite with coloring 1=0, 2=1, 4=0, 3=1.
    Directed-only: 1→2→4 and 3→4. Starting BFS at 1 colors 1=0,2=1,4=0; later starting at
    3 sets 3=0 and immediately conflicts with 4=0 via 3→4, falsely concluding not bipartite.
  Conclusion: directed modeling is brittle and order-dependent; undirected modeling robustly
  enforces the mutual “must differ” constraints.
**************************

Implementation notes (about this code):
- `group[i]` in {-1, 0, 1} tracks color/visit state (-1 = uncolored).
- BFS runs on every uncolored node i to cover **disconnected components**.
- The inner check:
    - If neighbor is uncolored → color it with 1 - group[curr].
    - If neighbor already has the same color as curr → conflict → return False.
- The outer loop ensures isolated nodes and separate components are handled.

Correctness and complexity:
- This is a standard bipartite check; it returns True iff every edge connects differently
  colored endpoints.
- Time: O(n + m), where m = len(dislikes) (each node/edge processed O(1) times).
- Space: O(n + m) for adjacency lists, queue, and color array.

Pitfalls to remember:
- Always model mutual constraints as **undirected** edges.
- Always iterate over all nodes to handle **disconnected** graphs.
"""


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        # 0 is group 0, 1 is group 1, -1 is no group assigned yet
        group = [-1] * (n + 1)
        graph = defaultdict(list)
        for n1,n2 in dislikes:
            graph[n1].append(n2)
            graph[n2].append(n1)
         

        def bfs(node):
            dq = deque([node])
            group[node] = 0
            while dq:
                for i in range(len(dq)):
                    curr_node = dq.popleft()
                    for next_node in graph[curr_node]:
                        if group[curr_node] == group[next_node]:
                            return False
                        if group[next_node] == -1:
                            group[next_node] = 1 - group[curr_node]
                            dq.append(next_node)
            return True
        for i in range(1, n + 1):
            # This seperate graph is checked already
            if group[i] != -1:
                continue
            if not bfs(i):
                return False
        return True
\
