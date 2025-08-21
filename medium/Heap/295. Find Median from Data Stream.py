"""
Maintain the running median in O(log n) per insert using two heaps:
  - maxHeap (store negatives): lower half of numbers
  - minHeap: upper half of numbers

Intuition:
  Split the stream into two halves so that every number in the lower half
  (maxHeap) is <= every number in the upper half (minHeap). The median is
  on the boundary: either the top of maxHeap (odd count) or the average of
  both tops (even count). After each insertion, restore:
    1) Order invariant: max(lower) <= min(upper)
    2) Size invariant: len(maxHeap) == len(minHeap) or len(maxHeap) == len(minHeap) + 1
       (i.e., lower may hold one extra)
"""

import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        
    def addNum(self, num: int) -> None:
        """
        Insert one number while preserving the two-heap invariants.
    
        Classification rule:
          - If maxHeap is non-empty and num < -self.maxHeap[0], push to maxHeap (lower half).
          - Elif minHeap is non-empty and num > self.minHeap[0], push to minHeap (upper half).
          - Else: push to maxHeap by convention. Either side is valid here because `num`
            lies between the two tops and will sit at the boundary regardless.
    
        Rebalance:
          - If len(maxHeap) -1 > len(minHeap): move the top of maxHeap to minHeap.
          - If len(minHeap) -1 > len(maxHeap): move the top of minHeap to maxHeap.
    
        Rationale:
          - The comparisons place `num` on the correct side of the boundary.
          - Rebalancing restores the size invariant while preserving order:
            max(lower) ≤ min(upper).
    
        Complexity: O(log n) per insert (heap push/pop); O(1) to read the median.
        """
        if self.maxHeap and -num > self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        elif self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        if len(self.maxHeap) - 1 > len(self.minHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) - 1 > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        
    def findMedian(self) -> float:
        """
        O(1) median query:
          - If lower has one extra element, return top(maxHeap).
          - Otherwise return the average of top(maxHeap) and top(minHeap).
        """

        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
       
        return (self.minHeap[0] + (-self.maxHeap[0])) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
