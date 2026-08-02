"""
This is the same problem as 486. Predict the Winner, please regarding the solution of that problem
"""
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        dp = [[0 for i in range(length)] for j in range(length)]
        for i in range(length):
            dp[i][i] = piles[i]
        for i in range(1, length):
            for j in range(length - i):
                last = j + i
                dp[j][last] = max(piles[last] - dp[j][last - 1], piles[j] - dp[j+1][last])
        
        return True if dp[0][length - 1] > 0 else False
                
            
        
