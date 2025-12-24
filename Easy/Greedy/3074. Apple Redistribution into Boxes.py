"""
Return the minimum number of boxes needed to hold all apples.

Idea:
- Only the total number of apples matters because apples can be redistributed
  freely among boxes.
- To minimize how many boxes are used, greedily choose boxes with the largest
  capacities first.
- Sort capacities descending, then take a running sum until it reaches or
  exceeds total apples.

Correctness sketch (exchange argument):
- Suppose an optimal solution uses a box with smaller capacity while a larger
  unused box exists. Swapping in the larger box never decreases the total
  capacity covered, so we can transform any optimal solution into one that
  uses the largest boxes first. Therefore, the greedy prefix that first
  reaches the total apples is optimal.

Complexity:
- Time: O(m log m) for sorting capacities (m = len(capacity))
- Space: O(1) extra space (aside from sorting internals)
"""

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        total = sum(apple)
        cap = 0
        for i in range(len(capacity)):
            cap += capacity[i]
            if cap >= total:
                return i + 1

                
            
