"""
Idea:
This is a graph problem using a "Graph Adjacency List" to represent edges for each vertex.
The goal is to use a DFS function to detect any cycle between a course and its prerequisite course.

For example:
numCourses = 2, prerequisites = [[1,0],[0,1]]
This creates a circular loop: 1 <- 0 <- 1, which is not finishable.

(Like the "no first job → no experience → no first job" paradox.)

Implementation:
We must check if we can complete all the courses from 0 to numCourses - 1.

Step 1: Create an adjacency list up to numCourses - 1, where each vertex maps to its prerequisite list.
Example:
numCourses = 6
prerequisites = [[1,0],[1,2],[3,1],[2,3],[2,4],[4,5],[2,5]]
Adjacency List:
{
  0: [],
  1: [0, 2],
  2: [3, 4, 5],
  3: [1],
  4: [5],
  5: []
}

Step 2: Implement a DFS function to check if a course can be completed.

Base case 1:
If a course has no prerequisites (empty list), return True.

Base case 2:
If a course is already in the `visited` set → we’ve found a cycle → return False.

Why?
Imagine checking a course (A) → it depends on course (B) → which depends on (A) again → endless loop → not completable.

Recursive step:
- Add current course to `visited`
- For each prerequisite, run DFS
  - If any call returns False → break and return False
- After all are valid:
  - Remove current course from `visited` (important for correctness)
  - Set its prerequisite list to [] → this memoizes that it's completable
  - Return True

❗ Why `visited.remove(course)` is important:
Counterexample:
{
  0: [],
  1: [],
  2: [3, 4],
  3: [1],
  4: [1],
  5: []
}
When checking course 2:
- Go to course 3 → depends on 1 → valid → return True
- Then course 4 → also depends on 1
  - But 1 is still in `visited` if we didn’t remove → False detection → bug

So we must `visited.remove(course)` after we’re done checking it.

Why do we set the course’s prereq list to empty?
This marks it as completable — avoids re-checking the same path in future DFS calls.

Outside DFS:
We loop over all courses from 0 to numCourses-1 because the graph might be disconnected.
Example:
{
  1:[2],
  2:[],
  3:[4],
  4:[]
}
Here 1→2 and 3→4 are disjoint; only checking one path is not enough.

Time Complexity:
O(V + E)
- V = numCourses
- E = total prerequisites
DFS is only run once per course due to memorization (setting prereq to [])

Space Complexity:
O(V + E) for the adjacency list
O(V) for recursion stack and visited set
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        dir_graph = {i:[] for i in range(numCourses)}
        for course, preq in prerequisites:
            dir_graph[course].append(preq)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if dir_graph[course] == []:
                return True
            visited.add(course)
            for preq in dir_graph[course]:
                res = dfs(preq)
                if not res: break
            visited.remove(course)
            dir_graph[course] = []
            return res
        for cours in range(numCourses):
            if not dfs(cours):
                return False   
        return True
            

        
