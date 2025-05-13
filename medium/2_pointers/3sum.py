"""
Idea: Fix one number (nums[i]) and reduce the problem to a 2Sum problem:

Approach:
Sort the given array in non-decreasing order.
Loop through the array from index 0 to n-1.
For each iteration, set the target as -nums[i].
Set two pointers, j=i+1 and k=n-1.
While j<k, check if nums[j]+nums[k]==target.
If yes, add the triplet {nums[i], nums[j], nums[k]} to the result and move j to the right and k to the left.
If no, move either j or k based on the comparison of nums[j]+nums[k] with target.
To avoid duplicate triplets, skip the iterations where nums[i]==nums[i-1] and also skip the iterations where nums[j]==nums[j-1] or nums[k]==nums[k+1].
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums) == 3): return ([[nums[0], nums[1], nums[2]]]) if(nums[0] + nums[1] + nums[2] == 0) else []
        results = []
        nums.sort()
     
        for i in range(len(nums) - 1):
            if(i != 0):
                if(nums[i] == nums[i-1]):
                    continue
            j = i+1
            k = len(nums) - 1
            while j < k:
                if(j != i + 1):
                    if nums[j] == nums[j - 1]:
                        j += 1
                        continue
                if(k != len(nums) - 1):
                    if(nums[k] == nums[k+1]):
                        k -= 1
                        continue
                sums = nums[i] + nums[j] + nums[k]
                if sums == 0:
                    results.append([nums[i], nums[j], nums[k]])
                    j += 1 
                elif sums > 0:
                    k -= 1
                elif sums < 0:
                    j += 1
        return results

        
        
                        
        
