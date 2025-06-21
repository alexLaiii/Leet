"""
### 🧠 BFS Practice: Minesweeper (Leetcode 529)

This problem is a good simulation-based BFS exercise.

---

### 🧩 Before we dive into the idea, understand the three core rules:

#### Minesweeper Reveal Rules:
1. **Mine clicked (`'M'`)**:
   - The game is over.
   - Change the clicked cell to `'X'`.

2. **Empty cell (`'E'`) with no adjacent mines**:
   - Change the cell to `'B'` (blank).
   - Recursively reveal all 8 surrounding unrevealed squares.

3. **Empty cell (`'E'`) with at least one adjacent mine**:
   - Change the cell to a digit (`'1'`–`'8'`) representing the number of adjacent mines.
   - Do not reveal any neighboring cells.

Once no more cells are revealed, return the updated board.

---

### 💡 BFS Strategy

We use **BFS** to implement Rule #2: recursively revealing all connected blank cells.

#### Step-by-step logic:
1. Start from the clicked cell.
2. If it’s a mine → mark as `'X'` and return.
3. Otherwise, begin BFS using a queue.

---

### 🔁 During BFS:

For each cell we process:
- **Count how many adjacent cells are mines** (check all 8 directions).
- If **mine count > 0**:
  - Apply **Rule #3**: mark current cell as the count (`'1'`–`'8'`)
  - **Do not add its neighbors to the queue** (not neigbour exploration needed)
- If **mine count == 0**:
  - Apply **Rule #2**: mark the cell as `'B'`
  - Then explore its adjacent neighbors via BFS

---

### ⚠️ When not to add adjacent cells to the queue:
Only add a neighbor if:
- It has **not already been added to the queue**
- It hasn’t already been revealed (`'B'` or `'1'`–`'8'`)
The above is same as saying:
- Only add a neighbor if "It is currently `'E'`

This prevents:
- Revisiting already revealed cells
- Redundant BFS processing

---

### ✅ Final Step:
When the BFS finishes, the board will reflect the correctly revealed state.
Return the updated board.

### ⏱ Time Complexity:
- **O(m × n)**  
  Every cell is visited at most once during BFS. For each cell, we may check up to 8 neighbors.

### 🗂 Space Complexity:
- **O(m × n)** worst case  
  In the worst case, the entire board could be queued if all are blank `'E'` cells.
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
        
        
