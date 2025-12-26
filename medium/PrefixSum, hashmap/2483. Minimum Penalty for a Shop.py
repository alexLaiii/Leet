"""
LeetCode 2483: Minimum Penalty for a Shop

Idea:
Consider closing the shop at hour t (0 <= t <= n), meaning:
  - Open during hours [0 .. t-1]
  - Closed during hours [t .. n-1]

Penalty definition:
  - For each 'N' while open: +1 (staffed but no customers)
  - For each 'Y' while closed: +1 (customers came but shop closed)

Therefore:
  penalty(t) = (# of 'N' in prefix [0..t-1]) + (# of 'Y' in suffix [t..n-1])

One-pass tracking:
  - prevN: number of 'N' seen so far (open-hours penalty for the prefix)
  - YLost: number of 'Y' remaining to the right (closed-hours penalty for the suffix)
      Initialize YLost = total count of 'Y' in the whole string.
      As we scan hour i, moving from considering close at i to close at i+1:
        * if customers[i] == 'Y', that 'Y' shifts from "closed suffix" to "open prefix",
          so decrement YLost.
        * if customers[i] == 'N', it contributes to open penalty, so increment prevN.

At each index i, compute the penalty for closing at hour (i + 1):
  currLost = prevN + YLost

We keep the earliest hour with the minimum penalty by only updating when currLost < minLost
(not <=), so ties do not overwrite the earlier answer.

Complexity:
  - Time: O(n)
  - Space: O(1)
"""

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prevN = 0
        prevY = 0
        YLost = 0
        for n in customers:
            if n == "Y":
                YLost += 1
        minLost = YLost
        res = 0
        for i in range(len(customers)):
            
            if customers[i] == "Y":
                YLost -= 1
            else:
                prevN += 1
            currLost = YLost + prevN
            if currLost < minLost:
                minLost = currLost
                res = i + 1

        return res 
