"""
Return the minimum number of seconds needed to reduce the mountain height to zero.

Each worker with base time t needs t, 2t, 3t, ... seconds for each successive
unit of mountain they reduce. This solution uses a min-heap to always choose
the worker who will finish their next unit earliest.

The heap stores:
    (current_finish_time, next_add_time, base_time)

Time complexity: O(mountainHeight * log w), where w is the number of workers.
Space complexity: O(w).
"""

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        minHeap = []
        # tuple format: (finish_time, next_chunk_time, base_time)
        # finish_time means the worker’s next completion time.
        # next_chunk_time means the worker's next completion time for 1 height
        for t in workerTimes:
            heapq.heappush(minHeap, (t,t,t))
            
        for i in range(mountainHeight - 1):
            total_time, add_time, base_time = heapq.heappop(minHeap)
            heapq.heappush(minHeap, (total_time + add_time + base_time, add_time + base_time, base_time))
        
        res, _, _= heapq.heappop(minHeap)
        return res
