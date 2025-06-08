"""
Solution 1:

Idea:
Convert the input adjacency matrix into an adjacency list, as adjacency lists are often easier and more intuitive for graph traversal.
We then use a DFS approach to count the number of connected components (provinces).

We loop through all `n` cities. If we find a city that hasn't been visited yet, that means we've discovered a new province, so we increment the province count.
We then perform a DFS from that city to visit all cities reachable from it, and marking them as visited alongside.

This ensures that we only count each province once — even if many cities are interconnected, they will all be marked visited during the first DFS.
Therefore, when the loop reach a later city, it will no perform dfs and again since it is marked as visited, and perserved the correct province count.

At the end, we return the number of provinces.

Time Complexity:
- O(n² + V + E)
  - O(n²) to convert the adjacency matrix into an adjacency list
  - O(V + E) for the DFS traversal

Space Complexity:
- O(V + E) for storing the adjacency list
- O(V) for the visited set
- O(V) auxiliary stack space for DFS (worst case)
"""


class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        graph = {}
        for i in range(n):
            graph[i] = []
            for j in range(n):
                if isConnected[i][j] == 1 and j != i:
                    graph[i].append(j)
        
        
        visited = set()
        def dfs(city):
            if city in visited:
                return
            visited.add(city)
            for cit in graph[city]:
                dfs(cit)        
        count = 0    
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
"""
Solution 2
Idea:
We use the matrix as a graph for traversal, so we don't need extra space for creating an adjacency list.
The idea is basically the same as above.

Implementation:
We also have a visited set to mark all the visited cities, and we loop through city 0 to city n in the outer loop.
Whenever we reach a city that is not visited, we perform DFS on that city and increment the province count.

How DFS works here:
(In the isConnected matrix, each isConnected[i] stores all the other cities that "city i" is connected to.
If they are connected, isConnected[i][j] = 1, indicating that city i and city j are connected.)
Therefore, we can use this fact to perform our DFS.
Whenever we visit a city, we mark it as visited.
Then we loop through isConnected[city], since this row has all the other cities connected to this city.
Perform recursive DFS on all these connected cities until all cities and their indirectly connected cities are visited.
When DFS ends, all the cities directly or indirectly reachable from the caller city will be marked as visited.

Therefore, when the outer loop later reaches any of those cities, it will not increment the province count nor perform DFS again,
because that city is already visited by the earlier DFS.
Return the count at the end.

Time Complexity:
- O(n²)
  We have to go through each cell no matter what, and there are total n² cells in the matrix.

Space Complexity:
- O(V) for the visited set
"""


class Solution(object):
    def findCircleNum(self, isConnected):
        count, visited = 0, set()
        def dfs(city):
            if city in visited:
                return
            visited.add(city)
            for i in range(len(isConnected[city])):
                if isConnected[city][i] == 1 and i not in visited:
                    dfs(i)
        for each_city in range(len(isConnected)):
            if each_city not in visited:
                dfs(each_city)
                count += 1
        return count
 
