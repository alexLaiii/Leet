class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        # uv stands for unvalid
        uv_rows, uv_cols, uv_l_diagonal, uv_r_diagonal = set(), set(),set(), set()
        queens = set()

        def backtrack(r):
            if r == n:
                return 
            for c in range(n):
                if c in uv_cols or r + c in uv_l_diagonal or r - c in uv_r_diagonal:
                    continue
                queens.add((r,c))
                if len(queens) == n:
                    self.res += 1
                uv_rows.add(r)
                uv_cols.add(c)
                uv_l_diagonal.add(r+c)
                uv_r_diagonal.add(r-c)

                backtrack(r+1)

                queens.remove((r,c))
                uv_rows.remove(r)
                uv_cols.remove(c)
                uv_l_diagonal.remove(r+c)
                uv_r_diagonal.remove(r-c)
           
        backtrack(0)
        return self.res

