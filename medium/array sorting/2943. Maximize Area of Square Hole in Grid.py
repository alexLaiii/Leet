"""
Key Idea:
----------
We want to maximize the area of a square hole after removing some horizontal
and vertical bars.

Removing k consecutive bars creates a gap of size (k + 1).

So:
- Longest consecutive horizontal removals → determines maximum height
- Longest consecutive vertical removals → determines maximum width
- The largest square we can form is limited by the smaller of the two

Therefore:
    side = min(max_consecutive_h, max_consecutive_v) + 1
    area = side^2

Algorithm:
----------
1. Sort hBars and vBars.
2. For each list, compute the longest sequence of consecutive integers.
3. Let:
       h = longest consecutive in hBars
       v = longest consecutive in vBars
4. Compute:
       side = min(h, v) + 1
5. Return side * side

Important Notes:
----------------
- Bars are indexed from 1 to n+2 (or m+2), where 1 and n+2 are edge bars.
- Edge bars cannot be removed, but input guarantees only removable bars are given.
- Defensive coding (optional): filter out bars <= 1 or >= n+2 if unsure.

Time Complexity:
----------------
O(H log H + V log V) due to sorting

Space Complexity:
-----------------
O(1) extra space (excluding sorting)
"""
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        
        horizontal_consecutive = 0 if hBars[0] == 1 else 1
        vertical_consecutive = 0 if vBars[0] == 1 else 1
        h_count = horizontal_consecutive
        v_count = vertical_consecutive
        for i in range(1, len(hBars)):
            horizontal_b = hBars[i]
            if horizontal_b < n + 2 and horizontal_b == hBars[i-1] + 1:
                h_count += 1
                horizontal_consecutive = max(h_count, horizontal_consecutive)
            else:
                h_count = 1
        
        for j in range(1, len(vBars)):
            vertical_b = vBars[j]
            if vertical_b < m + 2 and vertical_b == vBars[j-1] + 1:
                v_count += 1
                vertical_consecutive = max(v_count, vertical_consecutive)
            else:
                v_count = 1
        side = min(vertical_consecutive, horizontal_consecutive) + 1 
        return side * side
                
            
        
