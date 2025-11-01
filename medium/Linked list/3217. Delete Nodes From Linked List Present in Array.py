"""
Remove from a singly linked list all nodes whose values appear in `nums`.

Idea
----
Build a hash set of values to delete, then make a single pass through the list.
Keep a `dummy` head with a `candidates` tail pointer for the kept nodes:
  - If `curr.val` is NOT in the set, append `curr` to the kept list and advance.
  - Otherwise, skip `curr`.
Set `candidates.next = None` whenever you append to prevent stale links from
previously skipped nodes.

Correctness
-----------
Each node is visited exactly once and appended iff its value ∉ nums. Because we
always reconnect using `candidates.next` and null-terminate after each append,
the resulting list preserves the original relative order of kept nodes and has
no unintended cycles or leftover links.

Complexity
----------
Let n = length of the list, m = len(nums).
  - Time:  O(n + m)   (build set + single traversal)
  - Space: O(m)       (hash set of values to delete)

Edge Cases
----------
- `head is None`       → returns None.
- `nums` empty         → original list is returned unchanged.
- All values in nums   → returns None.
- Duplicates in nums   → harmless; set deduplicates.

Returns
-------
The head
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        hash_set = set()
        for n in nums:
            hash_set.add(n)
        dummy = ListNode()
        tail = dummy
        curr = head
        while curr:
            if curr.val not in hash_set:
                tail.next = curr
                tail = tail.next
                curr = curr.next
                tail.next = None
            else:
                curr = curr.next
                
        return dummy.next


                
                
