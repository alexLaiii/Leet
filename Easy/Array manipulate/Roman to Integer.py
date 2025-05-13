"""
Definitely cooked if I can't reproduce this.
Just remember the number less than the next num is always subtraction, e.g IX, 1 < 10 so 10 - 1
------------- the number larger than the next num is always addition,  e.g XI 10 < 1 -> false, so 10 + 1
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        maps = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
     
        num = maps[s[-1]]
        for i in range(len(s)-2, -1, -1):
    
            if maps[s[i+1]] <= maps[s[i]]:
                num += maps[s[i]]
            else:
                num -= maps[s[i]]
        return num            
        
