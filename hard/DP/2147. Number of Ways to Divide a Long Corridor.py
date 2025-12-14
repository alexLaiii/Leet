  """
  LeetCode 2147 — Number of Ways to Divide a Long Corridor

  Idea (pair seats, multiply by choices between pairs):
  - Each valid section must contain exactly 2 seats 'S'.
  - Scan left to right and group seats into consecutive pairs (1st+2nd, 3rd+4th, ...).
    Whenever we complete a pair (hit the 2nd seat), record its index.
  - The last recorded pair-ending does NOT create a divider "choice" after it, so we drop it.
  - For every earlier pair-ending position `pos`, count the consecutive plants 'P'
    immediately after it until the next seat begins.
      If there are k plants, then there are (k + 1) possible places to put the divider:
      right after the pair-ending seat, or after any of those k plants.
    The total number of ways is the product of (k + 1) over all gaps between seat-pairs.

  How this code computes (k + 1) multiplicatively using DP-like addition:
  - Maintain two integers: `prevWays` and `currWays` (start at 1).
  - For each gap after a pair-ending seat:
      - Each time we see a plant 'P' in that gap, do: currWays += prevWays
        This simulates multiplying by (k + 1):
          after k plants, currWays becomes prevWays * (k + 1).
      - After finishing this gap, set prevWays = currWays to carry the product forward.

  Validity checks:
  - If we end the scan with an unpaired seat (seat == 1) -> impossible -> return 0.
  - If we never formed even one full pair (no recorded positions) -> impossible -> return 0.
  - Otherwise, pop the last pair-ending index (no divider choice after final section).

  Complexity:
  - Time: O(n). Each character is processed O(1) times; the inner while only advances
    through plants and overall never exceeds n steps.
  - Space: O(#pairs) for storing `corrPosition` (indices of pair-end seats).

  Returns:
  - Number of ways modulo 1_000_000_007.
  """

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        corrPosition = []
        seat = 0
        for i in range(len(corridor)):
            if corridor[i] == "S":
                seat += 1
            if seat == 2:
                corrPosition.append(i)
                seat = 0
        if seat == 0 and corrPosition:
            corrPosition.pop()
        elif seat == 1 or not corrPosition:
            return 0
        prevWays, currWays = 1,1
  

        for pos in corrPosition:
            while pos + 1 < len(corridor) and corridor[pos + 1] == "P":
                currWays = (currWays + prevWays) % (10 ** 9 + 7)
                pos += 1
            if pos + 1 < len(corridor):
                prevWays = currWays
        return currWays
                
        
                
                
            
            
