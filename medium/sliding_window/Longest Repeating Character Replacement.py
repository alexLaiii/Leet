"""
Intitution: 
By tracking the most frequent character in the current window, 
Key Logic:
The key condition is to check [(current window length) - (most frequent character count in current window)] <= k, where k is the maximum replacement allow

Explanation: 
Since [(current window length) - (most frequent character count in current window)] will give you the number of characters need to replace to be a valid string
e.g -> AAABBCA, will be [7-4] = 3, where 4 is the most frequent character, which is A here, and 3 is the number of character need replacment, which is BBC here.
If the result > k, then the string is invalid, because we ony allow to make most of k replacement, so we shrink the window from the left, and check the condition again
if the result <= k, then the string is valid, we do nothing and check if the current window length is the max.
"""

# Intiutive solution:
# Time Complexity: O(n * 26)
# Space Complexity: O(1)
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maps = {}
        most_freq, max_count, i = 0,0, 0
        
        for j in range(len(s)):
            # if s[i] is already in the map, increment it by 1, if not, set it to 0
            maps[s[j]] = 1 + maps.get(s[j], 0)
            # while the window is invalid
            while (j - i + 1) - max(maps.values()) > k:
                maps[s[i]] -= 1
                i += 1
            max_count = max(j - i + 1, max_count)

        return max_count

        


            
                
            
            
