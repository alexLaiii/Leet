"""
Note a slightly tricky part, the isomorphism has to go both ways.
Knowing this I should be able to reproduce this.
"""



class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_s, map_t= {}, {}

        # since len(s) == len(t) is guranteen
        for i in range(len(s)):
            if(s[i] not in map_s):
                map_s[s[i]] = t[i]
            if(t[i] not in map_t):
                map_t[t[i]] = s[i]
            if map_t[t[i]] != s[i] or map_s[s[i]] != t[i]:
                return False

        return True
               
        
            
        
        
        
