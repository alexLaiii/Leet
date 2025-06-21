"""
### 🧠 Idea:

Easy DFS problem with a condition and in-place modification on the image.

You start from the given pixel and find all adjacent cells that:
- Have the **same color as the original**
- Are **not already the target color**

Then you change each of those cells to the target color. That’s it.

---

### ✅ Key Points:
- Only modify cells that match the original color
- Prevent infinite recursion if the original color equals the target color
- In-place update ensures minimal space usage

---

### ⏱ Time Complexity:
- **O(m × n)**  
  In the worst case, you visit every cell once (if all cells have the original color).

---

### 🗂 Space Complexity:
- **O(m × n)** worst case due to DFS recursion stack  
  Each recursive call goes one level deep per cell in the worst case (e.g., fully connected region).
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        M, N = len(image), len(image[0])
        ori_c = image[sr][sc]
        def dfs(r,c):
            if r < 0 or c < 0 or r >= M or c >= N or  image[r][c] != ori_c or image[r][c] == color :
                return
            image[r][c] = color
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr,dc in directions:
                dfs(r + dr, c + dc)

        dfs(sr,sc)
        return image
        
