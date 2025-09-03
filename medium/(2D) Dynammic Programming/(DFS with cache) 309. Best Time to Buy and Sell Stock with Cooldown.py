"""
This is super hard for me.

LeetCode 309 — Best Time to Buy and Sell Stock with Cooldown
Approach: Memoized DFS (top-down DP) over a decision tree (profit-to-go)

Key idea (decision tree)
------------------------
Think in terms of a *decision tree*:
- If we are in REST / COOLDOWN (not holding) → we can either **buy** or **skip** (rest).
- If we **bought** (i.e., we are HOLDING) → we can either **sell** or **keep holding** (which is just skipping).
- If we **sold today** → we must **cool down tomorrow**, so the next decision day jumps to **i + 2**.

State & meaning
---------------
dfs(i, canBuy) returns the **best future profit** from day i onward:
- i: day index
- canBuy == True  → we are NOT holding; allowed actions: buy or skip
- canBuy == False → we ARE holding; allowed actions: sell or hold

Transitions (profit-to-go)
--------------------------
Base: if i >= n → 0 (no more profit to earn)

If canBuy (not holding):
  buy today      → -prices[i] + dfs(i+1, False)
  skip (rest)    →  dfs(i+1, True)
  dfs(i, True)   = max(buy, skip)

If holding (already bought):
  sell today     → +prices[i] + dfs(i+2, True)   # one-day cooldown ⇒ i+2
  hold/skip      →  dfs(i+1, False)
  dfs(i, False)  = max(sell, hold)

Why memo works
--------------
We return *profit-to-go* (future gain only), which depends solely on (i, canBuy),
so caching by that key is valid and path-independent.

Complexity
----------
Time:  O(n) states × O(1) transitions ≈ O(n)
Space: O(n) for memo (plus recursion stack)

Answer
------
Return dfs(0, True) — best profit starting on day 0 when not holding.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in memo:
                return memo[(i, canBuy)]

            if canBuy:

                buy = dfs(i + 1, False) - prices[i]
                cooldown = dfs(i + 1, True)
                memo[(i, canBuy)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                cooldown = dfs(i + 1, False)
                memo[(i, canBuy)] = max(sell, cooldown)
            return memo[(i, canBuy)]

        return dfs(0, True)
            

                
        
