class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if(n == 1):
            return 1
        if(n == 2):
            return 2
        dynammic_table = [1,2]
        j = 0
        for i in range(3,n):
            dynammic_table[j] = dynammic_table[0] + dynammic_table[1]
            if(j == 0):
                j = 1
            else:
                j = 0
        return dynammic_table[0] + dynammic_table[1]
            
            
              

        
        
