"""
This problem is a fking hell, it cooked me badly.
Reminder If a failed to solve it again, try to draw out graph, indicating split ascending, like 4567012, will split into 4567 left graph, 012 right graph, but the value below lefthope it helps.
Idea: 
Binary search with coniditon that determine which part of the array you are in, the left sorted portion or the right sorted portion
Once the the location of your mid is determined, that write the if else cases accordingly

Example:
[4,5,6,7,0,1,2] , obviously, the left sorted portion is 4567, and the right sorted portion is 012, 
How to determine which portion the mid is in? 
Note that in:
left sorted portion, values are >= nums[left] and increase up to the rotation point.
right sorted portion, values are < nums[left]
With these condition, we can easily check which portion we are in, That is:
If nums[mid] >= nums[left]: -> in left portion
If nums[mid] < nums[left]: -> in right portion

After which portion is founded, write if else case accordingly
If mid is in left portion, these things can happen
    if target > nums[mid], then set left to mid + 1, since everything before mid is guranteen smaller (left portion behaviour)
    if target < nums[left], then set left to mid + 1, since the smallest in this portion is the left most value, so it cannot be in the left portion
    if target >= nums[left] and target < nums[mid], then set right = mid - 1, since this eplicitly mean target is in this portion
If mid is in right portion, these things can happen
    if target > nums[right], then set right = mid - 1, since the largest value of this portion is the right most value, so it cannot be in the right portion
    if target < nums[mid], then set right = mid - 1, since everything after mid is only increasing
    if target <= nums[right] and target > nums[mid], then set left = mid + 1, since this eplicitly mean target is in this portion

And this is the whole idea, brain rotting, lot of cases to figure out.

Time Complexity: 
O(logn): this is binary search with extra condition
Space Complexity
O(1)
"""


class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while r >= l:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                # must land on right portion, 
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                   l = m + 1
        return -1

            
     

            
