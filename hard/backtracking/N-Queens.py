class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:  
        nv_col, nv_l_diagonal, nv_r_diagonal = set(),set(), set()
        queens = []
        res = []

        def backtrack(r):
            if r == n:
                return
            for c in range(n):
                if c in nv_col or r + c in nv_l_diagonal or r - c in nv_r_diagonal:
                    continue
                queens.append([r,c])
                if len(queens) == n:
                    board = []
                    for i in range(n):
                        board.append("")
                        for j in range(n):                          
                            if [i,j] in queens:
                                board[i] += "Q"
                            else:
                                board[i] += "."
                    res.append(board)                               
                    queens.pop()
                    return
                nv_col.add(c)
                nv_l_diagonal.add(r+c)
                nv_r_diagonal.add(r-c)
                backtrack(r + 1)
                queens.pop()
                nv_col.remove(c)
                nv_l_diagonal.remove(r+c)
                nv_r_diagonal.remove(r-c)
        backtrack(0)
        return res
       

        
        
