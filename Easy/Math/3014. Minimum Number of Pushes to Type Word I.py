"""
Each phone key can hold at most one character at a given push count.
Since there are 8 available keys, the characters are grouped in batches
of 8:

- Characters 1-8 require 1 push each.
- Characters 9-16 require 2 pushes each.
- Characters 17-24 require 3 pushes each.
- Characters 25-26 require 4 pushes each.

The minimum number of pushes therefore depends only on the length of
the word. We add the contribution of each batch while capping its size
using min(...) to handle shorter words efficiently.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n <= 8:
            return n
        res = 8
   
        res += (min(n, 16) - 8) * 2
        if n > 16:
            res += (min(n, 24) - 16) * 3
        if n > 24:
            res += (n - 24) * 4
        
        
        return res
        
