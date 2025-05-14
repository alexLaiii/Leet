"""
Use binary search to locate the square root of x, always round down
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
      
        if x == 0:
            return 0
        if x == 1:
            return 1
        left,right, ans = 1,x , -1

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                right = mid - 1
                ans = mid - 1
            if mid * mid < x:
                left = mid + 1
                ans = mid
        
        return ans
            
        
        
