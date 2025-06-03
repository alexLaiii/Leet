"""
Idea: Patience Sort + Binary Search (Optimal solution)

Patience Sort (Interview-useful, real-life useless):
  - You cannot place a higher number on top of a pile ending in a lower number
  - Place the card on the leftmost pile whose top is ≥ current number (use Binary Search)
  - If no suitable pile is found, create a new pile
  - The number of piles after processing the entire `nums` array is the length of the Longest Increasing Subsequence (LIS)

Example with nums = [4, 10, 4, 3, 8, 9]:

Step-by-step pile simulation:
- 4 → no pile → create pile1: [4]
- 10 → > 4 → create pile2: [10]
- 4 → ≤ 4 → place in pile1: [4, 4]
- 3 → ≤ 4 → place in pile1: [4, 4, 3]
- 8 → ≤ 10 but > 3 → place in pile2: [10, 8]
- 9 → > 8 → create pile3: [9]

Final piles:
pile1: [4, 4, 3]
pile2: [10, 8]
pile3: [9]

Notice: The number of piles is 3, which is the length of the LIS [3, 8, 9].

Implementation notes:
- Linearly scan `nums`
- For each number, use binary search to find the correct pile to replace the top
- Use replacement instead of full append to simplify logic, since only the top matters

Time Complexity:
- O(n log n): each of n elements performs a binary search on the `piles` list

Space Complexity:
- O(n): in worst case (strictly increasing `nums`), we create one pile per number
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        # take the largest of each position
        if not nums:
            return 0
        
        patience_sort = [nums[0]]
        for i in range(1, len(nums)):
            left, right = 0, len(patience_sort)
            while right > left:
                mid = (left + right) // 2
                if(patience_sort[mid] >= nums[i]):
                    right = mid 
                # implicitly said if (patience_sort[mid] < nums[i])
                else:
                    left  = mid + 1
            if left < len(patience_sort):
                patience_sort[left] = nums[i]
            else:
                patience_sort.append(nums[i])
        return len(patience_sort)
                
            
            
            
            
            
                

        

   
        
        
