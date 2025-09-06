"""
This is a relatively easy problem If using Heap as a solution
Merge k sorted linked lists using a min-heap.

Idea:
- Keep a heap of the current smallest node from each list.
- Heap items are (node.val, tieBreaker, node), where tieBreaker is the
  list index `i` the node came from. This tiebreaker prevents Python
  from comparing `ListNode` objects when values are equal and gives a
  total ordering for tuples.

How it works:
1) Push each non-empty list head as (val, i, node).
2) Pop the smallest; append it to the output (via dummy/tail).
3) If that node has a next, push (next.val, i, next) using the SAME
   tieBreaker `i`, so the heap always holds at most one node per list.

Correctness:
- The heap always contains the smallest unmerged node from each list,
  so repeated pop→append yields a globally sorted merge.

Complexity:
- Time: O(N log k) for N total nodes, k lists (each node push+pop).
- Space: O(k) extra for the heap (plus O(N) for the result).
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        minHeap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minHeap, (lists[i].val, i, lists[i]))
        
        prevNode = ListNode()
        dummy = prevNode
 
        while minHeap:
            currVal, tieBreaker, currNode= heapq.heappop(minHeap)
            if currNode.next:
                heapq.heappush(minHeap, (currNode.next.val, tieBreaker, currNode.next))
            prevNode.next = currNode
            prevNode = currNode
        return dummy.next
