"""
Compute the "X-sum" for every length-k subarray of nums.

For each window nums[i : i+k], let count[v] be the frequency of value v in the window.
Define the X-sum as the sum of the top x entries when values are ranked by
(frequency DESC, value DESC). Equivalently, take up to x distinct values with highest
(freq, value) and add freq * value for each.

Approach:
- For each window, build a frequency table.
- Push (−freq, −value) pairs into a heap to simulate a max-heap on (freq, value).
- Pop up to x items and accumulate (freq * value).

Correctness notes:
- Ties on frequency are broken by larger value first via the second key (−value).
- If there are fewer than x distinct values in the window, we take all of them.

Complexity:
- For each of the t = len(nums) − k + 1 windows:
    * Counting costs O(k)
    * Heap build/pop is O(m + x log m), where m ≤ k is the number of distinct values
  Overall ~ O(t * (k + x log k)) time and O(k) extra space per window.

Edge cases:
- x ≥ number of distinct values → we just sum all (freq * value).
- k = 1 → result is just the element itself (since freq=1).
"""

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        t = len(nums) - k + 1
        arr = []
        for i in range(t):
            maxHeap = []
            count = defaultdict(int)
            res = 0
        
            for j in range(i, i + k):
                count[nums[j]] += 1
            
            for e in count:
                heapq.heappush(maxHeap, (-count[e], -e))
        
            popped = 0
            while maxHeap and popped < x:
                freq, num = heapq.heappop(maxHeap)
                res += ((-num) * (-freq))
                popped += 1
            arr.append(res)
        return arr
            
            
                
