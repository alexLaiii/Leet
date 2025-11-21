"""
Count distinct length-3 palindromic subsequences of form c x c.
Treat each index as the middle x and maintain:
  - leftSeen: chars that appeared on the left so far,
  - rightFrequent: remaining char counts on the right.
For a middle char x at position j, any char c that is in leftSeen
and still has positive count in rightFrequent forms some subsequence
c x c, so we record the pair (c, x) in a set to ensure each pattern
is counted at most once.
"""

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        leftSeen = defaultdict(bool)
        rightFrequent = defaultdict(int)
        counted = set()
        count = 0
        for c in s:
            rightFrequent[c] += 1
        
        for c in s:
            rightFrequent[c] -= 1
            for character in leftSeen:
                if rightFrequent[character] > 0 and (character, c) not in counted:
                    count += 1
                    counted.add((character, c))
            leftSeen[c] = True
        
        return count
            
