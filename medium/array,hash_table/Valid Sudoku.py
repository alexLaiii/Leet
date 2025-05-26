"""
Idea: Keep track of any duplicate value contains in each row, column, cell, return False immediately if duplicate is found, otherwise, return True if all cases passed

Implementation:
Initialize 3 different hash_table to store the value in row, column, and cell
row_check: {row_number : value[]} pair
col_check: {col_number : value[]} pair
cell_check: {cell_number : value[]} pair 
Example value:
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

For the above Sudoku, Assume the first 3 rows is ran, then:
row_check = { 0 : ["5","3","7"], 1 : ["6","1","9","5"], 2 : ["9","8","6"] } -> contains the first 3 completed rows
col_check = { 0 : ["5","6"], 1 : ["3","9"], 2 : ["8"], 3 : ["1"], 4:["7","9"], 5:["5"], 7:["6"] } -> contains 9 incomplete columns
cell_check = { 0: ["5","3","6","9","8"], 1:["7","1","9","5"], 2:["6"] } -> contains the first 3 cell (completed in this case, but not always true)
The rest are following the same idea

Time complexity: O(n^2) -> assume the passing board size is n x n, we need to visit every element
Space complexity: O(n^2 + n^2 + n^2) in worst case, Worst case: all element are valid Integers, no "".
                  each n^2 corresponding to "row_check", "col_check", "cell_check" respectively.
"""





class Solution(object):
    def isValidSudoku(self, board):
        row_check, col_check, cell_check = {},{},{}
        for rows in range(len(board)):
            for cols in range(len(board[rows])):
                if board[rows][cols] != '.':
                    # row duplicate check start 
                    if rows in row_check and board[rows][cols] in row_check[rows]:
                        return False
                    row_check[rows] = row_check.get(rows, [])
                    row_check[rows].append(board[rows][cols])
                    # col duplicate check start
                    if cols in col_check and board[rows][cols] in col_check[cols]:
                        return False
                    col_check[cols] = col_check.get(cols, [])
                    col_check[cols].append(board[rows][cols])
                    # cell duplicate check start
                    cell_nums = 3 * (rows//3) + (cols//3)
                    if cell_nums in cell_check and board[rows][cols] in cell_check[cell_nums]:
                        return False
                    cell_check[cell_nums] = cell_check.get(cell_nums, [])
                    cell_check[cell_nums].append(board[rows][cols])
    
        return True
