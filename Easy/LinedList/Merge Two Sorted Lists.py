# This doesn't feel like an easy if recursion is asked
"""
Recursive Intuition for Merging Two Sorted Linked Lists

Core Idea:
We want to merge two sorted linked lists into one sorted list.
Instead of using a loop, recursion lets us say:
  "Merge the rest, and I’ll attach the smaller node to the front."

Base Cases:
- If either list is empty, return the other list.
  This stops the recursion.

Recursive Step:
- Compare list1.val and list2.val
- Whichever is smaller becomes the current head
- Set its `.next` to the result of merging the rest
- Return that node as the new head

This way, the merged list is built from front to back,
but the connections happen on the way *back up* the recursive calls.

Example:
list1: 1 -> 3 -> 5
list2: 2 -> 4 -> 6

Step 1: 1 < 2 → return 1, and merge [3,5] with [2,4,6]
Step 2: 2 < 3 → return 2, and merge [3,5] with [4,6]
Step 3: 3 < 4 → return 3, and merge [5] with [4,6]
Step 4: 4 < 5 → return 4, and merge [5] with [6]
Step 5: 5 < 6 → return 5, and merge [] with [6]
Step 6: list1 is empty → return list2 → [6]

Builds this final merged list:
1 → 2 → 3 → 4 → 5 → 6

Key Rule:
Only advance the list you took a node from.
"""

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
