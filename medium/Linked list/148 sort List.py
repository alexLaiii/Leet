"""
Sort a singly linked list using a min-heap.

Push each node into a min-heap as (value, tie_breaker, node) so
nodes with equal values never require comparing ListNode objects.
Then repeatedly pop from the heap and relink nodes to build a
new sorted list. Time: O(n log n), Extra space: O(n).
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        minHeap = []
        curr = head
        count = 0
 
        while curr:
            heapq.heappush(minHeap, (curr.val, count, curr))
            count += 1
            prev = curr
            curr = curr.next
            prev.next = None
     
        x,y, newhead = heapq.heappop(minHeap)
        curr = newhead
        while minHeap:
            val, tiebreaker, node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next

        return newhead
            
        
