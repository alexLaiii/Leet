"""
Easy dfs problem with condition and inplace modification on image.

Find all the adjacent cell that has the same colour as the original color but not the target color.
And the change it to target colour, thats it

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
        
