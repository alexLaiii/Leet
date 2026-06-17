class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Finds the unique values that appear in both arrays.

        Converts both input arrays into sets to remove duplicates and allow
        O(1) average-time lookup. Then checks each unique value from nums1
        and adds it to the result if it also exists in nums2.
        """
        res = set()
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        
        for n in nums1_set:
            if n in nums2_set:
                res.add(n)
        
        return list(res)
