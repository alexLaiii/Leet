"""
Solution:
Use a min-heap to maintain the top k largest elements.
The root of the min-heap (heap[0]) will always represent the kth largest element.

Example: nums = [5, 4, 8, 2], k = 3
The 3rd largest element is 4. We build a min-heap: [4, 5, 8].
The number 2 is excluded because it doesn't affect the result — we only keep the k largest elements.

Initialization:
- Heapify the input list.
- While the heap size > k, pop the smallest element until size == k.
- If the list has fewer than k elements, we keep all of them.

add(val) function:
1. If heap size < k:
   - We must add val, since any new number will affect the kth largest.
   - Push val and return heap[0].

2. If heap size == k:
   - If val <= heap[0], it has no impact on the top k — skip it and return heap[0].
   - If val > heap[0]:
       - Push val to the heap.
       - Pop the smallest element to maintain size k.
       - This may update the kth largest.

Example:
- Heap: [4, 5, 8], k = 3
- Add 6 → heap becomes [4, 5, 6, 8] → after pop → [5, 6, 8]
- kth largest becomes 5

In all cases, return heap[0] as the current kth largest element.

Time Complexity:
def __init__: O(n + (n−k) log n) -> worst case: O(n + nlogn) -> O(nlogn) overall
def add: O(logn)
"""


import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        if nums:
            heapq.heapify(self.heap)
            while len(self.heap) > k:
                heapq.heappop(self.heap)
        
    def add(self, val):
        if len(self.heap) == self.k and self.heap[0] > val:
            return self.heap[0]
   
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

            
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
