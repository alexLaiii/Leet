"""
LeetCode 399 – Evaluate Division

Intuition:
This problem requires both math reasoning and the instinct to recognize that it's a graph problem.

Example:
Given: equations = [["a", "b"], ["b", "c"]], values = [2.0, 3.0]
Queries = [["a", "c"], ["b", "a"]]

We want to compute:
- a / c → Since a / b = 2 and b / c = 3, then:
  a / c = (a / b) * (b / c) = 2 * 3 = 6

Proof:
In (a / b) * (b / c), the denominator of the first term and the numerator of the second cancel out,
leaving us with a / c. So this multiplication is valid and always holds.

Now how about b / a?
If a / b = 2, then:
  a = b * 2
  1 = (b * 2) / a
  1 / 2 = b / a
So:
  b / a = 1 / (a / b)

This reciprocal logic is valid as long as we don't divide by zero — which the problem guarantees.

Why Graph:
- Since now we need to Map the denominator to all the possible numerator in the equations.
To generalize, our task is:
→ Map each variable to all other connected variables (from all equations), keeping track of the multiplication relationship (i.e., the weight).

This leads us naturally to a **graph** representation:
- Each variable is a **node**
- Each equation a / b = v is a **directed edge** from:
  - a → b with weight v
  - b → a with weight 1/v (since the reverse must also be queryable)

Implementation:
We construct a bidirectional weighted graph using an adjacency list.
Example:
equations = [["a","b"], ["b","c"]], values = [2.0, 3.0]

Adjacency list:
{
  'a': [('b', 2.0)],
  'b': [('a', 0.5), ('c', 3.0)],
  'c': [('b', 1/3)]
}

Then, to evaluate each query like "a / c", we perform a **DFS traversal** starting from 'a' and looking for a path to 'c', accumulating the product of weights along the path.

DFS function:
def dfs(n1, n2, ans):
    - n1: current node
    - n2: target node
    - ans: accumulated product along the path

Base case:
    - If n1 == n2, we've found the path → return ans

Recursive case:
    - Mark n1 as visited
    - For each neighbor of n1:
        - If neighbor already visited → skip
        - Recursively call dfs on neighbor with updated product: ans * weight
        - If result is not -1.0 → return it early (target found, If n1 == n2 excecuted)

If no path found to n2, return -1.0

Edge Cases:
- n1 and n2 both exist in the graph but are in **disconnected components** → still return -1.0
- This means the two variables have no relationship via given equations.

Outer Loop logic:
For each query [n1, n2]:
    - If either n1 or n2 is not in the graph → result is -1.0 (The variable is not given in the equation -> guranteens no result)
    - Otherwise, perform DFS and collect the result



Time Complexity:
- Let N = number of equations, Q = number of queries
- Building the graph: O(N)
- Each DFS: worst-case O(N) per query
- Overall: O(N + Q * N)
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.ans = 1
        adj_list = defaultdict(list)
        for i in range(len(equations)):
            n1,n2 = equations[i][0], equations[i][1]
            v = values[i]
            adj_list[n1].append((n2, v))
            adj_list[n2].append((n1, 1.0/v ))

        
        def dfs(n1,n2,ans):
            if n1 == n2:
                return ans
            visited.add(n1)
            for next_n,w in adj_list[n1]:
                if next_n in visited:
                    continue
                res = dfs(next_n, n2, ans * w)
                if res != -1.0:
                    return res
            return -1.0
        res = []
        for n1,n2 in queries:
            if n1 not in adj_list or n2 not in adj_list:
                res.append(-1.0)
                continue
            visited = set()
            res.append(dfs(n1,n2, 1))
            
        return res


###
Same Idea: But cleaner variable names
###
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            n1,n2 = equations[i]
            v = values[i]
            graph[n1].append((n2, v))
            graph[n2].append((n1, 1/v))

        def dfs(node, target, weight, visited):
            if node == target:
                return weight
            if node in visited:
                return -1.0
            visited.add(node)
            for next_node, next_w in graph[node]:
                res = dfs(next_node, target, weight * next_w, visited)
                if res != -1.0:
                    return res
            return -1.0
        
        results = []
        for x,y in queries:
            if x not in graph or y not in graph:
                results.append(-1.0)
                continue
            
            results.append(dfs(x,y, 1, set()))

        return results
            
