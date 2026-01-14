"""
Removes duplicates from a sorted singly-linked list in-place.

Because the list is sorted, duplicate values always appear consecutively.
Traverse the list once using two pointers:
- `prev` tracks the last unique node kept
- `curr` scans ahead for duplicates

When `curr.val == prev.val`, skip `curr` by linking `prev.next` to `curr.next`.
Otherwise, advance both pointers.

Time: O(n)
Space: O(1)
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        dummy = head
        prev = dummy
        curr = head.next
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
                curr.next = None
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        return dummy
