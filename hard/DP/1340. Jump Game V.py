"""
LeetCode 1340. Jump Game V

Idea:
We want dp[i] to mean the maximum number of indices we can visit starting from index i.

From index i, we are allowed to jump left or right by at most d positions, but only to an index
with a strictly smaller value. Also, if we meet an index with value >= arr[i], we must stop
checking further in that direction because it blocks all jumps beyond it.

Key insight:
A jump is only possible from a larger value to a smaller value. Therefore, if we process indices
in increasing order of arr[i], then whenever we are computing dp[i], all possible jump targets
with smaller values have already had their dp values computed.

Algorithm:
1. Sort indices by their array values from smallest to largest.
2. Initialize dp[i] = 1 for every index, because we can always visit the starting index itself.
3. For each index i in sorted order:
   - Check up to d steps to the right.
   - Stop if out of bounds or if arr[next] >= arr[i].
   - Otherwise, update dp[i] = max(dp[i], 1 + dp[next]).
   - Do the same to the left.
4. Return max(dp), the best starting point.

Why sorting works:
Because every valid jump target has a smaller value than the current index.
So processing from low values to high values guarantees that dp[target] is already known.

Time Complexity:
O(n log n + n * d)
Sorting takes O(n log n), and for each index we may scan up to d positions left and right.

Space Complexity:
O(n)
We store the dp array and the sorted index order.
"""

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        N = len(arr)
        visit_order = sorted(range(N), key=lambda i: arr[i])
        dp = [1] * N
        
        for i in visit_order:
            maxVisit = 1
            for j in range(1, d + 1):
                if not(i + j < N and arr[i] > arr[i + j]):
                    break
                maxVisit = max(maxVisit, 1 + dp[i + j])
            for j in range(1, d + 1):
                if not(i - j >= 0 and arr[i] > arr[i - j]):
                    break
                maxVisit = max(maxVisit, 1 + dp[i - j])
            dp[i] = maxVisit

        return max(dp)
                
        
