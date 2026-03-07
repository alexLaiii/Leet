class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        haveSegment = False
        for c in s:
            if c == "0" and not haveSegment:
                haveSegment = True
            elif c == "1" and haveSegment:
                return False
        return True
            
            
        
