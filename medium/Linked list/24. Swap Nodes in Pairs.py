"""
Swap nodes of a singly linked list in adjacent pairs *in-place* using three
moving pointers (`prevprev`, `prev`, `curr`) and a dummy head.

Summary
-------
- Rewires pointers to transform:  prevprev -> prev(a) -> curr(b) -> next
  into:                           prevprev -> b -> a -> next
- Advances the trio to the next candidate pair without extra storage.

Pointers & Invariant
--------------------
- `prevprev` : node *before* the current pair (starts at `dummy`).
- `prev`     : first node of the pair (`a`).
- `curr`     : second node of the pair (`b`).
Invariant at loop entry: the sublist beginning at `prevprev.next` is
either an intact pair (`prev`, `curr`) or we terminate if `curr` is None.

Algorithm (one iteration)
-------------------------
1) Detach `a` from `b` and connect `a` to `b.next`:
     prev.next = curr.next
2) Place `b` in front of `a`:
     curr.next = prev
3) Hook the swapped pair back to the prefix:
     prevprev.next = curr
4) Prepare to advance:
     curr = prev.next         # node after the swapped pair
     prevprev = prevprev.next # now points to `b`
   If there isn't a full next pair (`not curr or not curr.next`), exit.
   Otherwise move each pointer into position for the next pair:
     curr = curr.next         # next pair's second node
     prev = prev.next         # next pair's first node
     prevprev = prevprev.next # node before that next pair

Edge Cases
----------
- Empty list or single node: returns as-is.
- Odd length: the last node remains unswapped by construction.

Complexity
----------
Time:  O(n)  — each node is visited/relinked a constant number of times.
Space: O(1)  — in-place, only a few pointers.

Correctness Notes
-----------------
- The dummy head ensures the head swap is handled uniformly.
- The loop guard/early break guarantees swaps happen only on full pairs,
  so no `None` dereferences and the tail (if odd) is preserved.

Returns
-------
Optional[ListNode]
    The head of the pairwise-swapped list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0, head)
        prevprev = dummy
        prev = head
        curr = head.next
        while curr:
            prev.next = curr.next
            curr.next = prev
            prevprev.next = curr
            curr = prev.next
            prevprev = prevprev.next
            if not curr or not curr.next:
                break
            curr = curr.next
            prev = prev.next
            prevprev = prevprev.next
        return dummy.next
            


        
