"""
Easy one, follow it along
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = r = head
        while r and r.next:
            l = l.next
            r = r.next
            if r:
                r = r.next
    
        return l
