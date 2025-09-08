"""
LeetCode 658 — Find K Closest Elements (Two-Pointer after Binary Search)

Problem
-------
Given a sorted array `arr`, an integer `k`, and a target `x`, return the `k`
elements closest to `x`. If there is a tie, prefer the smaller values.
Output must be in ascending order.

Idea
----
1) Do a binary search to locate where `x` would fit: return a pair (i, j)
   such that i points to the last value <= x and j points to the first value >= x
   (i.e., a "split" around x, like bisect_left semantics).
2) Expand two pointers outward from this split to pick the closer of `arr[i]`
   and `arr[j]` at each step until we have `k` elements.
   - If distances tie, take from the left (`arr[i]`) to satisfy the
     "prefer smaller values" rule.
3) Use a deque: when taking from the left, `appendleft`; from the right,
   `append`. This keeps the result in sorted order without a final sort.

Why this works
--------------
In a sorted array, the `k` closest elements form a contiguous window.
Expanding from the insertion point of `x` always pulls in the next closest
boundary element; tie-breaking to the left ensures the required order rule.

Algorithm
---------
- Binary search to find (i, j) with `arr[i] <= x <= arr[j]` (or the nearest
  boundary when x is outside the array).
- While we still need elements:
    * If i < 0, we must take from the right.
    * If j >= n, we must take from the left.
    * Otherwise compare |arr[i] - x| vs |arr[j] - x|:
        - If left <= right, take left (appendleft and i -= 1).
        - Else take right (append and j += 1).
- Return the deque as a list.

Edge cases handled
------------------
- x smaller than all elements  → return `arr[:k]`.
- x larger than all elements   → return `arr[-k:]`.
- Duplicates around x          → still expands correctly; ties prefer left.
- k may be 0 or as large as len(arr).

Complexity
----------
Time:  O(log n) for the search + O(k) for expansion → O(log n + k).
Space: O(k) for the output deque (no extra sorting step).

Preconditions
-------------
- `arr` must be sorted ascending.
"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = deque()

        def findPosition(arr):
            l,r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] <= x and mid + 1 < len(arr) and arr[mid + 1] >= x:
                    return (mid, mid + 1)
                if arr[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            return (l,r)
        
        i,j = findPosition(arr)
        if i >= len(arr):
            return arr[len(arr) - k :]
        if j < 0:
            return arr[0: k]
        
        while k:
            if i < 0:
                res.append(arr[j])
                j += 1
            elif j >= len(arr):
                res.appendleft(arr[i])
                i -= 1
            elif abs(arr[i] - x) <=  abs(arr[j] - x):
                res.appendleft(arr[i])
                i -= 1
            else:
                res.append(arr[j])
                j += 1
            k -= 1
        
        return list(res)
"""
Solution 2: Binary Search on windows


-------------------
Binary-search the BEST **start index of window** `s` of the optimal length-`k` window.
Search space is `s ∈ [0, n-k]`. For a midpoint `mid`, compare the two adjacent
windows:
  - Left window:  arr[mid : mid+k]       (left boundary = arr[mid])
  - Right window: arr[mid+1 : mid+k+1]   (right boundary = arr[mid+k])

Decision rule
-------------
Compute boundary gaps:
    left_gap  = x - arr[mid]
    right_gap = arr[mid + k] - x
- If `right_gap >= left_gap` → keep/move **left** (`r = mid`)
- Else (right_gap < left_gap) → move **right** (`l = mid + 1`)
Using `>=` encodes the tie-break "prefer smaller elements" (stay left on ties).

Why this works (correctness sketch)
-----------------------------------
Adjacent k-windows differ by exactly one element: `arr[mid]` vs `arr[mid+k]`.
Whichever boundary is closer to `x` determines the better window among the two.
Define `g(s) = (x - arr[s]) - (arr[s+k] - x) = 2x - arr[s] - arr[s+k]`.
As `s` increases, both `arr[s]` and `arr[s+k]` are non-decreasing, so `g(s)` is
non-increasing (monotone). Binary search finds the smallest `s` with `g(s) <= 0`,
i.e., the leftmost optimal window per the tie rule.

"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Binary Search on windows
        l,r = 0, len(arr) - k
        while l < r:
            mid = (l + r) // 2
            # If right Difference to x >= left Difference to x: then the better starting point must be further left
            if x - arr[mid] <= arr[mid + k] - x:
                r = mid
            # If right Difference to x < left Difference to x: then the better starting point must be further right
            else:
                l = mid + 1
        
        return arr[l:l + k]
                
        
        
