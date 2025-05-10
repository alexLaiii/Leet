###
Idea / Proof:

The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
All other containers are less wide and thus would need a higher water level in order to hold more water.
The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.
Variables left and right define the container under consideration. We initialize them to first and last line, meaning the widest container. 
Variable max_area will keep track of the highest amount of water we managed so far. We compute left - right, the width of the current container, and min(height[left], height[right]), 
the water level that this container can support. Multiply them to get how much water this container can hold, and update water accordingly. 
Next remove the smaller one of the two lines from consideration, as justified above in "Idea / Proof". Continue until there is nothing left to consider, then return the result.
###


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
        
