"""
Rotate each rectangular layer of the grid counter-clockwise by k positions.

Idea:
Treat each layer/ring of the matrix as a 1D array.

For each layer:
1. Extract the boundary values in order:
   - top row: left -> right
   - right column: top+1 -> bot-2
   - bottom row: right -> left
   - left column: bot-2 -> top+1

2. Rotate the extracted layer by k:
   Since the extraction order follows the counter-clockwise direction,
   rotating counter-clockwise by k is equivalent to:
       shifted_layer = layer[k:] + layer[:k]

3. Write the rotated values back into the same boundary positions
   using the same order as extraction.

Important slicing detail:
When extracting the bottom row in reverse, if left == 0, we must use:
    grid[bot - 1][right - 1::-1]
instead of:
    grid[bot - 1][right - 1:left - 1:-1]
because left - 1 becomes -1, and -1 is interpreted as the last index,
not "before index 0".

Time Complexity:
O(m * n), because every grid cell is extracted and reassigned once.

Space Complexity:
O(m + n) per layer, for storing the current boundary as a 1D array.
"""
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # bot and right is not the index instead it is the real length
        top, bot, left, right = 0, len(grid), 0, len(grid[0])
        while bot - top > 0 and right - left > 0:

            ### extract layer as array
            layer = grid[top][left:right]
            for i in range(top + 1, bot - 1):
                layer.append(grid[i][right - 1])
            if left == 0:
                layer += grid[bot - 1][right - 1::-1]
            else:
                layer += grid[bot - 1][right-1:left-1:-1]
            for j in range(bot - 2, top, -1):
                layer.append(grid[j][left])
            
            ### rotate
            kshift = k % len(layer)
            shifted_layer = layer[kshift:] + layer[:kshift]

            ### assign rotated version to grid
            grid[top][left:right] = shifted_layer[0:right - left]
            curr_idx = right - left
 
            for i in range(top + 1, bot - 1):
                grid[i][right - 1] = shifted_layer[curr_idx]
                curr_idx += 1
    
            grid[bot - 1][left:right] = shifted_layer[curr_idx + (right - left) - 1:curr_idx - 1: -1 ]
            curr_idx = curr_idx + (right - left)
  
            for j in range(bot - 2, top, -1):
        
                grid[j][left] = shifted_layer[curr_idx]
                curr_idx += 1   
            # modify
            top += 1
            bot -= 1
            left += 1
            right -= 1

        return grid
