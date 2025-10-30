"""
Compute the next greater element for each value in nums1, where nums1 ⊆ nums2 and
nums2 contains distinct values (per LC 496). Scan nums2 once with a monotonic
decreasing stack: while the current x is greater than the stack top, pop the top
and record x as its next-greater. Unpopped items have no next-greater (-1).

Time:  O(len(nums2) + len(nums1))   # each element pushed/popped at most once
Space: O(len(nums2))                # map + stack
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        nextGreater = defaultdict(int)
        for i in range(len(nums2)):
            
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                nextGreater[val] = nums2[i]
            stack.append(nums2[i])
        res = []
        for n in nums1:
            if n not in nextGreater:
                res.append(-1)
            else:
                res.append(nextGreater[n])
        
        return res
        
            
