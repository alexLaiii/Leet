"""
Compute the length of both linked lists and align the starting pointers so that
they have the same number of nodes remaining.

If one list is longer, advance its pointer by the length difference. After this
adjustment, both pointers are equally far from the end of their respective lists.
Traverse the two lists simultaneously until either:

* The two pointers reference the same node (intersection found), or
* Both pointers reach the end of the lists (no intersection).

Time Complexity: O(m + n)
- Traverse both lists once to compute their lengths.
- Advance the longer list by the length difference.
- Traverse both aligned pointers together.

Space Complexity: O(1)
- Only a constant amount of extra space is used.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_A = len_B = 0
        curr = headA
        while curr:
            len_A += 1
            curr = curr.next
        curr = headB
        while curr:
            len_B += 1
            curr = curr.next
        
        adjustHead_A = headA
        adjustHead_B = headB
        if len_A > len_B:
            for i in range(abs(len_A - len_B)):
                adjustHead_A = adjustHead_A.next
        else:
            for i in range(abs(len_A - len_B)):
                adjustHead_B = adjustHead_B.next
        
        while adjustHead_A and adjustHead_B:
            if adjustHead_A == adjustHead_B:
                return adjustHead_A
            adjustHead_A = adjustHead_A.next
            adjustHead_B = adjustHead_B.next
        return None
            
        
        
