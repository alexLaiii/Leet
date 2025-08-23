    """
    Return all valid IPv4 addresses that can be formed from `s` (LeetCode 93).

    Core idea (DFS / backtracking over 4 segments):
      Build the address left→right by choosing exactly 4 segments. At each step:
        • If the next char is '0', the only valid segment is "0" (no leading zeros like "01").
        • Otherwise, try growing a segment s[start:i+1] and accept it while its integer
          value ≤ 255. As soon as the value exceeds 255, stop exploring longer slices from
          this start (they will only be larger) — in this implementation we `return` from
          the current call, which acts like a `break` for this branch.

    How this code enforces validity:
      • `segment` counts how many segments remain to be chosen (must end at exactly 0).
      • A result is recorded only when `segment == 0` AND the string is fully consumed
        (`start >= len(s)`), ensuring exactly 4 segments cover the entire string.
      • Leading-zero rule: when s[start] == '0', we take only that single digit as a segment.
      • Range rule: segments converted to int must be in [0, 255].
      • Dots are appended during construction; the final trailing dot is removed with `ip[:-1]`.

    Useful pruning (optional to add for speed/clarity):
      • Length feasibility: let rem = len(s) - start and left = segment. If
          rem < left  or  rem > 3*left, prune (not enough / too many chars to fill remaining segments).
      • Bound the inner loop to at most 3 digits:
          for i in range(start, min(len(s), start + 3)): ...
        (Functionally equivalent here because values > 255 trigger an early stop.)

    Complexity:
      Depth is fixed at 4 segments with branching up to ~3 per level (1–3 digits), so the
      search space is small (≈ 3^4). Each validity check is O(1); string concatenations
      add a small overhead.

    Edge notes:
      • If len(s) < 4 or > 12, there can be no valid addresses (the search will naturally return []).
      • Using character checks (e.g., s[start] == '0') avoids unnecessary int conversions.
    """


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(segment, start, ip):
            if segment == 0:
                if start >= len(s):
                    res.append(ip[:-1])
                return
            if start >= len(s):
                return
            
            if int(s[start]) == 0:
                backtrack(segment - 1, start + 1, ip + s[start] + ".")
            else:
                for i in range(start, len(s)):
                    if int(s[start:i + 1]) >  255:
                        return
                    backtrack(segment - 1, i + 1, ip + s[start:i + 1] + ".")
        
        backtrack(4, 0, "")
        return res
                        
                
