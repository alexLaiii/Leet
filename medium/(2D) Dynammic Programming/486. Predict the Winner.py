"""
Determine whether the first player (mover) can tie or win, assuming
both players play optimally, picking one pile from either end of
`nums` each turn.

Key idea: instead of tracking each player's absolute score (which
requires knowing both players' future choices simultaneously), track
the SCORE DIFFERENTIAL the current mover can guarantee:

    dp[i][j] = (current mover's score) - (opponent's score)
               for optimal play restricted to nums[i:j+1]

This works because the roles of "mover" and "opponent" swap with
every turn, but the recurrence doesn't care about identity, only
about whoever's turn it is on a given subarray:

    dp[i][j] = max(
        nums[j]   - dp[j][last-1],   # take right end, opponent
                                      # then nets dp[j][last-1] on
                                      # what's left
        nums[last] - dp[j+1][last],  # take left end, symmetric
    )

Subtracting the opponent's best differential on the remainder is
the crux: whatever edge they lock in there counts against you.

Base case: dp[i][i] = nums[i] (one pile left, just take it).

Fill order: subarrays are filled by increasing length (`i` here is
length-1, the offset between start and end index), since dp[i][j]
always depends only on strictly shorter subarrays.

Final answer: dp[0][n-1] is the first player's guaranteed margin
over the whole array. >= 0 means they can tie or win.

Time: O(n^2) states, O(1) work each -> O(n^2)
Space: O(n^2) for the table
"""

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)
        dp = [[0 for i in range(length)] for j in range(length)]
        for i in range(length):
            dp[i][i] = nums[i]
        for i in range(1, length):
            for j in range(length - i):
                last = j + i
                dp[j][last] = max(nums[last] - dp[j][last - 1], nums[j] - dp[j+1][last])
        
        return True if dp[0][length - 1] >= 0 else False
                                
