"""
Return the k-th bit in the n-th binary string S_n.

The string sequence is defined as:
  S_1 = "0"
  S_i = S_{i-1} + "1" + reverse(invert(S_{i-1})) for i > 1

This solution simulates the construction directly:
- Start with S_1 as [0]
- For each next string, build the inverted version of the current
string, reverse it, and append it after a middle 1
- Return the (k - 1)-th bit as a string

Args:
  n: The index of the binary string to construct.
  k: The 1-based position of the bit to return.

Returns:
  The k-th bit of S_n as a string, either "0" or "1".

Time Complexity:
  O(2^n), since the full string is built.

Space Complexity:
  O(2^n), since the full string is stored.
"""

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        curr = [0]
        for i in range(n - 1):
            invert = []
            for j in range(len(curr)):
                invert.append(curr[j] ^ 1)
            curr = curr + [1] + invert[::-1]

        
        return str(curr[k-1])
            
            
            
            

            
