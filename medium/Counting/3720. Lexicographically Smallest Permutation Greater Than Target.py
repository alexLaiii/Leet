"""
Return the lexicographically smallest permutation of s that is
strictly greater than target, or "" if no such permutation exists.

Approach:
1. Greedily match target's prefix using s's letters for as long as
   possible, tracking the max matchable prefix length `i`.
2. Starting from position `i` (or `i-1` if s fully matches target)
   and walking left, find the rightmost position `j` where some
   remaining letter is strictly greater than target[j]. Diverging
   as late as possible keeps the result as close to (and just
   above) target as possible, which is what makes it minimal.
   At each step left, the letter that was tentatively used at the
   old position is returned to the pool before testing the new
   position, since it's no longer part of the matched prefix.
3. Fill every position after `j` with the smallest remaining
   letters in ascending order, giving the smallest possible
   arrangement for the tail.

Args:
    s: string whose letters (as a multiset) form the permutation.
    target: string to exceed; same length as s.

Returns:
    The smallest permutation of s greater than target, or "" if
    none exists (e.g. target already uses s's letters in their
    maximum/descending arrangement).

Time: O(n) — n positions, each doing O(26) work over the fixed
      lowercase-letter alphabet.
Space: O(n) for the result buffer, O(26) for the frequency map.
"""

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # the res must be at least as long as target
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        larger = False
        i = 0
        res = [""] * len(s)
        while i < len(s) and freq[target[i]] >= 1:
            res[i] = target[i]
            freq[target[i]] -= 1
            i += 1
        j = i if i < len(s) else i - 1
 
        while j >= 0 and not larger:
            character = "z"
            for c, f in freq.items():
                if f > 0 and c > target[j]:
                    character = min(c, character)
                    larger = True

            if i > j:
                    freq[target[j]] += 1
            if larger:
                res[j] = character
                freq[character] -= 1
            else:
                j -= 1
        if j < 0:
            return ""
        for k in range(j + 1, len(s)):
            character = "z"
            for c, f in freq.items():
                if f > 0:
                    character = min(character, c)
            res[k] = character
            freq[character] -= 1
        return "".join(res)
                
            
            
    
