"""
Super simple problem
"""
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        M, N = len(nums1), len(nums2)
        i = j = 0
        while i < M and j < N:
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                return nums1[i]
        return -1
