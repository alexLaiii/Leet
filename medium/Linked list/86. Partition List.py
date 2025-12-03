
"""
Reorder the linked list so that all nodes with value < x appear before nodes
with value >= x, while preserving the original relative order within each group.

This is done with a stable partition using two separate lists:
- `left` list collects nodes with val < x.
- `right` list collects nodes with val >= x.
We iterate the original list once, detach each node, append it to the
appropriate list, and finally connect `left` to `right`.

Args:
    head: Head of the original singly-linked list.
    x: Pivot value used to partition the list.

Returns:
    The head of the partitioned list where all nodes with val < x come
    before all nodes with val >= x, with relative order preserved.

Time Complexity:
    O(n), where n is the number of nodes in the list (single pass).

Space Complexity:
    O(1) extra space (only a few pointers and two dummy nodes are used;
    nodes are rearranged in-place).
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftDummy = ListNode()
        rightDummy = ListNode()
        left= leftDummy
        right = rightDummy
        curr = head
        while curr:
            nextN = curr.next
            curr.next = None
            if curr.val < x:
                left.next = curr
                left = left.next
            else:
                right.next = curr
                right = right.next
            curr = nextN
        left.next = rightDummy.next
        return leftDummy.next


"""
Messy approach
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        split = head
        dummyHead = ListNode()
        dummyHead.next = head
        prevBack = ListNode()
        prevBack.next = split
        while(split and split.val < x):
            prevBack = prevBack.next
            split = split.next

        curr = split
        while(curr):
            temp = curr.next
            tempNext = curr.next
            if curr.val < x:
                prev = dummyHead
                headCurr = dummyHead.next
                while(headCurr != split and headCurr.val < x):
                    prev = headCurr
                    headCurr = headCurr.next
                
                prevBack.next = curr.next
                prev.next = curr
                curr.next = headCurr
            else:
                prevBack = prevBack.next
            curr = temp
         
    
        return dummyHead.next
