    """
    Leetcode 4: Median of Two Sorted Arrays
    ---------------------------------------

    Goal:
    Given two sorted arrays nums1 and nums2, find the median of the combined sorted array 
    in O(log(min(m, n))) time without merging them.

    Key Idea:
    - Perform binary search on the shorter array to partition both arrays into left and right halves.
    - Ensure:
        maxLeftA <= minRightB
        maxLeftB <= minRightA
    - Once this condition is met, we’ve found the correct partition for the median.

    Variables:
    - Total length = m + n
    - i: number of elements taken from nums1 (binary search on this)
    - j = (m + n + 1) // 2 - i → number from nums2 to complete left half
    - maxLeftA = nums1[i-1] if i > 0 else -inf
    - minRightA = nums1[i] if i < len(nums1) else inf
    - Likewise for nums2

    Median Rules:
    - If (m + n) is odd → median = max(maxLeftA, maxLeftB)
    - If (m + n) is even → median = (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2

    Binary Search Logic:
    - If maxLeftA > minRightB → move left (r = i - 1)
    - If maxLeftB > minRightA → move right (l = i + 1)
    - Else partition is valid

    Time Complexity:
    - O(log(min(m, n)))

    Edge Cases:
    - One or both arrays empty
    - Arrays with very different lengths
    - All elements in one array are greater than all in the other
    - Duplicates

    Example:
    nums1 = [1, 3], nums2 = [2]
    → Combined = [1, 2, 3], Median = 2

    nums1 = [1, 2], nums2 = [3, 4]
    → Combined = [1, 2, 3, 4], Median = (2 + 3)/2 = 2.5
    """
