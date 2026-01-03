"""
Add two non-negative integers represented by linked lists in reverse order.

Each input list stores digits least-significant first (e.g., 342 is 2 -> 4 -> 3).
We simulate grade-school addition from LSD to MSD by walking both lists together,
maintaining a `carry`, and building the result list on the fly.

Approach:
- Use a dummy head to simplify list construction.
- While either list still has nodes:
  * Read current digits (0 if the list is exhausted).
  * Compute sum = d1 + d2 + carry.
  * Append a node with digit (sum % 10).
  * Update carry = sum // 10.
  * Advance l1/l2 if possible.
- After the loop, if carry remains, append one final node (value 1).

Correctness notes:
- Handles different lengths by treating missing digits as 0.
- Carry is always 0 or 1 because digits are 0–9.

Time Complexity: O(m + n) where m, n are lengths of l1 and l2.
Space Complexity: O(m + n) for the output list (O(1) extra aside from output).
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        carry = 0
        while l1 or l2:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            val = d1 + d2 + carry
            prev.next = ListNode(val % 10)
            carry = val // 10
            prev = prev.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        if carry == 1:
            prev.next = ListNode(1)
        return dummy.next
            


                
            

            
        
        
