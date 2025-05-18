"""
This problem can be optimized from O(n × 26) to O(n), but the trick isn’t obvious.
Core Idea:
We maintain a sliding window, and at every step, check this condition: (window length) - (most frequent character count) <= k  
This tells us whether the current window can be turned into all the same character with at most k replacements.

Optimization:

We don’t need to update the most frequent character count (max_freq) when shrinking the window.

Key Insight:
We’re maximizing the window length under a strict constraint.
Only when the most frequent character is at its peak will it produce the longest valid window.
Once max_freq drops (after shrinking), we don't care anymore —
it won’t lead to a better result, so we don’t bother updating it.

⚠️ Why It Feels Wrong:
The logic seems off — we’re using a max_freq that may become outdated during shrinking, and the math can look incorrect in those moments. In fact, the max_freq does stay stale and might not reflect the actual frequency in the current window.

But this is an acceptable "wrong", because the non-valid window will not be the longest window anyways. The invalid window cannot be longer than a valid earlier one (since you are shrinking the window), 
 and therefore will never beat the true max length, so the outdated max_freq never causes incorrect answers — it just helps us avoid unnecessary recomputation.

"""


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # O(n) solution
        char_counts = {}
        count, left, max_freq = 0,0,0

        for right in range(len(s)):
            char_counts[s[right]] = 1 + char_counts.get(s[right], 0)
            if char_counts[s[right]] > max_freq:
                max_freq = char_counts[s[right]]
            
            while right - left + 1 - max_freq > k:
                char_counts[s[left]] -= 1
                left += 1
            count = max(count, right-left + 1)

        return count
