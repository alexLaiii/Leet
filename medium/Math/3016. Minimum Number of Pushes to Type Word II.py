"""
Count the frequency of each character and assign the most frequent
characters to the cheapest button presses.

Since a keypad can hold at most 8 characters per press count:
- The 8 most frequent characters require 1 push.
- The next 8 require 2 pushes.
- The next 8 require 3 pushes.
- The remaining characters require 4 pushes.

Sorting the frequencies in descending order guarantees that the
total number of button presses is minimized (a greedy strategy),
because assigning smaller costs to larger frequencies always
produces the minimum possible sum.

Time Complexity:
    O(n), where n = len(word). Sorting is performed on only 26
    elements, which is constant time.

Space Complexity:
    O(1), since the frequency array has a fixed size of 26.
"""

class Solution:
    def minimumPushes(self, word: str) -> int:
        char_freq = [0] * 26
        for c in word:
            char_freq[ord(c) - ord("a")] += 1
        char_freq.sort(reverse=True)
       
        res = 0
        for i in range(26):

            if i < 8:
                res += char_freq[i]
            elif i < 16:
                res += char_freq[i] * 2
            elif i < 24:
                res += char_freq[i] * 3
            else:
                res += char_freq[i] * 4
        return res
        
