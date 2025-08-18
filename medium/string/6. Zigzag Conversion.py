"""
Zigzag Conversion using row-simulation (0-based rows).
Example:
Input: "PAYPALISHIRING"

ZIGZAG:
P   A   H   N
A P L S I I G
Y   I   R

Output:"PAHNAPLSIIGYIR"

What this does
---------------
Simulate the exact row index sequence a zigzag layout would produce:
0 → 1 → … → numRows-1 → numRows-2 → … → 1 → 0 → … (a “pendulum”).
Maintain per-row buffers in `allRows`, append each character of `s` to
the current row `curr_row`, and flip direction only at the top (row 0)
or bottom (row numRows-1). Concatenate rows top→bottom at the end.

Why it works
------------
The visual zigzag is fully determined by that periodic row-index pattern
(cycle length = 2*(numRows-1)). By reproducing the same sequence while
streaming characters, each char lands in the same row as in the diagram;
reading rows in order matches the problem’s required output.

Invariants
----------
- 0 <= curr_row < numRows at all times.
- `downward == True` ⇒ next step tries `curr_row += 1`; otherwise `curr_row -= 1`.
  Direction toggles only when hitting row 0 or row numRows-1.

Complexity
----------
Time: O(n) — each character appended once.
Space: O(n) — total size of row buffers (plus O(numRows) bookkeeping).

Edge cases
----------
- numRows == 1: no zigzag; return s (handled here).
- (Optional) When numRows >= len(s), returning s directly is equivalent.
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        curr_row = 0
        downward = True
        allRows = defaultdict(list)
        for i in range(len(s)):
            allRows[curr_row].append(s[i])
         
            if downward:
                if curr_row < numRows - 1:
                    curr_row += 1
                else:
                    downward = False
                    curr_row -= 1
            else:
                if curr_row > 0:
                    curr_row -= 1
                else:
                    downward = True
                    curr_row += 1
        
        return "".join("".join(allRows[row]) for row in range(numRows))
        
            
        
