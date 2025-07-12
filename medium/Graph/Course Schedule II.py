"""
Topological Sort via DFS
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
            
            
