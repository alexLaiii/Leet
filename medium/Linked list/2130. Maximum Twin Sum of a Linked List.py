"""
Calculates the maximum twin sum of an even-length linked list.

The solution first counts the total number of nodes, then stores the first
half of the list in a stack. It then traverses the second half while popping
from the stack, which gives the matching twin node from the first half in
reverse order. For each twin pair, it updates the maximum sum found.

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        N = 0
        while curr:
            curr = curr.next
            N += 1
        half = N // 2
        curr = head
        res = 0
        stack = []
        for i in range(half):
            stack.append(curr.val)
            curr = curr.next
        for i in range(half):
 
            res = max(res, stack[-1] + curr.val)
            stack.pop()
            curr = curr.next
            
        return res
            

        
        
        
