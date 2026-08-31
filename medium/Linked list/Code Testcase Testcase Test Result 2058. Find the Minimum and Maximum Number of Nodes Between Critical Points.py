"""
Find the minimum and maximum distance between critical points in a linked list.

A critical point is a node (other than the first or last) that is either
a local maximum (greater than both neighbors) or a local minimum (less than
both neighbors). This does a single pass, tracking the index of the first
critical point found and the most recently found one, updating the minimum
gap between consecutive critical points on the fly, then computing the
maximum gap as the distance between the first and last critical points.

Args:
    head: Head of the singly linked list.

Returns:
    A two-element list [minDistance, maxDistance] between critical points,
    or [-1, -1] if fewer than two critical points exist.

Time: O(n), single pass over the list.
Space: O(1) auxiliary.
"""
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = lastCrit = -1
        minDis = float("inf")
        prev = head
        curr = head.next
        i = 1
        while curr.next:
            if prev.val < curr.val > curr.next.val or prev.val > curr.val < curr.next.val:
                if first == -1:
                    first = i
                if lastCrit != -1:
                    minDis = min(minDis, i - lastCrit)
                lastCrit = i
            prev = curr
            curr = curr.next
            i += 1
        minDis = minDis if minDis != float("inf") else -1
        maxDis = lastCrit - first if lastCrit != first else -1
        return [minDis, maxDis]
                
                
        
