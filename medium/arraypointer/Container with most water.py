class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left, right = 0, len(height) - 1
        while(left != right):
            area = (right - left) * min(height[left], height[right])
            if(max_area < area): max_area = area
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area
        
