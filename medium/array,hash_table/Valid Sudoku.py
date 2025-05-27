"""
Idea:  
Keep track of any duplicate value contained in each row, column, and cell.  
Return False immediately if a duplicate is found, otherwise return True if all checks pass.

Implementation:  
Initialize 3 different hash tables (dictionaries) to store the values seen in:
- Each row (row_check)
- Each column (col_check)
- Each 3×3 cell (cell_check)

Each dictionary stores a set instead of a list to allow **O(1)** time complexity for checking if a value already exists.  
Sets are used because they:
- Avoid duplicates by nature (You can't have duplicates in this problem anyways)
- Allow fast membership checking (val in set) in constant time

Structure:
- row_check: { row_number : set of values }  
- col_check: { col_number : set of values }  
- cell_check: { cell_number : set of values }  

Example board:
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

For the above Sudoku, assume the first 3 rows are processed, then:

row_check = {  
  0: {"5", "3", "7"},  
  1: {"6", "1", "9", "5"},  
  2: {"9", "8", "6"}  
}  
→ contains the first 3 completed rows

col_check = {  
  0: {"5", "6"},  
  1: {"3", "9"},  
  2: {"8"},  
  3: {"1"},  
  4: {"7", "9"},  
  5: {"5"},  
  7: {"6"}  
}  
→ contains values seen in partially filled columns

cell_check = {  
  0: {"5", "3", "6", "9", "8"},  
  1: {"7", "1", "9", "5"},  
  2: {"6"}  
}  
→ contains values seen in each 3×3 sub-box (cell index = 3 * (row // 3) + (col // 3))

The same logic applies for the remaining rows, columns, and cells.

Time complexity: O(n^2)  
→ assuming the board size is n × n, we visit every element once

Space complexity: O(n^2 + n^2 + n^2) in the worst case  
→ Worst case: all elements are valid digits, no "."  
→ Each n^2 corresponds to row_check, col_check, and cell_check respectively
"""


class Solution(object):
    def isValidSudoku(self, board):
        row_check, col_check, cell_check = {},{},{}
        for row in range(len(board)):
            for col in range(len(board[row])):
                val = board[row][col]
                if val != '.':
                    cell_nums = 3 * (row//3) + (col//3)
                    # if that row/col/cell didnt exist yet, store the row and intialize as an empty list 
                    # if that row/col/cell exist, these lines do nothing
                    row_check.setdefault(row, set())
                    col_check.setdefault(col, set())
                    cell_check.setdefault(cell_nums, set())
                    # Check duplicate
                    if (val in row_check[row] or 
                        val in col_check[col] or 
                        val in cell_check[cell_nums]) :
                        return False
                    
                    # Add to seen
                    row_check[row].add(val)
                    col_check[col].add(val)
                    cell_check[cell_nums].add(val)
        return True


# class Solution(object):
#     def isValidSudoku(self, board):
#         row_check, col_check, cell_check = {},{},{}
#         for rows in range(len(board)):
#             for cols in range(len(board[rows])):
#                 if board[rows][cols] != '.':
#                     # row duplicate check start 
#                     if rows in row_check and board[rows][cols] in row_check[rows]:
#                         return False
#                     row_check[rows] = row_check.get(rows, [])
#                     row_check[rows].append(board[rows][cols])
#                     # col duplicate check start
#                     if cols in col_check and board[rows][cols] in col_check[cols]:
#                         return False
#                     col_check[cols] = col_check.get(cols, [])
#                     col_check[cols].append(board[rows][cols])
#                     # cell duplicate check start
#                     cell_nums = 3 * (rows//3) + (cols//3)
#                     if cell_nums in cell_check and board[rows][cols] in cell_check[cell_nums]:
#                         return False
#                     cell_check[cell_nums] = cell_check.get(cell_nums, [])
#                     cell_check[cell_nums].append(board[rows][cols])
    
#         return True

