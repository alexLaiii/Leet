"""
Count buildings that are "covered" in all 4 cardinal directions.

A building at coordinate (x, y) is considered covered if:
  - On the same vertical line x, there exists at least one building with smaller y
    (below) AND at least one building with larger y (above).
  - On the same horizontal line y, there exists at least one building with smaller x
    (left) AND at least one building with larger x (right).

Approach (sort + interior check):
1) Group points by x (columns) and by y (rows):
     xMap[x] = list of points [x, y] sharing the same x
     yMap[y] = list of points [x, y] sharing the same y
2) Sort each group:
     - For xMap[x], sorting orders points by y (since x is constant), so the
       "interior" points (indices 1..len-2) have both an above and below neighbor.
     - For yMap[y], sorting orders points by x (since y is constant), so the
       first and last elements are the leftmost/rightmost in that row.
3) First collect candidates that are interior in their column (covered vertically).
4) For each candidate (x, y), check row coverage by ensuring x is NOT equal to the
   minimum x or maximum x in yMap[y] (i.e., not leftmost/rightmost). If true, it is
   covered horizontally as well, so count it.

Notes:
- `n` is unused in this implementation; only the given coordinates matter.
- Assumes building coordinates are unique (typical for this problem). If duplicates
  exist, counts may be inflated.

Complexity:
- Let m = len(buildings).
- Building the maps: O(m)
- Sorting all column/row groups: O(m log m) total across all groups
- Candidate scan + counting: O(m)
- Space: O(m)

Returns:
- Integer count of buildings covered in all 4 directions.
"""

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xMap, yMap = defaultdict(list), defaultdict(list)
        for x,y in buildings:
            xMap[x].append([x,y])
            yMap[y].append([x,y])
        
        for e in xMap:
            xMap[e].sort()
        for e in yMap:
            yMap[e].sort()

        candidates = []
        res = 0
        for e in xMap:
            for i in range(1, len(xMap[e])):
                if i + 1 < len(xMap[e]):
                    candidates.append(xMap[e][i])
        for x,y in candidates:     
            if yMap[y][0][0] != x and yMap[y][-1][0] != x:
                res += 1
        return res
        
