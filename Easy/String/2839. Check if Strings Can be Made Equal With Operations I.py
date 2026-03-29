"""
Logical code, nothing fancy really
"""

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if (s1[0] != s2[0] or s1[2] != s2[2])and (s1[0] != s2[2] or s1[2] != s2[0]):
            return False
        if (s1[1] != s2[1] or s1[3] != s2[3]) and (s1[1] != s2[3] or s1[3] != s2[1]):
            return False
        return True
            
        
