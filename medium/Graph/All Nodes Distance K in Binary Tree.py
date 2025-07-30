"""
Given a binary tree with unique values, a target node, and an integer k,
this function returns all node values that are exactly k distance away
from the target node. Distance is measured in terms of the number of edges
between nodes, and nodes can be reached by going upward to parents or downward to children.

Idea:
- The binary tree is treated as an undirected graph where each node is connected to its
children and to its parent. Since TreeNode does not have parent pointers, we simulate
this by building an undirected graph from the tree using DFS.

Step-by-step breakdown:
1. Convert the tree into an undirected graph:
  - Traverse the tree using DFS.
  - For each node, create bidirectional edges between the node and its children
    by populating an adjacency list (stored in a defaultdict of lists).

2. Perform Breadth-First Search (BFS) starting from the target node:
  - Initialize a queue with the target node's value.
  - Track visited nodes using a set to avoid cycles and re-visiting.
  - At each level of BFS, increment the distance counter.
  - When the BFS reaches distance k, return all node values in the queue.

Why it works:
- BFS guarantees that when distance == k, all nodes in the queue are
exactly k steps away from the target node.
- By treating the tree as an undirected graph, we can explore in all directions.

Time Complexity:
- O(N), where N is the number of nodes in the tree.
- O(N) to build the graph.
- O(N) for BFS traversal (in the worst case, we may visit all nodes).

Space Complexity:
- O(N) for the graph and visited set.
- O(N) for the BFS queue in the worst case.

Returns:
- A list of integer values of nodes that are exactly k distance from the target node.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        graph = defaultdict(list)
        def dfs(node):
            if not node:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        tar = target.val
        dq = deque([tar])
        visited = set()
        distance = 0
        while dq:
            if distance == k:
                return list(dq)
            for i in range(len(dq)):
                curr_node = dq.popleft()
                visited.add(curr_node)
                for next_node in graph[curr_node]:
                    if next_node in visited:
                        continue
                    dq.append(next_node)
            distance += 1

        return []
