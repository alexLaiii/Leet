# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        N = 0
        curr = head
        last = head
        while curr:
            last = curr
            curr = curr.next
            N += 1
        if N == 0 or k == 0 or k % N == 0 or N == 1:
            return head
        new_head_Position = N - (k % N)
        curr = head
        i = 0
        while i < new_head_Position - 1:
            curr = curr.next
            i += 1
        new_head = curr.next
        curr.next = None
        last.next = head
        return new_head
        
