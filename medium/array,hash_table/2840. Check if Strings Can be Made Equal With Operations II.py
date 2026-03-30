"""
Determine whether two strings can be made equal using operations that only allow
swapping characters within indices of the same parity (even with even, odd with odd).

Key Insight:
Characters at even indices can only move among even positions, and characters at
odd indices can only move among odd positions. Therefore, s1 can be transformed
into s2 if and only if both strings have identical frequency distributions for:
    1. Characters at even indices
    2. Characters at odd indices

Approach:
- Use two fixed-size arrays (length 26 for lowercase English letters) to track
  frequency differences:
    - even[i]: net count difference of character i at even indices
    - odd[i]: net count difference of character i at odd indices
- Traverse both strings simultaneously:
    - Increment count for s1 and decrement for s2 at corresponding parity index
- At the end, both arrays must be all zeros for the transformation to be possible

Time Complexity:
O(n), where n is the length of the strings

Space Complexity:
O(1), since arrays are of fixed size (26)

Constraints:
- Assumes input strings consist of lowercase English letters
"""
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        OFFSET = ord("a")
        evenSet = [0] * 26
        oddSet = [0] * 26

        for i in range(len(s1)):
            valS1 = ord(s1[i])
            valS2 = ord(s2[i])
            if i % 2 == 0:
                evenSet[valS1 - OFFSET] += 1
                evenSet[valS2 - OFFSET] -= 1
            else: 
                oddSet[valS1 - OFFSET] += 1
                oddSet[valS2 - OFFSET] -= 1
        

        return all(x == 0 for x in evenSet) and all(y == 0 for y in oddSet)
            
        
