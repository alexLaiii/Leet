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


        
