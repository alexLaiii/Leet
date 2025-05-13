"""
Idea: store the count of each char of @magazine and @ransomNote in the character array
- Then subtract the count of magazine from ransomNote to see if there's enough character to build ransome
- The Python built in Counter class acheive the same thing, just cleaner code
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if(len(ransomNote) > len(magazine)):
            return False

        # ransom = [0] * 26
        # maga = [0] * 26
        
        # for i in range(len(magazine)):
        #     maga[ord(magazine[i])-97] += 1
        #     if(i < len(ransomNote)):
        #         ransom[ord(ransomNote[i])-97] += 1

        # for i in range(len(ransom)):
        #     if(maga[i] < ransom[i]): return False
        # return True
        return Counter(ransomNote) - Counter(magazine) == {}
    
             
