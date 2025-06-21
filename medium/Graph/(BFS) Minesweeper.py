"""
BFS problem in practice.

"""


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        M, N = len(board), len(board[0])
        
        start_r, start_c = click[0], click[1]
        if board[start_r][start_c] == "M":
            board[start_r][start_c] = "X"
            return board

        directions = [[-1,-1], [-1,0], [-1,1],
                    [0,-1],          [0,1],
                    [1,-1],   [1,0], [1,1]]
        inQ = set()
        q = deque([(start_r, start_c)])
        inQ.add((start_r, start_c))
       
        while q:
            r,c = q.popleft()
            mine_count = 0
            for dr, dc in directions:
                # out of bound cell
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= M or nc >= N:
                    continue
                if board[nr][nc] == "M":
                    mine_count += 1
            if mine_count > 0:
                board[r][c] = str(mine_count)
            else:
                board[r][c] = "B"
                for dr, dc in directions: 
                    # out of bound cell
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= M or nc >= N:
                        continue
                    if board[nr][nc] == "E" and (nr, nc) not in inQ:
                        inQ.add((nr,nc))
                        q.append((nr,nc))
                    
        return board
        
        
