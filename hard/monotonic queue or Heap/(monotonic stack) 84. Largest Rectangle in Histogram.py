"""
Calculates the area of the largest rectangle that can be formed in a histogram.

Given an array `heights` representing the heights of bars in a histogram (each bar has width 1),
this function uses a monotonic increasing stack to efficiently determine the largest possible
rectangle that can be formed using consecutive bars.

Core Idea:
- We use a stack to keep track of histogram bars in increasing order of height.
- Each element in the stack is a tuple: (height, leftmost_index_that_bar_can_extend_to)
- When we see a bar shorter than the top of the stack, we:
    1. Pop the taller bar.
    2. Calculate the area that this bar could have extended to:
       - Width = current index - the stored left boundary index.
       - Area = height × width
    3. We also update the current bar's `furthest` index to allow shorter bars
       to extend left through previously popped taller bars.
- After scanning all bars, we may still have bars left in the stack (which were never closed by a shorter bar).
  For these, the right boundary is the end of the histogram (index = len(heights)).

Steps:
1. Loop over each bar in `heights`:
    - If the current bar is taller than or equal to the top of the stack, push it.
    - If it's shorter, keep popping until the stack is empty or the top is shorter than the current bar.
      For each pop, compute the maximal area using the popped bar as the smallest height.
      Store the left boundary (furthest) so the current bar knows how far back it can extend.
2. After the loop, flush the remaining bars in the stack using the histogram's end as the right boundary.

Time Complexity:
    - O(n): Each bar is pushed and popped from the stack at most once.

Space Complexity:
    - O(n): In the worst case, all bars are increasing and stored in the stack.

Example:
    Input: heights = [2, 1, 5, 6, 2, 3]
    Stack process and flush will compute:
        - Area from 5 and 6 → width 2 → area = 10
        - Area from 1 → width 6 → area = 6
        - Max area overall = 10
    Output: 10
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
    
            furthest = i
            while stack and heights[i] < stack[-1][0]:
                h, idx = stack.pop()
                maxArea = max(maxArea, h * (i - idx))
                furthest = idx
            stack.append((heights[i], furthest))

        while stack:
            h, idx = stack.pop()
            maxArea = max(maxArea, h * (len(heights) - idx))
        return maxArea
            
        
                        
        
