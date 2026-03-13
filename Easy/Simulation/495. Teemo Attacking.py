"""
Return the total number of seconds that Ashe remains poisoned.

Each attack at time t poisons Ashe for `duration` seconds, covering the
half-open interval [t, t + duration). If a new attack occurs before the
previous poison effect ends, the intervals overlap and should not be
counted twice.

This solution tracks the current poison interval using `attackStart`
and `attackEnd`.

For each attack time `t`:
- If `t >= attackEnd`, the previous poison interval has ended, so add
  its full length (`attackEnd - attackStart`) to the result.
- Otherwise, the new attack overlaps with the current poison interval,
  so only add the non-overlapping portion (`t - attackStart`).

Then reset the current interval to start at `t` and end at `t + duration`.

After processing all attacks, add the final poison interval length
(`duration`) to the result.

Time Complexity:
    O(n), where n is the length of `timeSeries`.

Space Complexity:
    O(1).

Args:
    timeSeries: A sorted list of attack times.
    duration: The poison duration caused by each attack.

Returns:
    The total poisoned duration.
"""

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        attackEnd= 0
        attackStart = 0
        res = 0
        for t in timeSeries:
            if t >= attackEnd:
                res += attackEnd - attackStart
            else:
                res += t - attackStart
            attackStart = t
            attackEnd = t + duration
        return res + duration

        
