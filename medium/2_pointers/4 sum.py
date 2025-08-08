"""
Problem: Leetcode 18 - 4Sum

Core Idea:
- Sort the array first to make it easier to handle duplicates and use two pointers.
- Fix two numbers (`nums[k]` and `nums[l]`) using two nested loops.
- Then use the two-pointer technique (`i` and `j`) to search for the remaining two numbers.
- This reduces the 4Sum problem to a 2Sum problem on the remaining subarray.

Steps:
1. Sort the input array `nums`.
2. Loop through the array with two indices `k` and `l` to fix the first two numbers.
3. For each fixed pair (nums[k], nums[l]), initialize two pointers:
    - `i = l + 1` (start of the remaining range)
    - `j = len(nums) - 1` (end of the array)
4. While `i < j`, calculate the sum of the four numbers:
    - If sum == target → append the quadruplet to result
    - If sum < target → move `i` forward to increase sum
    - If sum > target → move `j` backward to decrease sum
5. Skip over duplicates for all four indices to ensure unique quadruplets.

Time Complexity: O(n^3)
    - Two nested loops (O(n^2)) and a two-pointer scan (O(n)) for each pair

Space Complexity: O(1) extra space (excluding the result list)

This method efficiently finds all unique quadruplets whose sum equals the target.
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []
        for k in range(len(nums) - 3):
            if k != 0 and nums[k] == nums[k - 1]:
                continue
            for l in range(k + 1, len(nums) - 2):
                if l != k + 1 and nums[l] == nums[l - 1]:
                    continue
                i = l + 1
                j = len(nums) - 1
                while i < j:
                    if i != l + 1 and nums[i] == nums[i - 1]:
                        i += 1
                    elif j != len(nums) - 1 and nums[j] == nums[j + 1]:
                        j -= 1
                    elif nums[k] + nums[l] + nums[i] + nums[j] < target:
                        i += 1
                    elif nums[k] + nums[l] + nums[i] + nums[j] > target:
                        j -= 1
                    else:
                        res.append([nums[k], nums[l], nums[i], nums[j]])
                        j -= 1
        return res

        
