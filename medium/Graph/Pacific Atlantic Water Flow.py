"""
Idea:
Instead of asking "Can I reach both the Pacific and Atlantic oceans from this cell?", we reverse the DFS logic:

→ From a Pacific or Atlantic border cell, can I reach some inner cell?
If yes, that inner cell can flow *to* the ocean that next to the border cell, since water flows from higher to lower or equal elevation.
This reverse traversal gives us all the cells that can eventually reach an ocean.

Since each cell is visited once per ocean, the overall time complexity is:
O(m * n + m * n) → O(m * n),
where m and n are the dimensions of the grid. This is significantly better than the naive approach,
which performs DFS from every cell without memoization, leading to O((m * n)^2) in the worst case.

Implementation:
We initialize two sets — `pacific` and `atlantic` — to store cells that can flow to the Pacific and Atlantic oceans respectively.

The `dfs(r, c, visited, prev_height)` function:
- Is called from a border cell
- Recursively explores all valid neighbors that are ≥ the previous height
- Every cell reached this way can flow to the starting border (i.e., the ocean)

⚠️ Key point:
Because we’re reversing the flow direction (from ocean to land), the traversal condition is:
`heights[curr] >= heights[prev]`
This ensures that in the **normal direction**, water would have flowed *down* from `curr` to `prev`.

Outer loop explanation:
- In the first loop (looping over columns), we search all the cells that can flow to the **top border (Pacific)** and **bottom border (Atlantic)**.
- In the second loop (looping over rows), we search all the cells that can flow to the **left border (Pacific)** and **right border (Atlantic)**.

❗Important:
Even though some DFS calls may overlap and visit the cells that is plan for the later index in the for loop, we must **still loop over every border cell**.  
Why? Because some border cells may be **isolated** — unable to flow into any neighbor.  
If we skipped them, we would miss valid answers (e.g., an edge cell with high elevation that doesn’t flow anywhere else).  
The `visited` set ensures these redundant DFS calls are cheap (O(1)), so there is **no performance cost**, but **full correctness** is guaranteed.

After the DFS completes, the intersection of the `pacific` and `atlantic` sets gives us all the cells that can flow to **both** oceans.

Time Complexity: O(m * n)
Each cell is visited at most twice (once per ocean)

Space Complexity: O(m * n)
Two sets (pacific & atlantic) store up to m * n elements
"""




class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r,c, visited, prev_height):
            if r >= m or c >= n or r < 0 or c < 0 or (r,c) in visited or heights[r][c] < prev_height:
                return
            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for i in range(n):
            # From top row: search all cells that can flow to the **top edge** of the Pacific Ocean
            dfs(0, i, pacific, 0)

            # From bottom row: search all cells that can flow to the **bottom edge** of the Atlantic Ocean
            dfs(m - 1, i, atlantic, 0)

        for i in range(m):
            # From left column: search all cells that can flow to the **left edge** of the Pacific Ocean
            dfs(i, 0, pacific, 0)

            # From right column: search all cells that can flow to the **right edge** of the Atlantic Ocean
            dfs(i, n - 1, atlantic, 0)


        return [[r,c] for r in range(m) for c in range(n) if (r,c) in pacific and (r,c) in atlantic]

"""
Naive brute force solution:
DFS everycell and check if it can reach both ocean
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        res = []
        
        def dfs(r,c, prev_height, flow):
         
            if r < 0 or c < 0:
                # flow to Pacific
                flow[0] = True
                return flow
            if (r >= m or c >= n):
                flow[1] = True
                return flow
            if (r,c) in visited or heights[r][c] > prev_height :
                return flow
            visited.add((r,c))
            if flow != [True, True]:
                flow = dfs(r + 1, c, heights[r][c], flow)
                flow = dfs(r - 1, c, heights[r][c], flow)
                flow = dfs(r, c + 1, heights[r][c], flow)
                flow = dfs(r, c - 1, heights[r][c], flow)
            
            return flow
        
            
        for r in range(m):
            for c in range(n):
                visited = set()
                if dfs(r,c, heights[r][c], [False,False]) == [True, True]:
                    res.append([r,c])
        return res


        
