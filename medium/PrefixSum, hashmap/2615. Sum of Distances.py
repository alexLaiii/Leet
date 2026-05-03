"""
Compute the sum of distances between each index i and all other indices j
such that nums[i] == nums[j].

Key Idea:
Instead of brute force (O(n^2)), group indices by value and use prefix sums
to compute distances in O(1) per index.

For each value x:
- Store prefix sums of indices where x appears.
- Track how many times x has appeared so far (occurrence count).

For current index i:
Let:
- occurs = number of same values seen before (left count)
- k = total occurrences of x
- prefix[x] = prefix sum array of indices for value x

Split contribution into two parts:

1. Left side (indices before i):
   distance = i * occurs - sum(left indices)

2. Right side (indices after i):
   distance = sum(right indices) - i * right_count

Using prefix sums:
- sum(left indices) = prefix[x][occurs - 1]
- sum(right indices) = prefix[x][-1] - prefix[x][occurs]

Total distance = left + right

This avoids recomputing distances and reduces complexity.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        prefix = defaultdict(list)
        for i in range(len(nums)):
            if prefix[nums[i]]:
                prefix[nums[i]].append(prefix[nums[i]][-1] + i)
            else:
                prefix[nums[i]].append(i)
        res = []


        occurrence = defaultdict(int)
        for i in range(len(nums)):
            x = nums[i]
            k = len(prefix[x])
            occurs = occurrence[nums[i]]
            left_prefix = right_prefix = left_val = right_val =  0
            if occurs > 0:
                left_prefix = -(prefix[x][occurs - 1])
            right_prefix = prefix[x][-1] - prefix[x][occurs]

            res.append((i * occurs + (-(i * (k-1-occurs))))+ (left_prefix + right_prefix))
            occurrence[nums[i]] += 1
                      
        return res
        
        
            
        
