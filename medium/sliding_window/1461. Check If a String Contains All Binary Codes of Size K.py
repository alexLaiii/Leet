"""
Determine whether a binary string `s` contains every possible binary code
of length `k` as a substring.

Approach:
- Use a sliding window of size `k` to generate all substrings of length `k`.
- Store each substring in a set to ensure uniqueness.
- A binary code of length `k` has exactly 2^k possible distinct combinations.
- If the number of unique substrings collected equals 2^k, then all
possible binary codes of length `k` are present in `s`.

Parameters:
s (str): A binary string consisting only of '0' and '1'.
k (int): The length of binary codes to check.

Returns:
bool: True if all possible binary codes of size `k` appear in `s`,
    otherwise False.

Time Complexity:
O(n * k), where n is the length of `s`.
Each of the (n - k + 1) substrings requires O(k) time to copy.

Space Complexity:
O(min(n, 2^k) * k) for storing unique substrings in the set.
"""

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # The number of distinct sub-strings should be exactly 2^k.
        subString = set()
        l = 0
        for r in range(k, len(s) + 1):
            subString.add(s[l:r])
            l += 1
        
        if len(subString) !=  2 ** k:
            return False
        return True
