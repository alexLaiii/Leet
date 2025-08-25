  """
  Note:
  This problem is similar tp " 373. Find K Pairs with Smallest Sums "
  
  Find the k-th smallest element in a row- and column-sorted matrix
  using a min-heap + BFS-style expansion.

  Approach:
      - The matrix is sorted both row-wise and column-wise.
      - Start from the smallest element at (0,0) in a min-heap.
      - Repeatedly pop the smallest element from the heap. 
        Each pop is effectively "visiting" the next element 
        in the sorted order of the entire matrix.
      - After popping (r, c), push its two neighbors:
          (r+1, c)  -> next row in the same column
          (r, c+1)  -> next column in the same row
        Only push if within bounds and not already visited.
      - Continue until the k-th pop; that element is the answer.

  Why it works:
      - Because rows and columns are sorted, (r+1, c) and (r, c+1) 
        are the only possible candidates that could be larger 
        but still close to the current popped element.
      - By always expanding from the globally smallest available 
        candidate, the heap produces elements in ascending order.
      - A visited set ensures we never push duplicates.

  Complexity:
      - Time: O(k log k)
          * We perform k heap pops.
          * Each pop can push up to 2 new elements, so heap size ≤ O(k).
          * Heap operations cost log k.
      - Space: O(k) for the heap and visited set.

  """

import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # k * log(k) 
        N = len(matrix)
        minHeap = [(matrix[0][0], 0, 0)]
        visited = set()
        visited.add((0,0))
        smallesth, res = 0, 0
        while minHeap and smallesth < k:
            res, row, col = heapq.heappop(minHeap)
            if row + 1 < N and (row + 1, col) not in visited:
                heapq.heappush(minHeap, (matrix[row + 1][col], row + 1, col))
                visited.add((row + 1, col))
            if col + 1 < N and  (row, col + 1) not in visited:
                heapq.heappush(minHeap, (matrix[row][col + 1], row, col + 1))
                visited.add((row, col + 1))
            smallesth += 1
        return res
