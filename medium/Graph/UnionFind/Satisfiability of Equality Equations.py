"""
LeetCode 990 – Satisfiability of Equality Equations

Idea:
We use a Union-Find (Disjoint Set) approach to solve this problem.

There are only two types of equations:
- "==" → represents equality (i.e., a connection)
- "!=" → represents inequality (i.e., not connected)

Concept:
- "a == b" means a and b are in the same group — we connect them.
- "a != b" means a and b must not be in the same group — we check for contradictions later.

Implementation Steps:
1. Graph Building Phase:
   - We only process "==" equations here.
   - For each "a == b", we union them (i.e., put them in the same set).
   - This builds groups of variables that are declared equal.
   - We use the ord(char) - ord("a") trick to map lowercase letters to indices 0–25.

2. Contradiction Check Phase:
   - We then loop through all "!=" equations.
   - If a != b but their representatives (parents) are the same → ❗ contradiction!
   - In that case, return False.

3. If no contradictions are found, return True at the end.

Why Not Check and Build in One Loop?

Consider:
["a == b", "a != c", "c == a"]

- If we process "a != c" before "c == a" is added, we won’t detect the contradiction.
- This is because a and c are not yet connected when we check their inequality.
- So we must first build all "==" connections, then validate "!=" equations after.

Technically, you could track "!=" relations separately and re-check them after "==" unions,
but that's messy and error-prone — it's cleaner to separate the build and check phases.

Why Union-Find?
- It efficiently groups variables that are equal.
- It lets us quickly check if two variables are in the same group.
- It’s faster and simpler than graph traversal for this case.

Time and Space Complexity:
- Time:
    - Each union/find operation is nearly O(1) with path compression
    - Total: O(N) where N = number of equations

- Space:
    - O(1) for parent/rank arrays, always size 26 so constant space (since only lowercase letters)

Summary:
Build "==" relationships using Union-Find → then check "!=" for contradictions.
Always separate building and validation to avoid missing early contradictions.
"""



class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = [i for i in range(26)]
        rank = [1 for i in range(26)]

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return
            if rank[p1] >= rank[p2]:
                rank[p1] += rank[p2]
                parents[p2] = p1
            else:
                rank[p2] += rank[p1]
                parents[p1] = p2

        for eq in equations:
            n1,n2 = ord(eq[0]) - ord("a"), ord(eq[3]) - ord("a")
            if eq[1:3] == "==":
                union(n1, n2)
        
        for eq in equations:
            n1,n2 = ord(eq[0]) - ord("a"), ord(eq[3]) - ord("a")
            if eq[1:3] == "!=" and (find(n1) == find(n2)):
                return False
        return True
            
