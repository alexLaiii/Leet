"""
LeetCode 2144 — Minimum Cost of Buying Candies With Discount

Idea:
    Sort prices in descending order so each group of 3 has the two most
    expensive first and the cheapest last. With the "buy 2 get 1 free"
    rule, you pay for indices 0,1, skip 2; pay for 3,4, skip 5; etc.
    That guarantees every third candy (when sorted desc) is free.

Algorithm:
    1) Sort cost in reverse order.
    2) Iterate and add prices except when index % 3 == 2.

Correctness:
    Grouping in descending order ensures the free item in each triple is
    the cheapest of that triple, maximizing the discount globally.

Complexity:
    Time:  O(n log n) for sorting; O(n) scan.
    Space: O(1) extra (in-place sort).

Edge cases:
    - n < 3: no free items; sum all.
    - All equal prices: skip every third as usual.
"""

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        i = 0
        spent = 0
        buy = 0
        while i < len(cost):
            if buy != 2:
                spent += cost[i]
                buy += 1
            else:
                buy = 0
            i += 1
        return spent
        
                
                
