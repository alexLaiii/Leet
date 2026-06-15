"""
Deletes the middle node from a singly linked list.

If the list has only one node, returns None. Otherwise, uses a right pointer
to scan through the list and moves the left pointer once every two right-pointer
moves, so left stops at the node before the middle node. The middle node is then
removed by skipping over left.next.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        # the left.next is to remove
        left = head
        right = head
        moved = 0
        while right.next:
            if moved == 2:
                left = left.next
                moved = 0
            right = right.next
            moved += 1
        
        temp = left.next
        left.next = temp.next
        temp.next = None
        return head
            
            
        
