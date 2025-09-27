    """
    LeetCode 409 — Longest Palindrome (by rearranging characters)

    Approach (your logic, explained):
      - Count characters on the fly and maintain:
          1) odd_count  : number of distinct chars that currently have an odd frequency.
          2) max_palindrome: best palindrome length derivable from everything seen so far.
      - When a character's count flips from even->odd, odd_count += 1.
        When it flips from odd->even, odd_count -= 1.
        Thus, at any time:
            pairs_length_so_far = (processed_length) - odd_count
        because each odd bucket contributes one unpaired char that can’t be paired yet.
      - Each step updates:
            max_palindrome = max(max(hashMap[curr_char], pairs_length_so_far),
                                  max_palindrome)
        Intuition:
          • pairs_length_so_far uses every available pair (2, 4, 6, …) across all chars.
          • max(hashMap[curr_char], ...) ensures we never do worse than the largest
            single-char block seen (useful early on or in very skewed strings).

      - Final adjustment:
          If the best length so far is even and the total string has at least one leftover
          odd character (i.e., len(s) > max_palindrome), we can place exactly one odd
          in the center → add +1.
          Otherwise, return max_palindrome as-is.

    Why this works:
      - The maximum palindrome length from a multiset of characters equals:
            (sum over all chars of (count // 2) * 2)  +  (1 if any count is odd else 0)
        • pairs_length_so_far = processed_length - odd_count
          is exactly the running sum of all even pair contributions.
        • The final +1 adds a single center when any odd exists.

    Complexity:
      - Time:  O(n), single pass over s.
      - Space: O(k), where k ≤ 52 for letters (or at most the alphabet size used),
        due to the frequency map and a few integers.

    Notes / pitfalls:
      - Order in the input string doesn’t matter (we’re rearranging).
      - At most one odd-count character can contribute the central +1.
      - This implementation purposefully tracks a running best, but the canonical
        solution can also be written by first counting all characters and then applying
        the formula in one shot.
    """

class Solution:
    def longestPalindrome(self, s: str) -> int:

        hashMap = defaultdict(int)
        odd_count = 0
        max_palindrome = 0
        for i in range(len(s)):
            hashMap[s[i]] += 1
            if (hashMap[s[i]] - 1) % 2 == 0:
                odd_count += 1
            else:
                odd_count -= 1
            max_palindrome = max(max(hashMap[s[i]], i + 1 - odd_count), max_palindrome)

        return max_palindrome + 1 if len(s) > max_palindrome and max_palindrome % 2 == 0 else max_palindrome
            

            
