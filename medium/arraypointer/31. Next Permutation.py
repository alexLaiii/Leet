"""
Rearranges nums in-place into the next lexicographical permutation.

The algorithm:
1. Scan from left to right to find the rightmost index `i` such that
   nums[i] < nums[i + 1] (the pivot). If no such index exists, the
   array is in descending order, so we sort it ascending and return.
2. Among elements to the right of the pivot, find the smallest element
   that is strictly greater than nums[i].
3. Swap the pivot with this element.
4. Sort the suffix (elements to the right of the pivot) in ascending
   order so the resulting array is the smallest permutation larger
   than the original.
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastPair = [-1,-1]
        smallestIdx = -1
        
        for i in range(len(nums)):
            if i > 0 and nums[i] > nums[i - 1]:
                lastPair[0] = i - 1
                lastPair[1] = i
                smallestIdx = i

        if lastPair[0] != -1:
            for i in range(lastPair[1], len(nums)):
                if nums[i] < nums[smallestIdx] and nums[i] > nums[lastPair[0]]:
                    smallestIdx = i

            nums[lastPair[0]], nums[smallestIdx] = nums[smallestIdx], nums[lastPair[0]]

            nums[lastPair[1] : len(nums)] = sorted(nums[lastPair[1] : len(nums)])
        else:
            nums.sort()
