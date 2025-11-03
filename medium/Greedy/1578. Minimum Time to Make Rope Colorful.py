"""
Return the minimum total time to remove balloons so that no two adjacent
balloons share the same color.

Idea:
Scan left→right with two indices:
- `prev` tracks the index of the *most expensive* balloon kept so far
  within the current run of identical colors.
- When colors[prev] == colors[curr], we must delete one of them. Pay the
  cheaper one (add min(neededTime[prev], neededTime[curr]) to `res`) and
  keep the more expensive as the new `prev`. This ensures that across a
  whole run of equal colors we keep exactly the one with maximum time and
  delete/pay all others.
- When the color changes, start a new run (`prev = curr`).

Correctness:
In any maximal run of identical colors, exactly one balloon must remain.
The cheapest way is to keep the balloon with maximum removal time and pay
the sum of the rest. The algorithm simulates this greedily in one pass by
always retaining the current max within the run.

Complexity:
- Time: O(n) single pass over the string
- Space: O(1) extra space

Edge cases:
- All colors already distinct → cost 0
- Entire string one color → sum(all) - max(all)
- Ties in neededTime handled (either choice costs the same)
"""
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) == 1:
            return 0
        prev, curr = 0, 1
        res = 0
        while curr < len(colors):
            if colors[prev] != colors[curr]:
                prev = curr
                curr += 1
                continue    
            if neededTime[prev] > neededTime[curr]:
                res += neededTime[curr]
            else:
                res += neededTime[prev]
                prev = curr
            curr += 1
        return res

                    
