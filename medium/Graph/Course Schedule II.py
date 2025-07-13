"""
Use same idea from Course Schedule but track the path of course finishing.
Topological Sort via DFS.

Idea:
We apply topological sorting to determine a valid order in which to take courses.

- A course with no prerequisites can be taken immediately.
- For each course, we perform a DFS to recursively visit all of its prerequisites.
- We mark nodes as visited during DFS to detect cycles (i.e., circular dependencies).
- After visiting all prerequisites of a course, we add the course to the result list.
  This ensures that prerequisites are always added before the course that depends on them.
- The graph is built such that each course maps to a list of its prerequisites (i.e., course → prereqs).

Since we're adding courses post-recursively, the result is already in the correct topological order (no need to reverse).

Time Complexity: O(V+E)
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for course, preq in prerequisites:
            graph[course].append(preq)
        
        res = []
        visited = set()
        taken = set()
        def dfs(course):
            # Cyclic graph
            if course in visited:
                return False
            # This course has been checked and can be finished, return True
            if course in taken:
                return True
            visited.add(course)
            for preq in graph[course]:
                if not dfs(preq):
                    return False
            res.append(course)
            taken.add(course)
            visited.remove(course)
            return True
            
            

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
            
            
