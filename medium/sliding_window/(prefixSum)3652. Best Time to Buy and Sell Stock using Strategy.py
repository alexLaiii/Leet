  """
  Compute the maximum achievable gain by optionally applying one "strategy overwrite"
  operation on a contiguous window of length k.

  Problem model (as used by this solution)
  ---------------------------------------
  - Baseline gain is: sum(prices[i] * strategy[i]) over all days i.
  - You may choose ONE contiguous window of length k (k is assumed even).
  - Inside that window, the strategy is forced to:
      * first k/2 positions -> 0 (do not sell / contribute 0)
      * last  k/2 positions -> 1 (sell / contribute prices[i])
    Days outside the window keep their original strategy values.

  Key idea
  --------
  Precompute prefix/suffix sums so each candidate window can be evaluated in O(1).

  Precomputations
  --------------
  - prefix[i]     = sum_{t=0..i} prices[t] * strategy[t]
                   (baseline gain prefix; lets us add unchanged left part)
  - suffix[i]     = sum_{t=i..n-1} prices[t] * strategy[t]
                   (baseline gain suffix; lets us add unchanged right part)
  - sellPrefix[i] = sum_{t=0..i} prices[t]
                   (plain price prefix; lets us sum the forced "sell half" quickly)

  Window evaluation (window ends at i)
  -----------------------------------
  Let the window be [lower .. i], where lower = i - (k - 1).
  After overwriting the window:
  - Left of window:  unchanged baseline -> prefix[lower - 1] (if lower > 0)
  - Right of window: unchanged baseline -> suffix[i + 1]      (if i + 1 < n)
  - Inside window:
      * first half contributes 0
      * last half contributes sum(prices over the last k/2 elements of the window)

  The last-half sum is computed with sellPrefix as:
      sum(prices[i - k/2 + 1 .. i]) = sellPrefix[i] - sellPrefix[i - k/2]

  We take the maximum over:
  - doing nothing: prefix[n-1] (baseline)
  - applying the overwrite on each possible window of length k

  Complexity
  ----------
  Time:  O(n)  (three linear passes + one linear sweep over window ends)
  Space: O(n)  (prefix, suffix, sellPrefix arrays)

  Assumptions / Notes
  -------------------
  - k is even and 1 <= k <= len(prices) (typical problem constraint).
  - Index arithmetic uses inclusive prefix sums; be careful with off-by-one.
  """

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        prefix, suffix, sellPrefix = [prices[0] * strategy[0]],[0] * len(prices),[prices[0]]
        for i in range(1, len(prices)):
            prefix.append(prefix[i - 1] + (prices[i] * strategy[i]))
            sellPrefix.append(sellPrefix[i - 1] +  prices[i])
        suffix[-1] = prices[-1] * strategy[-1]
        for i in range(len(prices) - 2, -1, -1):
            suffix[i] = suffix[i + 1] + (prices[i] * strategy[i])
        
        bestGain = prefix[-1]
  
        for i in range(k - 1, len(prices)):
            lower = i - (k - 1)
            res = sellPrefix[i] - sellPrefix[i - (k//2)]
            if lower - 1 >= 0:
                res += prefix[lower - 1]
            if i + 1 < len(prices):
                res += suffix[i + 1]
            bestGain = max(bestGain, res)
        return bestGain
       
        
        
