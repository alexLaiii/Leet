"""
Assigns a rank to each element in the array based on its value.

The algorithm sorts a copy of the input array, then traverses the sorted
values to assign consecutive ranks to each distinct value. Duplicate
values are assigned the same rank by checking whether a rank has already
been recorded. Finally, it constructs the result by replacing each
original element with its assigned rank.

Time Complexity:
    O(n log n)
    - Sorting the array takes O(n log n).
    - Assigning ranks to distinct values takes O(n).
    - Building the result array takes O(n).

Space Complexity:
    O(n)
    - O(n) for the sorted copy of the array.
    - O(n) for the rank mapping.
    - O(n) for the output array.
"""

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = defaultdict(int)
        sorted_arr = sorted(arr)
        rank_count = 1
        for n in sorted_arr:
            if n not in rank:
                rank[n] = rank_count 
                rank_count  += 1
        res = []
        for n in arr:
            res.append(rank[n])
        return res        
        
        
        
