  """
  Return the k pairs (u, v) with the smallest sums where u ∈ nums1 and v ∈ nums2.

  Intuition (heap frontier over a monotone grid):
  - Visualize a matrix of sums S[i][j] = nums1[i] + nums2[j].
    Because both arrays are sorted ascending, each row i is nondecreasing as j increases,
    and each column j is nondecreasing as i increases.
  - The global minimum is at (0,0). From any cell (i,j), the only strictly new candidates
    that can beat future sums are its right neighbor (i, j+1) and its down neighbor (i+1, j).
  - Use a min-heap as a "frontier" of the smallest unseen candidates. Start from (0,0),
    repeatedly pop the smallest cell, append its pair to the answer, and push its two neighbors
    if in-bounds and not seen before.

  Why this works (correctness sketch):
  - Monotonicity: moving right increases nums2[j], moving down increases nums1[i], so sums
    do not decrease along rows/columns. Therefore, once (i,j) is popped as the smallest,
    every cell left/above it has already been considered; the only next plausible minima are
    (i, j+1) and (i+1, j).
  - The min-heap always contains the smallest unseen candidates along this frontier, so each pop
    yields the next smallest pair in global order.

  Data structures / invariants:
  - minHeap stores tuples (sum, i, j) with sum = nums1[i] + nums2[j].
  - visited prevents pushing the same grid cell twice (since both neighbors are explored).
    NOTE: initialize as `{(0, 0)}` (a set with one tuple), not `set((0,0))`.

  Complexity:
  - Each pop produces one answer; at most k pops.
  - Each pop pushes up to 2 new neighbors, each push/pop costs O(log H) where H is heap size.
  - Heap size is O(k) in the worst case for this neighbor-expansion style.
  - Overall time: O(k log k). Space: O(k) for heap + visited.

  Constraints / edge cases:
  - Requires nums1 and nums2 to be sorted ascending for the monotone frontier argument.
  - LeetCode guarantees k ≤ len(nums1) * len(nums2) and non-empty arrays; under these constraints,
    a for-loop of k iterations is safe (the heap won’t empty early).
  - If adapting elsewhere, guard for k == 0 or empty arrays.

  Alternatives:
  - Row-seeding variant: seed (i, 0) for i in [0, min(len(nums1)-1, k-1)] and only push (i, j+1).
    That keeps heap size ≤ min(len(nums1), k) and avoids a visited set, with complexity
    O(k log min(len(nums1), k)).
  """


import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        visited = {(0, 0)}
        minHeap = [[nums1[0] + nums2[0], 0, 0]]
        for i in range(k):
            sums, idx1, idx2 = heapq.heappop(minHeap)
            res.append([nums1[idx1], nums2[idx2]])
            if idx1 + 1 < len(nums1) and (idx1 + 1, idx2) not in visited:
                visited.add((idx1 + 1, idx2))
                heapq.heappush(minHeap, [nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2])
            if idx2 + 1 < len(nums2) and (idx1, idx2 + 1) not in visited:
                visited.add((idx1, idx2 + 1))
                heapq.heappush(minHeap, [nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1])
        return res



            
        
