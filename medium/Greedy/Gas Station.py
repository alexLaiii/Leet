"""
Determine the starting gas station index from which you can travel 
around the circuit once without running out of gas.

Approach (Greedy — Reset on Failure):
-------------------------------------
- Let diff[i] = gas[i] - cost[i] be the net gas gained/lost at station i.
- If the total net gas over all stations is negative, no solution exists.
  (Because the car will always lose more gas than it gains.)
- Otherwise, there is exactly one valid starting station.

Greedy Invariant:
- Maintain `tank`: current net gas since the last chosen start.
- Iterate through stations in order:
    1. Add the current station's net gas to `tank`.
    2. If `tank` is negative, it means starting anywhere in the current 
       segment (from the last start to this station) would fail before 
       reaching this station.
       => Reset `start` to the current station index and set `tank` to 
          this station's net gas (effectively starting fresh here).
- Maintain `total` (in this code called `debt`, but inverted) as the sum 
  of all -diff values, to check if the journey is possible at all.

Why the reset works:
- If starting at `start` fails at station `i`, then any starting index
  between `start` and `i` would have even less gas upon reaching `i`
  (because you’d skip some of the positive net gas earlier in the segment
  or encounter the same deficits). So none of them can work, and the only
  candidate left is `i` itself.

Complexity:
- Time: O(n) — one pass through the stations.
- Space: O(1) — only a few variables.

Edge cases:
- Returns -1 if the total gas < total cost.
- Works when gas[i] == cost[i] for some stations (tank may reset or carry on).
- Works for circular routes with exactly one valid start (guaranteed by the problem).
"""



class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        tank = 0
        debt = 0
        for i in range(len(gas)):
            
            debt += cost[i] - gas[i]
            if tank < 0:
                start = i
                tank = gas[i] - cost[i]
            else:
                tank += gas[i] - cost[i]
       
        return start if debt <= 0 else -1
