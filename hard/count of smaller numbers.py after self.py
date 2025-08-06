  """
  Leetcode 315 – Count of Smaller Numbers After Self

  Problem:
  For each element in the input list `nums`, count how many elements to its right 
  are smaller than it, and return a result list `res` of the same length.

  Approach:
  This solution uses a modified Merge Sort algorithm to achieve an efficient 
  time complexity of O(n log n), while counting the number of smaller elements 
  to the right during the merge step.

  Core Idea:
  - Each element is paired with its original index to track its position after sorting.
  - The array is recursively split and sorted using merge sort.
  - During the merge step:
      - When an element from the right half is placed before an element in the left half,
        it means the right element is smaller and originally came after the left element.
        So we increment a counter `rightCount`.
      - When placing a left element into the merged list, we add `rightCount` to its 
        result count in `res`, since that many smaller elements have already passed from the right.

  Key Concepts:
  - This is based on the inversion count concept: if `nums[i] > nums[j]` and `i < j`,
    we consider it a "smaller-after" event.
  - Instead of counting total inversions, we record individual counts for each original index.

  Example:
      Input:  [5, 2, 6, 1]
      Pairs:  [(5,0), (2,1), (6,2), (1,3)]
      Output: [2, 1, 1, 0]
      Explanation:
          - 5 has 2 smaller elements after it: [2, 1]
          - 2 has 1 smaller element after it: [1]
          - 6 has 1 smaller element after it: [1]
          - 1 has none

  Time Complexity:
      - O(n log n): standard merge sort time
  Space Complexity:
      - O(n): auxiliary space for merge and recursion stack

  Returns:
      A list of integers where res[i] is the number of smaller elements to the right of nums[i].
  """

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0 for i in range(len(nums))]
        nums = [(nums[i], i) for i in range(len(nums))]

        def sortAndCount(nums):
            if len(nums) == 1:
                return nums
            mid = len(nums) // 2
            left = sortAndCount(nums[:mid])
            right = sortAndCount(nums[mid:])
            rightCount = 0
            merge = []
            i, j = 0, 0
            for k in range(len(nums)):
                if i >= len(left):
                    merge.append(right[j])
                    j += 1
                    continue
                if j >= len(right):
                    res[left[i][1]] += rightCount
                    merge.append(left[i])
                    i += 1
                    continue
                    
                if left[i][0] > right[j][0]:
                    rightCount += 1
                    merge.append(right[j])
                    j += 1
                else:
                    res[left[i][1]] += rightCount
                    merge.append(left[i])
                    i += 1
            return merge
        sortAndCount(nums)
        return res
                
                
            
        
