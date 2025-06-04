"""
This is something called a closing sliding window mountain sorted array, huh
These constraint are really important in this question: 
1. -231 <= nums[i] <= 231 - 1
2. nums[i] != nums[i + 1] for all valid i.

Condition 1 ensure that the peak element exists, since if on part is ascending, then the other part must be descending, also ensure that no matter how right or how left
your binary search start with, you will always finda peak later on since the last element is always smaller than the second last element.
Condition 2 ensure that neighbour deplicate does not exist, so there will be no unsolvable case like [4,5,5,5,5,5,5,4]

We use binary search to randomly find an element and check its next element, if the next element is greater, then the next element might be peak, might be not
But what we can make sure is the current element cannot be peak, so we set left to the index of the next element and continue searching.

If the next element is smaller, then this element might be peak, again might be not, be we cannot exclude it, so we set right to the current index to smaller the gap.
By looping this process, the left index keep increasing and the right index keep decreasing, they we eventually met at the peak point.
Thus, when left == right, the result is found, and left and right are the index of the peak elenment

Time Complexity:
O(logn): binary Search
Space Complexity:
O(1)

"""



class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while(left != right):
            mid = (left + right) // 2
            if(nums[mid] > nums[mid + 1]):
                right = mid
            else:
                left = mid + 1
        return left
        
