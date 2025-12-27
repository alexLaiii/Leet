  """
  Brute-force simulation using a heap of meetings (start-time order) + O(n) room scan.

  We need to process meetings in increasing start time. Instead of sorting `meetings`,
  we push all (start, end) into a min-heap so we can pop the next meeting in
  chronological order.

  State:
  - roomEndtime[i]: the next time room i becomes available (initially 0 for all rooms)
  - usedCount[i]:   how many meetings have been assigned to room i

  For each meeting (start, end) popped from the meeting-heap:
  1) Scan rooms from i = 0..n-1 to find an assignment:
     - If we find a free room (start >= roomEndtime[i]), we must use the
       smallest-index free room, so we pick the first such i and start at `start`.
     - If no room is free, we must delay the meeting and pick the room whose
       end time is smallest (earliest release). If multiple rooms tie on end time,
       we pick the smallest index (achieved naturally by scanning and only updating
       the candidate when we find a strictly smaller end time).
  2) Increment usedCount for the chosen room.
  3) Update that room's end time:
       actual_start_time + (end - start)
     (meeting duration is preserved even if delayed).

  Complexity:
  - Building meeting heap: O(m log m)
  - For each meeting, scanning up to n rooms: O(m * n)
  - Total: O(m log m + m*n), with n <= 100 typically acceptable for m up to 1e5.

  Space:
  - O(m) for the meeting heap, O(n) for roomEndtime/usedCount.
  """

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        roomEndtime = [0] * n
        usedCount = [0] * n
        
        minHeap = []
        for start, end in meetings:
            heapq.heappush(minHeap, (start, end))
        
        while minHeap:
            start, end = heapq.heappop(minHeap)
            earliestRoom = 0
            earliestTime = float("inf")
            for i in range(n):
                if start >= roomEndtime[i]:
                    earliestRoom = i
                    earliestTime = start
                    break
                elif roomEndtime[i] < earliestTime:
                    earliestTime = roomEndtime[i]
                    earliestRoom = i
         
            usedCount[earliestRoom] += 1
            roomEndtime[earliestRoom] = earliestTime + (end - start)

        mostUsedRoom = 0
        for i in range(n):
            if usedCount[i] > usedCount[mostUsedRoom]:
                mostUsedRoom = i
        return mostUsedRoom
            

        

            

        
