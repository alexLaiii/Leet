"""
Problem: Leetcode 16 - 3Sum Closest

Given an integer array `nums` of length n and an integer `target`, 
the goal is to find the sum of three integers in `nums` such that 
the sum is closest to `target`. Return this closest sum. 
It's guaranteed that there is exactly one solution.

Core Idea:
- This problem is a variation of the classic "3Sum" problem, 
  but instead of finding triplets that sum to exactly the target, 
  we aim to find a triplet whose sum is closest to the target.

Algorithm Concept:
1. Sort the array to enable the use of the two-pointer technique.
2. Iterate through each index `k` in the array:
   - For each fixed index `k`, use two pointers (`i`, `j`) to scan 
     the remaining elements from both ends (`k+1` to end of array).
   - Calculate the current sum of the triplet: nums[k] + nums[i] + nums[j].
   - If the current sum is closer to the target than the previously stored 
     closest sum, update the closest sum.
   - Adjust the pointers based on whether the current sum is less than 
     or greater than the target:
     - If the current sum is less than the target, move the left pointer (`i`) rightward.
     - If the current sum is greater than the target, move the right pointer (`j`) leftward.
     - If the current sum equals the target, return it immediately (early exit).
3. After checking all possible triplets, return the closest sum found.

Time Complexity: O(n^2)
    - Sorting takes O(n log n)
    - Two-pointer scan for each element takes O(n), done n times
Space Complexity: O(1)
    - No extra space used beyond a few variables

This solution guarantees finding the unique closest sum in optimal time.
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        
        nums.sort()
        closestSum = nums[0] + nums[1] + nums[2]
        for k in range(len(nums)):
            if k != 0 and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = len(nums) - 1
            while i < j:
                currSum = nums[k] + nums[i] + nums[j]
                if currSum == target:
                    return currSum

                if abs(target - currSum) < abs(target - closestSum):
                    closestSum = currSum
                    
                if currSum < target:
                    i += 1
                else:
                    j -= 1

        return closestSum
                    
                    
