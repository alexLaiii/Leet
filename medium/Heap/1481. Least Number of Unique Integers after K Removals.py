  """
  Greedy (min-heap over frequencies).
  Count how often each integer appears, 
  then remove entire integers starting
  from the smallest frequency until k deletions are used up.
  This minimizes the number of unique integers that remain.

  Time:  O(n + u log u), where u = # of unique integers
  Space: O(u)
  """

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        minHeap = []

        count = defaultdict(int)
        for n in arr:
            count[n] += 1
        
        for c in count.values():
            heapq.heappush(minHeap, c)
            
 
        while minHeap:
            duplicates = heapq.heappop(minHeap)
            k -= duplicates
            if k == 0:
                return len(minHeap)
            elif k < 0:
                return len(minHeap) + 1
        
        return 0
