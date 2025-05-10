## Hint: Use stack Data structure 

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(len(s) < 2):
            return False
        close = []
            
        for i in range(len(s)):
            if(s[i] == "("): close.append(")")
            elif(s[i] == "["):close.append("]")
            elif(s[i] == "{"):close.append("}")
            else:
                if not close or s[i] != close.pop():
                    return False
        return not close
            
