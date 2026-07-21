"""
Compute the maximum number of active sections ('1's) obtainable after
performing at most one trade operation.

Observation:
- Compress the string into consecutive character segments using
run-length encoding (e.g., "0011100" -> [[0,2], [1,3], [0,2]]).
- Let `one_count` be the total number of '1's in the original string.
- Trading an internal '1' segment merges its adjacent '0' segments into
the active region. The net gain is therefore:
      left_zero_segment_length + right_zero_segment_length
since the length of the traded '1' segment cancels out.
- The answer is the original number of '1's plus the maximum possible
gain among all internal '1' segments.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # segment : count
        segment = [[s[0], 1]]
        one_count = int(s[0])
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                segment[-1][1] += 1
            else:
                segment.append([s[i], 1])
            if s[i] == '1':
                one_count += 1
        
        delta = 0
        for i in range(1, len(segment) - 1):
            if segment[i][0] == '1':
                delta = max(delta, segment[i-1][1] + segment[i+1][1])
        return delta + one_count
                
        
        
                
                
        
