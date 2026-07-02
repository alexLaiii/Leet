"""
Use Dijkstra's algorithm to find the minimum health cost needed
to reach the bottom-right cell.

Each cell has a cost of either 0 or 1. Entering a cell with value 1
reduces health by 1, while entering a cell with value 0 costs nothing.
The starting cell's cost is included in the initial cost.

A min-heap always explores the path with the lowest total cost first.
Once a cell is popped from the heap, that is the cheapest possible way
to reach that cell, so we mark it as visited.

If the current cost is greater than or equal to health, the path is
unsafe because health must remain at least 1. If the bottom-right cell
is reached before that happens, return True.

Time Complexity: O(M * N * log(M * N))
Space Complexity: O(M * N)
"""
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        direction = [[0,1], [0,-1], [1,0], [-1,0]]
        M,N = len(grid), len(grid[0])
        visited = set()
        # cost, row, col
        minHeap = [(grid[0][0], 0, 0)]
        while minHeap:
            cost, row, col = heapq.heappop(minHeap)
            if cost >= health:
                return False
            if row == M - 1 and col == N - 1:
                return True
            if (row,col) in visited:
                continue
            visited.add((row,col))
            for dr,dc in direction:
                new_r, new_c = row + dr, col + dc
                if (new_r, new_c) in visited or new_r < 0 or new_r >= M or new_c < 0 or new_c >= N:
                    continue
                heapq.heappush(minHeap, (cost + grid[new_r][new_c], new_r, new_c))
        
        return False     
            
            
        
        
